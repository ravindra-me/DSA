"""AI provider abstraction.

Providers implement one method, `complete(system, user) -> str`. Adding a
provider means subclassing Provider and registering it in `create_provider`.
Any OpenAI-compatible endpoint (Azure OpenAI, OpenRouter, Groq, ...) works
with the "openai" provider plus OPENAI_BASE_URL. Google Gemini (including its
free tier) has a dedicated provider that uses the native Gemini API.

API keys are read from the environment only (populated from GitHub Secrets),
sent only in request headers, and never logged.
"""

from __future__ import annotations

import json
import os
import random
import re
import socket
import time
import urllib.error
import urllib.request
from typing import Any, Callable, Dict, Mapping, Optional

from . import log
from .config import AISettings
from .errors import AIError, AIRetryableError, AIUnavailableError, ConfigError

RETRYABLE_STATUS = {408, 409, 425, 429, 500, 502, 503, 504, 529}
# Order matters for provider "auto": the first key found wins.
KEY_ENV = {"openai": "OPENAI_API_KEY", "anthropic": "ANTHROPIC_API_KEY", "gemini": "GEMINI_API_KEY"}
MODEL_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


class Provider:
    name = "abstract"

    def __init__(self, model: str) -> None:
        self.model = model

    def complete(self, system: str, user: str) -> str:
        raise NotImplementedError


def _post_json(url: str, headers: Mapping[str, str], body: Dict[str, Any], timeout: int) -> Dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "dsa-learning-agent/1.0", **headers},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:600]
        message = f"HTTP {exc.code} from {url}: {detail}"
        if exc.code in RETRYABLE_STATUS:
            retry_after = exc.headers.get("retry-after") if exc.headers else None
            if not retry_after:
                # Gemini reports the wait in the body: "retryDelay": "37s"
                hint = re.search(r'"retryDelay"\s*:\s*"(\d+(?:\.\d+)?)s"', detail)
                retry_after = hint.group(1) if hint else None
            raise _with_retry_after(AIRetryableError(message), retry_after) from None
        if exc.code == 404:
            raise AIUnavailableError(message + " (model not found or not available to this key)") from None
        if exc.code in (401, 403):
            message += " (check that the API key secret is set correctly and has access to this model)"
        raise AIError(message) from None
    except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError) as exc:
        raise AIRetryableError(f"network error calling {url}: {exc}") from None
    except ValueError as exc:
        raise AIRetryableError(f"invalid JSON from {url}: {exc}") from None


def _with_retry_after(exc: AIRetryableError, value: Optional[str]) -> AIRetryableError:
    try:
        exc.retry_after = min(float(value), 120.0) if value else None  # type: ignore[attr-defined]
    except ValueError:
        exc.retry_after = None  # type: ignore[attr-defined]
    return exc


def with_retries(call: Callable[[], str], attempts: int, what: str, sleep: Callable[[float], None] = time.sleep) -> str:
    """Retry transient failures with exponential backoff + jitter (bounded)."""
    for attempt in range(1, attempts + 1):
        try:
            return call()
        except AIRetryableError as exc:
            if attempt == attempts:
                raise AIUnavailableError(f"{what} failed after {attempts} attempts: {exc}") from None
            delay = getattr(exc, "retry_after", None) or min(90.0, 5.0 * 2.0 ** attempt) + random.uniform(0, 1)
            log.warn(f"{what}: transient error (attempt {attempt}/{attempts}), retrying in {delay:.0f}s: {exc}")
            sleep(delay)
    raise AssertionError("unreachable")


class OpenAIProvider(Provider):
    name = "openai"

    def __init__(self, model: str, api_key: str, base_url: str, settings: AISettings) -> None:
        super().__init__(model)
        self._api_key = api_key
        self._url = base_url.rstrip("/") + "/chat/completions"
        self._settings = settings

    def complete(self, system: str, user: str) -> str:
        body: Dict[str, Any] = {
            "model": self.model,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "response_format": {"type": "json_object"},
            "max_completion_tokens": self._settings.max_output_tokens,
        }
        if self._settings.temperature is not None:
            body["temperature"] = self._settings.temperature
        data = _post_json(self._url, {"Authorization": f"Bearer {self._api_key}"}, body, self._settings.timeout_seconds)
        try:
            choice = data["choices"][0]
            content = choice["message"]["content"]
        except (KeyError, IndexError, TypeError):
            raise AIRetryableError(f"unexpected OpenAI response shape: {str(data)[:300]}") from None
        if choice.get("finish_reason") == "length":
            raise AIError("response was truncated (finish_reason=length); increase ai.maxOutputTokens")
        if not content:
            raise AIRetryableError("empty response content")
        return content


