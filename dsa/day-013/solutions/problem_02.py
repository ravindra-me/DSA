class StackQueue:
    """FIFO queue implemented using two LIFO stacks."""

    def __init__(self) -> None:
        """Initialize data structures."""
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []

    def push(self, x: int) -> None:
        """Push element x to the back of the queue."""
        self.in_stack.append(x)

    def _shift_stacks(self) -> None:
        """Move elements from in_stack to out_stack if out_stack is empty."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        """Remove and return the element from front of queue."""
        self._shift_stacks()
        return self.out_stack.pop()

    def peek(self) -> int:
        """Get the front element."""
        self._shift_stacks()
        return self.out_stack[-1]

    def empty(self) -> bool:
        """Return whether the queue is empty."""
        return not self.in_stack and not self.out_stack
