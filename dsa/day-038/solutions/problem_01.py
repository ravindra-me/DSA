from collections import deque


class StreamFirstUnique:
    def __init__(self) -> None:
        """Initialize the stream data structure."""
        self._counts: dict[str, int] = {}
        self._queue: deque[str] = deque()

    def add(self, ch: str) -> None:
        """Add character ch to the stream."""
        new_count = self._counts.get(ch, 0) + 1
        self._counts[ch] = new_count
        if new_count == 1:
            self._queue.append(ch)

    def get_first_unique(self) -> str:
        """Return the first unique character in the stream, or empty string."""
        while self._queue and self._counts[self._queue[0]] > 1:
            self._queue.popleft()
        return self._queue[0] if self._queue else ""
