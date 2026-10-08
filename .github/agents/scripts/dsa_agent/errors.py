"""Exception hierarchy. Every error the agent raises on purpose is an AgentError,
so the CLI can print a clean message instead of a stack trace."""


class AgentError(Exception):
    """Base class for expected, user-facing failures."""


class ConfigError(AgentError):
    """Invalid configuration, roadmap, progress file or user input."""


class AIError(AgentError):
    """The AI provider failed or returned an unusable response."""


class AIRetryableError(AIError):
    """A transient AI/API failure (rate limit, 5xx, timeout) worth retrying."""


class ValidationFailed(AgentError):
    """Generated content failed validation and could not be repaired."""
