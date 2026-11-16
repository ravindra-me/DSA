class OverwriteBuffer:
    def __init__(self, capacity: int) -> None:
        """Initialize the overwrite ring buffer with a fixed capacity."""
        raise NotImplementedError

    def push(self, val: int) -> None:
        """Push val, overwriting the oldest item if full."""
        raise NotImplementedError

    def pop_oldest(self) -> int:
        """Pop and return the oldest item, or -1 if empty."""
        raise NotImplementedError

    def get_last_k(self, m: int) -> list[int]:
        """Return up to m newest elements in chronological order."""
        raise NotImplementedError
