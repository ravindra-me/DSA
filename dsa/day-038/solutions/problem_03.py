class OverwriteBuffer:
    def __init__(self, capacity: int) -> None:
        """Initialize the overwrite ring buffer with a fixed capacity."""
        self._capacity = capacity
        self._buffer: list[int] = [0] * capacity
        self._head = 0
        self._size = 0

    def push(self, val: int) -> None:
        """Push val, overwriting the oldest item if full."""
        if self._size == self._capacity:
            # Overwrite oldest element: write at current head and advance head
            self._buffer[self._head] = val
            self._head = (self._head + 1) % self._capacity
        else:
            idx = (self._head + self._size) % self._capacity
            self._buffer[idx] = val
            self._size += 1

    def pop_oldest(self) -> int:
        """Pop and return the oldest item, or -1 if empty."""
        if self._size == 0:
            return -1
        val = self._buffer[self._head]
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return val

    def get_last_k(self, m: int) -> list[int]:
        """Return up to m newest elements in chronological order."""
        count = min(m, self._size)
        start_offset = self._size - count
        result: list[int] = []
        for i in range(count):
            idx = (self._head + start_offset + i) % self._capacity
            result.append(self._buffer[idx])
        return result
