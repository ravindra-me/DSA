class StockSpanner:
    """Calculates stock span for consecutive streaming prices."""

    def __init__(self) -> None:
        # Stack stores tuples of (price, span)
        self._stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        span = 1
        while self._stack and self._stack[-1][0] <= price:
            span += self._stack.pop()[1]
        self._stack.append((price, span))
        return span
