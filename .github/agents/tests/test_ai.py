import io
import json
import unittest
import urllib.error
from unittest import mock

from helpers import TempRepo, temp_settings

from dsa_agent import ai
from dsa_agent.errors import AIError, ConfigError


class _Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def http_error(code, body="{}"):
    return urllib.error.HTTPError("https://x", code, "err", {}, io.BytesIO(body.encode()))


class ProviderTests(unittest.TestCase):
    def setUp(self):
        self._repo = TempRepo()
        self.settings = temp_settings(self._repo.__enter__())

    def tearDown(self):
        self._repo.__exit__(None, None, None)

    def test_auto_detects_provider_from_secret(self):
        p = ai.create_provider(self.settings.ai, {"ANTHROPIC_API_KEY": "k"})
        self.assertEqual((p.name, p.model), ("anthropic", "claude-sonnet-5-5"))
        p = ai.create_provider(self.settings.ai, {"OPENAI_API_KEY": "k", "ANTHROPIC_API_KEY": "k"})
        self.assertEqual(p.name, "openai")

    def test_missing_key_is_a_clear_error(self):
        with self.assertRaisesRegex(ConfigError, "OPENAI_API_KEY"):
            ai.create_provider(self.settings.ai, {})

    def test_model_override(self):
        settings = temp_settings(self.settings.repo_root, DSA_AI_MODEL="my-model", DSA_AI_PROVIDER="openai")
        self.assertEqual(ai.create_provider(settings.ai, {"OPENAI_API_KEY": "k"}).model, "my-model")

    def test_openai_request_and_retry_on_429(self):
        provider = ai.create_provider(self.settings.ai, {"OPENAI_API_KEY": "sk-secret"})
        ok = _Response(json.dumps({"choices": [{"message": {"content": "{\"a\": 1}"}, "finish_reason": "stop"}]}).encode())
        with mock.patch("urllib.request.urlopen", side_effect=[http_error(429), ok]) as urlopen:
            text = ai.with_retries(lambda: provider.complete("sys", "user"), 3, "test", sleep=lambda s: None)
        self.assertEqual(json.loads(text), {"a": 1})
        request = urlopen.call_args[0][0]
        self.assertEqual(request.get_header("Authorization"), "Bearer sk-secret")
        self.assertEqual(json.loads(request.data)["response_format"], {"type": "json_object"})

    def test_auth_error_is_not_retried_and_hides_key(self):
        provider = ai.create_provider(self.settings.ai, {"OPENAI_API_KEY": "sk-secret"})
        with mock.patch("urllib.request.urlopen", side_effect=[http_error(401)]) as urlopen:
            with self.assertRaises(AIError) as ctx:
                ai.with_retries(lambda: provider.complete("s", "u"), 3, "test", sleep=lambda s: None)
        self.assertEqual(urlopen.call_count, 1)
        self.assertNotIn("sk-secret", str(ctx.exception))

    def test_retries_are_bounded(self):
        provider = ai.create_provider(self.settings.ai, {"ANTHROPIC_API_KEY": "k"})
        with mock.patch("urllib.request.urlopen", side_effect=[http_error(503)] * 3) as urlopen:
            with self.assertRaisesRegex(AIError, "after 3 attempts"):
                ai.with_retries(lambda: provider.complete("s", "u"), 3, "test", sleep=lambda s: None)
        self.assertEqual(urlopen.call_count, 3)

    def test_anthropic_truncation_is_reported(self):
        provider = ai.create_provider(self.settings.ai, {"ANTHROPIC_API_KEY": "k"})
        body = {"content": [{"type": "text", "text": "{"}], "stop_reason": "max_tokens"}
        with mock.patch("urllib.request.urlopen", return_value=_Response(json.dumps(body).encode())):
            with self.assertRaisesRegex(AIError, "maxOutputTokens"):
                provider.complete("s", "u")


class GeminiTests(unittest.TestCase):
    def setUp(self):
        self._repo = TempRepo()
        self.settings = temp_settings(self._repo.__enter__())
        self.provider = ai.create_provider(self.settings.ai, {"GEMINI_API_KEY": "g-secret"})

    def tearDown(self):
        self._repo.__exit__(None, None, None)

    def test_auto_detects_gemini_and_builds_native_request(self):
        self.assertEqual((self.provider.name, self.provider.model), ("gemini", "gemini-3.8-flash"))
        body = {"candidates": [{"content": {"parts": [
            {"text": "thinking...", "thought": True}, {"text": "{\"a\": 1}"},
        ]}, "finishReason": "STOP"}]}
        with mock.patch("urllib.request.urlopen", return_value=_Response(json.dumps(body).encode())) as urlopen:
            self.assertEqual(json.loads(self.provider.complete("sys", "user")), {"a": 1})
        request = urlopen.call_args[0][0]
        self.assertTrue(request.full_url.endswith("/v1beta/models/gemini-3.8-flash:generateContent"))
        self.assertNotIn("g-secret", request.full_url)
        self.assertEqual(request.get_header("X-goog-api-key"), "g-secret")
        sent = json.loads(request.data)
        self.assertEqual(sent["systemInstruction"]["parts"][0]["text"], "sys")
        self.assertEqual(sent["generationConfig"]["responseMimeType"], "application/json")

    def test_rate_limit_uses_retry_delay_from_body(self):
        limited = http_error(429, '{"error": {"details": [{"retryDelay": "37s"}]}}')
        ok = _Response(json.dumps({"candidates": [{"content": {"parts": [{"text": "{}"}]}}]}).encode())
        waits = []
        with mock.patch("urllib.request.urlopen", side_effect=[limited, ok]):
            ai.with_retries(lambda: self.provider.complete("s", "u"), 3, "test", sleep=waits.append)
        self.assertEqual(waits, [37.0])

    def test_truncation_and_bad_model_name(self):
        body = {"candidates": [{"content": {"parts": [{"text": "{"}]}, "finishReason": "MAX_TOKENS"}]}
        with mock.patch("urllib.request.urlopen", return_value=_Response(json.dumps(body).encode())):
            with self.assertRaisesRegex(AIError, "maxOutputTokens"):
                self.provider.complete("s", "u")
        settings = temp_settings(self.settings.repo_root, DSA_AI_MODEL="../evil")
        with self.assertRaises(ConfigError):
            ai.create_provider(settings.ai, {"GEMINI_API_KEY": "k"})


class JsonHandlingTests(unittest.TestCase):
    def test_extract_json_variants(self):
        for text in ('{"a": 1}', '```json\n{"a": 1}\n```', 'Here you go:\n{"a": 1}\nThanks'):
            self.assertEqual(ai.extract_json(text), {"a": 1})
        with self.assertRaises(ValueError):
            ai.extract_json("no json here")

    def test_complete_json_feeds_validation_errors_back(self):
        class Scripted(ai.Provider):
            name = "scripted"

            def __init__(self):
                super().__init__("m")
                self.prompts = []

            def complete(self, system, user):
                self.prompts.append(user)
                return '{"ok": false}' if len(self.prompts) == 1 else '{"ok": true}'

        def validate(payload):
            if not payload["ok"]:
                raise ValueError("ok must be true")
            return payload

        provider = Scripted()
        self.assertEqual(ai.complete_json(provider, "s", "u", validate, "t", 3, sleep=lambda s: None), {"ok": True})
        self.assertIn("ok must be true", provider.prompts[1])


if __name__ == "__main__":
    unittest.main()
