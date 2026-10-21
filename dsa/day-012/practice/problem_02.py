class StockSpanner:
    """Calculates stock span for consecutive streaming prices."""

    def __init__(self) -> None:
        raise NotImplementedError

    def next(self, price: int) -> int:
        raise NotImplementedError
