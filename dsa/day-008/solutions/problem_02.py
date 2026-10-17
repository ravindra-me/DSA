class ResettableCounters:
    """A fixed-size array of counters with O(1) increment, get, and set_all operations."""

    def __init__(self, size: int) -> None:
        """Initialize size counters with 0."""
        self._size: int = size
        self._values: list[int] = [0] * size
        self._update_time: list[int] = [0] * size
        self._current_time: int = 0
        self._set_all_val: int = 0
        self._set_all_time: int = 0

    def increment(self, i: int) -> None:
        """Add 1 to counter i in O(1) worst-case time."""
        self._current_time += 1
        if self._update_time[i] < self._set_all_time:
            self._values[i] = self._set_all_val + 1
        else:
            self._values[i] += 1
        self._update_time[i] = self._current_time

    def set_all(self, val: int) -> None:
        """Set all counters to val in O(1) worst-case time."""
        self._current_time += 1
        self._set_all_val = val
        self._set_all_time = self._current_time

    def get(self, i: int) -> int:
        """Return the value of counter i in O(1) worst-case time."""
        if self._update_time[i] < self._set_all_time:
            return self._set_all_val
        return self._values[i]
