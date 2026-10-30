# Solution 4: 2D Matrix Block Sum Queries

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** 2D Prefix Sum (Integral Image)

## Approach

Precompute a 2D prefix sum (integral image) matrix of size $(m+1) \times (n+1)$ where `pref[r+1][c+1]` represents the sum of all elements in the subgrid from $(0, 0)$ to $(r, c)$. Any rectangular range sum from $(r_1, c_1)$ to $(r_2, c_2)$ can then be answered in $O(1)$ time using the principle of inclusion-exclusion: `pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]`.

## Thought Process

A naive approach calculates the sum for each query by iterating through all cells inside the query bounds $[r_1..r_2] \times [c_1..c_2]$. In the worst case, each query takes $O(m \times n)$ time. With up to $10^4$ queries on a $200 \times 200$ matrix, this requires up to $4 \times 10^8$ operations, which is too slow.

To achieve $O(1)$ query time, we generalize the 1D prefix sum concept to 2D. Let `pref[i][j]` be the sum of the subgrid spanning rows $0$ to $i-1$ and columns $0$ to $j-1$. When constructing `pref`, each cell `(i, j)` can be computed from previously computed values:
`pref[i][j] = matrix[i-1][j-1] + pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1]`.
Here, `pref[i-1][j-1]` is added twice (once in `pref[i-1][j]` and once in `pref[i][j-1]`), so we subtract it once.

For a query defined by corners $(r_1, c_1)$ to $(r_2, c_2)$:
1. Take the full rectangle from $(0, 0)$ to $(r_2, c_2)$, which is `pref[r2 + 1][c2 + 1]`.
2. Subtract the area above the rectangle: `pref[r1][c2 + 1]`.
3. Subtract the area to the left of the rectangle: `pref[r2 + 1][c1]`.
4. Add back the doubly-subtracted top-left area: `pref[r1][c1]`.

Using 1-based indexing for the prefix table avoids special bounds checking when $r_1 = 0$ or $c_1 = 0$.

## Algorithm

1. In `__init__`, record dimensions $m = \text{len}(matrix)$ and $n = \text{len}(matrix[0])$.
2. Allocate a 2D array `pref` of size $(m + 1) \times (n + 1)$ filled with zeros.
3. Populate `pref` using nested loops over $r \in [0, m-1]$ and $c \in [0, n-1]$: `pref[r+1][c+1] = matrix[r][c] + pref[r][c+1] + pref[r+1][c] - pref[r][c]`.
4. In `sum_region(row1, col1, row2, col2)`, apply inclusion-exclusion using 1-based bounds: return `pref[row2 + 1][col2 + 1] - pref[row1][col2 + 1] - pref[row2 + 1][col1] + pref[row1][col1]`.

## Complexity Analysis

- **Time:** Initialization: $O(m \times n)$ to compute the 2D prefix sum table. Query: $O(1)$ per `sum_region` call using 4 table lookups and 3 arithmetic operations.
- **Space:** $O(m \times n)$ auxiliary space to store the $(m + 1) \times (n + 1)$ prefix sum matrix.

## Edge Cases

- Single cell matrix (1x1): Handled seamlessly because size is $(2 \times 2)$ in prefix table and bounds 0 to 0 work correctly.
- Single row or single column matrix: Correctly computes horizontal or vertical 1D prefix sums without extra conditions.
- Whole matrix query (row1=0, col1=0, row2=m-1, col2=n-1): Works cleanly due to zero-padding in row 0 and column 0.
- Negative numbers and zeros: Additions and subtractions correctly handle negative sums and zero cancellations.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
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
```
