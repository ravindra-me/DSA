class CircularQueue:
    def __init__(self, k: int) -> None:
        """Initialize the queue with capacity k."""
        self._capacity: int = k
        self._buffer: list[int] = [0] * k
        self._head: int = 0
        self._size: int = 0

    def enqueue(self, value: int) -> bool:
        """Insert value. Return True if successful, False if full."""
        if self.is_full():
            return False
        tail_index = (self._head + self._size) % self._capacity
        self._buffer[tail_index] = value
        self._size += 1
        return True

    def dequeue(self) -> bool:
        """Delete front value. Return True if successful, False if empty."""
        if self.is_empty():
            return False
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return True

    def front(self) -> int:
        """Return front value, or -1 if empty."""
        if self.is_empty():
            return -1
        return self._buffer[self._head]

    def rear(self) -> int:
        """Return rear value, or -1 if empty."""
        if self.is_empty():
            return -1
        tail_index = (self._head + self._size - 1) % self._capacity
        return self._buffer[tail_index]

    def is_empty(self) -> bool:
        """Check whether queue is empty."""
        return self._size == 0

    def is_full(self) -> bool:
        """Check whether queue is full."""
        return self._size == self._capacity
