"""Loads .github/agents/config/agent.json and applies environment overrides.

Environment variables (all optional; empty values are ignored so unset GitHub
repository variables behave like "not configured"):

    DSA_LANGUAGE      lesson language (python | javascript)
    DSA_TIMEZONE      IANA timezone that defines "today" for idempotency
    DSA_AI_PROVIDER   auto | openai | anthropic | gemini
    DSA_AI_MODEL      model name for the selected provider
    DSA_AI_FALLBACK_MODELS  comma-separated fallback models ("none" disables)
    OPENAI_BASE_URL   OpenAI-compatible endpoint (Azure, OpenRouter, Groq, ...)
    DSA_SANDBOX       docker | process  (process = NO isolation, local dev only)
    DSA_REPO_ROOT     repository root (defaults to the checkout containing this file)
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping, Optional, Tuple

from .errors import ConfigError
from .fsutil import read_json

AGENTS_DIR = Path(__file__).resolve().parents[2]  # .github/agents
DEFAULT_REPO_ROOT = AGENTS_DIR.parents[1]

DIFFICULTY_LEVELS = ("progressive", "easy", "medium", "hard")
SANDBOX_MODES = ("docker", "process")
PROVIDERS = ("auto", "openai", "anthropic", "gemini")
THINKING_LEVELS = ("minimal", "low", "medium", "high")


@dataclass(frozen=True)
class RevisionSettings:
    enabled: bool
    intervals: Tuple[int, ...]
    min_new_lessons_between: int


@dataclass(frozen=True)
class AISettings:
    provider: str
    models: Mapping[str, str]
    base_urls: Mapping[str, str]
    model_override: Optional[str]
    fallback_models: Mapping[str, Tuple[str, ...]]
    fallback_override: Optional[Tuple[str, ...]]
    gemini_thinking_level: Optional[str]
    temperature: Optional[float]
    max_output_tokens: int
    timeout_seconds: int
    max_attempts: int


@dataclass(frozen=True)
class SandboxSettings:
    mode: str
    timeout_seconds: int
    memory: str
    cpus: str
    pids_limit: int


@dataclass(frozen=True)
class Settings:
    repo_root: Path
    agents_dir: Path
    lessons_dir: Path
    language: str
    timezone: str
    problems_per_day: int
    max_problems_per_day: int
    default_difficulty: str
    min_tests_per_problem: int
    max_repair_attempts: int
    revision: RevisionSettings
    ai: AISettings
    sandbox: SandboxSettings
    raw: Mapping[str, object] = field(repr=False, default_factory=dict)

    @property
    def progress_path(self) -> Path:
        return self.lessons_dir / "progress.json"

    @property
    def prompts_dir(self) -> Path:
        return self.agents_dir / "prompts"

    @property
    def roadmap_path(self) -> Path:
        return self.agents_dir / "roadmap" / "roadmap.json"


def _env(env: Mapping[str, str], name: str) -> Optional[str]:
    value = env.get(name, "").strip()
    return value or None


def _int(data: Mapping[str, object], key: str, lo: int, hi: int) -> int:
    value = data.get(key)
    if not isinstance(value, int) or isinstance(value, bool) or not lo <= value <= hi:
        raise ConfigError(f"config '{key}' must be an integer in [{lo}, {hi}], got {value!r}")
    return value


def load_settings(
    repo_root: Optional[Path] = None,
    env: Optional[Mapping[str, str]] = None,
    agents_dir: Path = AGENTS_DIR,
) -> Settings:
    env = os.environ if env is None else env
    config_path = agents_dir / "config" / "agent.json"
    try:
        data = read_json(config_path)
    except (OSError, ValueError) as exc:
        raise ConfigError(f"cannot read {config_path}: {exc}") from exc

    root = Path(repo_root or _env(env, "DSA_REPO_ROOT") or DEFAULT_REPO_ROOT).resolve()

    lessons_dir_name = str(data.get("lessonsDir", "dsa"))
    if not lessons_dir_name or Path(lessons_dir_name).is_absolute() or ".." in Path(lessons_dir_name).parts:
        raise ConfigError("config 'lessonsDir' must be a relative path inside the repository")

    language = (_env(env, "DSA_LANGUAGE") or str(data.get("language", "python"))).lower()
    timezone = _env(env, "DSA_TIMEZONE") or str(data.get("timezone", "UTC"))
    _check_timezone(timezone)

    default_difficulty = str(data.get("defaultDifficulty", "progressive")).lower()
    if default_difficulty not in DIFFICULTY_LEVELS:
        raise ConfigError(f"config 'defaultDifficulty' must be one of {DIFFICULTY_LEVELS}")

    max_problems = _int(data, "maxProblemsPerDay", 1, 10)
    problems = _int(data, "problemsPerDay", 1, max_problems)

    rev = data.get("revision") or {}
    intervals = rev.get("intervalsInDays", [])
    if not isinstance(intervals, list) or not all(isinstance(i, int) and i > 0 for i in intervals):
        raise ConfigError("config 'revision.intervalsInDays' must be a list of positive integers")
    if intervals != sorted(set(intervals)):
        raise ConfigError("config 'revision.intervalsInDays' must be strictly increasing")
    revision = RevisionSettings(
        enabled=bool(rev.get("enabled", True)),
        intervals=tuple(intervals),
        min_new_lessons_between=_int(rev, "minNewLessonsBetweenRevisions", 0, 30),
    )

    ai_raw = data.get("ai") or {}
    provider = (_env(env, "DSA_AI_PROVIDER") or str(ai_raw.get("provider", "auto"))).lower()
    if provider not in PROVIDERS:
        raise ConfigError(f"AI provider must be one of {PROVIDERS}, got {provider!r}")
    base_urls = dict(ai_raw.get("baseUrls") or {})
    if _env(env, "OPENAI_BASE_URL"):
        base_urls["openai"] = _env(env, "OPENAI_BASE_URL")
    for name, url in base_urls.items():
        if not str(url).startswith("https://") and not str(url).startswith("http://localhost"):
            raise ConfigError(f"base URL for {name} must use https://")
    temperature = ai_raw.get("temperature")
    if temperature is not None and not isinstance(temperature, (int, float)):
        raise ConfigError("config 'ai.temperature' must be a number or null")
    fallbacks_raw = ai_raw.get("fallbackModels") or {}
    if not isinstance(fallbacks_raw, dict) or not all(
        isinstance(v, list) and all(isinstance(m, str) and m for m in v) for v in fallbacks_raw.values()
    ):
        raise ConfigError("config 'ai.fallbackModels' must map provider names to lists of model names")
    fallback_env = _env(env, "DSA_AI_FALLBACK_MODELS")
    fallback_override = None
    if fallback_env is not None:
        fallback_override = () if fallback_env.lower() == "none" else tuple(m.strip() for m in fallback_env.split(",") if m.strip())
    thinking = ai_raw.get("geminiThinkingLevel")
    if thinking is not None and thinking not in THINKING_LEVELS:
        raise ConfigError(f"config 'ai.geminiThinkingLevel' must be null or one of {THINKING_LEVELS}")
    ai = AISettings(
        provider=provider,
        models=dict(ai_raw.get("models") or {}),
        base_urls=base_urls,
        model_override=_env(env, "DSA_AI_MODEL"),
        fallback_models={k: tuple(v) for k, v in fallbacks_raw.items()},
        fallback_override=fallback_override,
        gemini_thinking_level=thinking,
        temperature=temperature,
        max_output_tokens=_int(ai_raw, "maxOutputTokens", 1000, 128000),
        timeout_seconds=_int(ai_raw, "requestTimeoutSeconds", 10, 1800),
        max_attempts=_int(ai_raw, "maxAttempts", 1, 10),
    )

    sb = data.get("sandbox") or {}
    mode = (_env(env, "DSA_SANDBOX") or str(sb.get("mode", "docker"))).lower()
    if mode not in SANDBOX_MODES:
        raise ConfigError(f"sandbox mode must be one of {SANDBOX_MODES}, got {mode!r}")
    sandbox = SandboxSettings(
        mode=mode,
        timeout_seconds=_int(sb, "timeoutSeconds", 5, 1800),
        memory=str(sb.get("memory", "512m")),
        cpus=str(sb.get("cpus", "1")),
        pids_limit=_int(sb, "pidsLimit", 16, 4096),
    )

    return Settings(
        repo_root=root,
        agents_dir=agents_dir,
        lessons_dir=root / lessons_dir_name,
        language=language,
        timezone=timezone,
        problems_per_day=problems,
        max_problems_per_day=max_problems,
        default_difficulty=default_difficulty,
        min_tests_per_problem=_int(data, "minTestsPerProblem", 1, 50),
        max_repair_attempts=_int(data, "maxRepairAttempts", 0, 10),
        revision=revision,
        ai=ai,
        sandbox=sandbox,
        raw=data,
    )


def _check_timezone(name: str) -> None:
    try:
        from zoneinfo import ZoneInfo

        ZoneInfo(name)
    except Exception as exc:  # ZoneInfoNotFoundError, ValueError
        raise ConfigError(f"unknown timezone {name!r}") from exc
