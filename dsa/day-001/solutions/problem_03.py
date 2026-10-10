class AmortizedQueue:
    """FIFO queue implemented using two LIFO stacks with amortized O(1) operations."""

    def __init__(self) -> None:
        self._in_stack: list[int] = []
        self._out_stack: list[int] = []

    def _shift(self) -> None:
        """Transfer elements from in_stack to out_stack if out_stack is empty."""
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())

    def push(self, x: int) -> None:
        """Push element x to the back of the queue."""
        self._in_stack.append(x)

    def pop(self) -> int:
        """Remove and return the element at the front of the queue."""
        self._shift()
        return self._out_stack.pop()

    def peek(self) -> int:
        """Return the element at the front of the queue without removing it."""
        self._shift()
        return self._out_stack[-1]

    def empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        return not self._in_stack and not self._out_stack
