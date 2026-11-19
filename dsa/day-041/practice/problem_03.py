class TwoStackDeque:
    def __init__(self) -> None:
        """Initialize empty deque backed by two stacks."""
        raise NotImplementedError

    def push_front(self, val: int) -> None:
        raise NotImplementedError

    def push_back(self, val: int) -> None:
        raise NotImplementedError

    def pop_front(self) -> int | None:
        raise NotImplementedError

    def pop_back(self) -> int | None:
        raise NotImplementedError

    def peek_front(self) -> int | None:
        raise NotImplementedError

    def peek_back(self) -> int | None:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
