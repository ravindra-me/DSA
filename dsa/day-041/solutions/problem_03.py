class TwoStackDeque:
    def __init__(self) -> None:
        """Initialize empty deque backed by two stacks."""
        self._front: list[int] = []
        self._back: list[int] = []

    def push_front(self, val: int) -> None:
        self._front.append(val)

    def push_back(self, val: int) -> None:
        self._back.append(val)

    def _rebalance(self) -> None:
        if not self._front and not self._back:
            return

        source = self._front if self._front else self._back
        from_front = bool(self._front)
        n = len(source)
        half = n // 2

        temp: list[int] = []
        while source:
            temp.append(source.pop())

        # temp now has elements popped from source.
        # If source was front: temp[0] was front top (first deque element),
        # temp[-1] was front bottom (middle of deque).
        # If source was back: temp[0] was back top (last deque element),
        # temp[-1] was back bottom (middle of deque).
        if from_front:
            # Elements that stay in front should end up with temp[0] at top of front.
            # Elements going to back should have temp[-1] near back bottom.
            # The back part corresponds to temp[half:], which must be pushed to back.
            for i in range(half, n):
                self._back.append(temp[i])
            for i in range(half - 1, -1, -1):
                self._front.append(temp[i])
        else:
            # Elements that stay in back should end up with temp[0] at top of back.
            # Elements going to front should have temp[-1] near front bottom.
            for i in range(half, n):
                self._front.append(temp[i])
            for i in range(half - 1, -1, -1):
                self._back.append(temp[i])

    def pop_front(self) -> int | None:
        if not self._front:
            self._rebalance()
        if not self._front:
            return None
        return self._front.pop()

    def pop_back(self) -> int | None:
        if not self._back:
            self._rebalance()
        if not self._back:
            return None
        return self._back.pop()

    def peek_front(self) -> int | None:
        if not self._front:
            self._rebalance()
        if not self._front:
            return None
        return self._front[-1]

    def peek_back(self) -> int | None:
        if not self._back:
            self._rebalance()
        if not self._back:
            return None
        return self._back[-1]

    def __len__(self) -> int:
        return len(self._front) + len(self._back)
