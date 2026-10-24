from collections import deque


class RecentCounter:
    """Counts recent calls within a 3000 ms sliding window."""

    def __init__(self) -> None:
        """Initialize the counter."""
        raise NotImplementedError

    def ping(self, t: int) -> int:
        """Record ping at time t and return count in [t - 3000, t]."""
        raise NotImplementedError
