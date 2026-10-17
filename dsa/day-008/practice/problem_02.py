class ResettableCounters:
    """A fixed-size array of counters with O(1) increment, get, and set_all operations."""

    def __init__(self, size: int) -> None:
        """Initialize size counters with 0."""
        raise NotImplementedError

    def increment(self, i: int) -> None:
        """Add 1 to counter i in O(1) worst-case time."""
        raise NotImplementedError

    def set_all(self, val: int) -> None:
        """Set all counters to val in O(1) worst-case time."""
        raise NotImplementedError

    def get(self, i: int) -> int:
        """Return the value of counter i in O(1) worst-case time."""
        raise NotImplementedError
