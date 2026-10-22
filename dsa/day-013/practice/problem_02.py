class StackQueue:
    def __init__(self) -> None:
        """Initialize data structures."""
        raise NotImplementedError

    def push(self, x: int) -> None:
        """Push element x to the back of the queue."""
        raise NotImplementedError

    def pop(self) -> int:
        """Remove and return the element from front of queue."""
        raise NotImplementedError

    def peek(self) -> int:
        """Get the front element."""
        raise NotImplementedError

    def empty(self) -> bool:
        """Return whether the queue is empty."""
        raise NotImplementedError
