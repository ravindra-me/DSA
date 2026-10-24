from collections import deque


class RecentCounter:
    """Counts recent calls within a 3000 ms sliding window."""

    WINDOW_SIZE: int = 3000

    def __init__(self) -> None:
        """Initialize the counter with an empty window of requests."""
        self._requests: deque[int] = deque()

    def ping(self, t: int) -> int:
        """Record ping at time t and return count in [t - 3000, t]."""
        self._requests.append(t)
        min_time = t - self.WINDOW_SIZE
        while self._requests and self._requests[0] < min_time:
            self._requests.popleft()
        return len(self._requests)
