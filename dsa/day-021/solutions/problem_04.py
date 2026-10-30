class NumMatrix:
    """2D range sum query data structure using a 2D prefix sum table."""

    def __init__(self, matrix: list[list[int]]) -> None:
        """Precomputes 2D prefix sums for O(1) rectangular range sum queries."""
        if not matrix or not matrix[0]:
            self._pref: list[list[int]] = [[]]
            return

        m = len(matrix)
        n = len(matrix[0])
        self._pref = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                self._pref[r + 1][c + 1] = (
                    matrix[r][c]
                    + self._pref[r][c + 1]
                    + self._pref[r + 1][c]
                    - self._pref[r][c]
                )

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Calculates sum of elements in submatrix [row1..row2] x [col1..col2]."""
        return (
            self._pref[row2 + 1][col2 + 1]
            - self._pref[row1][col2 + 1]
            - self._pref[row2 + 1][col1]
            + self._pref[row1][col1]
        )