class AnthropicProvider(Provider):
    name = "anthropic"

    def __init__(self, model: str, api_key: str, base_url: str, settings: AISettings) -> None:
        super().__init__(model)
        self._api_key = api_key
        self._url = base_url.rstrip("/") + "/v1/messages"
        self._settings = settings

    def complete(self, system: str, user: str) -> str:
        body: Dict[str, Any] = {
            "model": self.model,
            "max_tokens": self._settings.max_output_tokens,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        }
        if self._settings.temperature is not None:
            body["temperature"] = self._settings.temperature
        headers = {"x-api-key": self._api_key, "anthropic-version": "2023-06-01"}
        data = _post_json(self._url, headers, body, self._settings.timeout_seconds)
        blocks = data.get("content")
        if not isinstance(blocks, list):
            raise AIRetryableError(f"unexpected Anthropic response shape: {str(data)[:300]}")
        if data.get("stop_reason") == "max_tokens":
            raise AIError("response was truncated (stop_reason=max_tokens); increase ai.maxOutputTokens")
        text = "".join(b.get("text", "") for b in blocks if isinstance(b, dict) and b.get("type") == "text")
        if not text.strip():
            raise AIRetryableError("empty response content")
        return text


class GeminiProvider(Provider):
    """Google Gemini via the native generateContent API (works on the free tier)."""

    name = "gemini"

    def __init__(self, model: str, api_key: str, base_url: str, settings: AISettings) -> None:
        super().__init__(model)
        if not MODEL_NAME.match(model):
            raise ConfigError(f"invalid Gemini model name {model!r}")
        self._api_key = api_key
        self._url = f"{base_url.rstrip('/')}/models/{model}:generateContent"
        self._settings = settings
        self._thinking_level = settings.gemini_thinking_level

    def complete(self, system: str, user: str) -> str:
        config: Dict[str, Any] = {
            "maxOutputTokens": self._settings.max_output_tokens,
            "responseMimeType": "application/json",
        }
        if self._settings.temperature is not None:
            config["temperature"] = self._settings.temperature
        if self._thinking_level:
            # Less "thinking" = much faster responses; plenty for lesson generation.
            config["thinkingConfig"] = {"thinkingLevel": self._thinking_level}
        body = {
            "systemInstruction": {"parts": [{"text": system}]},
            "contents": [{"role": "user", "parts": [{"text": user}]}],
            "generationConfig": config,
        }
        # The key goes in a header, never in the URL, so it cannot appear in logged URLs.
        headers = {"x-goog-api-key": self._api_key}
        try:
            data = _post_json(self._url, headers, body, self._settings.timeout_seconds)
        except AIError as exc:
            if "HTTP 400" not in str(exc) or "thinking" not in str(exc).lower() or "thinkingConfig" not in config:
                raise
            log.warn(f"{self.model} rejected thinkingConfig; retrying without it")
            self._thinking_level = None
            del config["thinkingConfig"]
            data = _post_json(self._url, headers, body, self._settings.timeout_seconds)
        candidates = data.get("candidates")
        if not isinstance(candidates, list) or not candidates:
            feedback = data.get("promptFeedback") or str(data)[:300]
            raise AIRetryableError(f"Gemini returned no candidates: {feedback}")
        candidate = candidates[0]
        if candidate.get("finishReason") == "MAX_TOKENS":
            raise AIError("response was truncated (finishReason=MAX_TOKENS); increase ai.maxOutputTokens")
        parts = (candidate.get("content") or {}).get("parts") or []
        # Skip "thought" parts from thinking models; keep only the answer.
        text = "".join(p.get("text", "") for p in parts if isinstance(p, dict) and not p.get("thought"))
        if not text.strip():
            raise AIRetryableError(f"empty Gemini response (finishReason={candidate.get('finishReason')})")
        return text


class FallbackProvider(Provider):
    """Tries the primary model; if it stays overloaded/unavailable after
    retries, switches to the next fallback model for the rest of the run."""

    def __init__(self, providers: "list[Provider]", attempts: int, sleep: Callable[[float], None] = time.sleep) -> None:
        super().__init__(providers[0].model)
        self.name = providers[0].name
        self._providers = providers
        self._index = 0
        self._attempts = attempts
        self._sleep = sleep

    def complete(self, system: str, user: str) -> str:
        while True:
            current = self._providers[self._index]
            try:
                return with_retries(
                    lambda: current.complete(system, user), self._attempts, f"{current.name}/{current.model}", self._sleep
                )
            except AIUnavailableError as exc:
                if self._index + 1 >= len(self._providers):
                    raise
                self._index += 1
                self.model = self._providers[self._index].model
                log.warn(f"model {current.model} is unavailable ({str(exc)[:200]}); switching to fallback model {self.model}")


