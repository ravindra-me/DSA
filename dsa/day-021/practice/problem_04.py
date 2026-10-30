class NumMatrix:
    """2D range sum query data structure using a 2D prefix sum table."""

    def __init__(self, matrix: list[list[int]]) -> None:
        """Precomputes 2D prefix sums for O(1) rectangular range sum queries."""
        raise NotImplementedError

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Calculates sum of elements in submatrix [row1..row2] x [col1..col2]."""
        raise NotImplementedError
