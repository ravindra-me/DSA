class MinStack:
    def __init__(self) -> None:
        """Initialize the stack and auxiliary minimum tracking stack."""
        self._stack: list[int] = []
        self._min_stack: list[int] = []

    def push(self, val: int) -> None:
        """Push element val onto stack and record current minimum."""
        self._stack.append(val)
        if not self._min_stack or val < self._min_stack[-1]:
            self._min_stack.append(val)
        else:
            self._min_stack.append(self._min_stack[-1])

    def pop(self) -> None:
        """Remove the top element from both stacks."""
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        """Return the top element of the primary stack."""
        return self._stack[-1]

    def get_min(self) -> int:
        """Retrieve the minimum element in constant time."""
        return self._min_stack[-1]