def create_provider(
    settings: AISettings, env: Optional[Mapping[str, str]] = None, fallback: bool = True
) -> Provider:
    env = os.environ if env is None else env
    name = settings.provider
    if name == "auto":
        name = next((p for p, var in KEY_ENV.items() if env.get(var, "").strip()), "")
        if not name:
            raise ConfigError(
                "no AI API key found. Add a GEMINI_API_KEY, OPENAI_API_KEY or ANTHROPIC_API_KEY repository secret "
                "(Settings -> Secrets and variables -> Actions)."
            )
    api_key = env.get(KEY_ENV[name], "").strip()
    if not api_key:
        raise ConfigError(f"AI provider '{name}' selected but the {KEY_ENV[name]} secret is not set")
    model = settings.model_override or settings.models.get(name)
    if not model:
        raise ConfigError(f"no model configured for provider '{name}' (set ai.models.{name} or DSA_AI_MODEL)")
    base_url = settings.base_urls.get(name)
    if not base_url:
        raise ConfigError(f"no base URL configured for provider '{name}'")
    cls = {"openai": OpenAIProvider, "anthropic": AnthropicProvider, "gemini": GeminiProvider}[name]
    primary = cls(model, api_key, base_url, settings)
    fallbacks = settings.fallback_override if settings.fallback_override is not None else settings.fallback_models.get(name, ())
    extra = [m for m in dict.fromkeys(fallbacks) if m != model]
    if not fallback or not extra:
        return primary
    return FallbackProvider([primary] + [cls(m, api_key, base_url, settings) for m in extra], settings.max_attempts)


# --------------------------------------------------------------------------- JSON handling

_ESCAPE = re.compile(r"\\(.)", flags=re.DOTALL)


def _repair_escapes(text: str) -> str:
    """Double any backslash that does not start a valid JSON escape. Scans
    escape pairs left to right, so valid sequences like \\\\ stay intact."""
    return _ESCAPE.sub(lambda m: m.group(0) if m.group(1) in '"\\/bfnrtu' else "\\\\" + m.group(1), text)


def extract_json(text: str) -> Dict[str, Any]:
    """Parse a JSON object from a model response, tolerating code fences or
    stray prose around it."""
    candidates = [text.strip()]
    fence = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, flags=re.DOTALL)
    if fence:
        candidates.append(fence.group(1))
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end > start:
        candidates.append(text[start : end + 1])
    for candidate in candidates:
        # strict=False accepts raw newlines/tabs inside strings; the second
        # variant also repairs invalid escapes such as "\d" or "\(".
        for variant in (candidate, _repair_escapes(candidate)):
            try:
                value = json.loads(variant, strict=False)
            except ValueError:
                continue
            if isinstance(value, dict):
                return value
    raise ValueError(
        f"response did not contain a valid JSON object ({len(text)} chars; "
        f"starts {text[:120]!r} ... ends {text[-120:]!r})"
    )


def complete_json(
    provider: Provider,
    system: str,
    user: str,
    validate: Callable[[Dict[str, Any]], Dict[str, Any]],
    what: str,
    attempts: int,
    sleep: Callable[[float], None] = time.sleep,
) -> Dict[str, Any]:
    """Ask for JSON, retrying transient API errors and malformed/invalid output.

    `validate` must return the cleaned payload or raise ValueError describing
    what is wrong; the description is fed back to the model on the retry.
    """
    feedback = ""
    for attempt in range(1, attempts + 1):
        prompt = user if not feedback else (
            f"{user}\n\nIMPORTANT: your previous answer was rejected: {feedback}\n"
            "Return a corrected, complete JSON object that follows the schema exactly."
        )
        started = time.monotonic()
        text = with_retries(lambda: provider.complete(system, prompt), attempts, what, sleep)
        log.info(f"{what}: received {len(text)} characters in {time.monotonic() - started:.1f}s")
        try:
            return validate(extract_json(text))
        except ValueError as exc:
            feedback = str(exc)[:1000]
            log.warn(f"{what}: invalid response (attempt {attempt}/{attempts}): {feedback}")
    raise AIError(f"{what}: model did not return valid output after {attempts} attempts (last problem: {feedback})")
