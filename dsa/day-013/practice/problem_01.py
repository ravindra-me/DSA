class CircularQueue:
    def __init__(self, k: int) -> None:
        """Initialize the queue with capacity k."""
        raise NotImplementedError

    def enqueue(self, value: int) -> bool:
        """Insert value. Return True if successful, False if full."""
        raise NotImplementedError

    def dequeue(self) -> bool:
        """Delete front value. Return True if successful, False if empty."""
        raise NotImplementedError

    def front(self) -> int:
        """Return front value, or -1 if empty."""
        raise NotImplementedError

    def rear(self) -> int:
        """Return rear value, or -1 if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Check whether queue is empty."""
        raise NotImplementedError

    def is_full(self) -> bool:
        """Check whether queue is full."""
        raise NotImplementedError
