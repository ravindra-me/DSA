from collections import deque


class RecentCounter:
    """Counts the number of recent requests within a 3000 ms sliding window."""

    def __init__(self) -> None:
        """Initialize the counter with an empty timestamp queue."""
        self._requests: deque[int] = deque()

    def ping(self, t: int) -> int:
        """Record request at time t and return count in [t - 3000, t]."""
        self._requests.append(t)
        min_time = t - 3000
        while self._requests and self._requests[0] < min_time:
            self._requests.popleft()
        return len(self._requests)
