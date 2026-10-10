class AmortizedQueue:
    """FIFO queue implemented using two LIFO stacks with amortized O(1) operations."""

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, x: int) -> None:
        """Push element x to the back of the queue."""
        raise NotImplementedError

    def pop(self) -> int:
        """Remove and return the element at the front of the queue."""
        raise NotImplementedError

    def peek(self) -> int:
        """Return the element at the front of the queue without removing it."""
        raise NotImplementedError

    def empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        raise NotImplementedError
