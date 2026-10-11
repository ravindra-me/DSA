# Solution 4: Set Matrix Zeroes

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** 2D array state encoding and memory optimization

## Approach

To achieve $O(1)$ auxiliary space, we use the first row and first column of the matrix as state markers instead of allocating additional arrays. Since cell `(0, 0)` overlaps both the first row and first column, we track whether the first column needs to be zeroed out using a separate boolean variable `first_col_has_zero`.

## Thought Process

A naive approach uses an $O(m \times n)$ extra copy of the matrix or $O(m + n)$ arrays to track which rows and columns should be zeroed. However, we can re-use the matrix itself to store this information.

If cell `matrix[r][c] == 0`, we set `matrix[r][0] = 0` and `matrix[0][c] = 0`. Before overwriting the first row and column as flags, we check if they originally contained any zeroes. For row 0, cell `matrix[0][0]` can store its status, while a separate boolean variable `first_col_has_zero` stores whether column 0 should be zeroed. After marking, we iterate through the inner matrix `(1..m-1, 1..n-1)` and update cells based on `matrix[r][0]` and `matrix[0][c]`. Finally, we update the first row and column based on our saved state.

## Algorithm

1. Check if the first column contains any zero and store the result in `first_col_has_zero`.
2. Iterate over all cells `(r, c)`. If `matrix[r][c] == 0`, mark `matrix[r][0] = 0` and `matrix[0][c] = 0`.
3. Iterate over the submatrix from row 1 to $m-1$ and column 1 to $n-1$. If `matrix[r][0] == 0` or `matrix[0][c] == 0`, set `matrix[r][c] = 0`.
4. If `matrix[0][0] == 0`, set all elements in the first row `matrix[0][c]` to 0.
5. If `first_col_has_zero` is True, set all elements in the first column `matrix[r][0]` to 0.

## Complexity Analysis

- **Time:** $\mathcal{O}(m \times n)$: We iterate over the matrix of size $m \times n$ a constant number of times.
- **Space:** $\mathcal{O}(1)$: In-place modification using only a single boolean flag for space optimization.

## Edge Cases

- Single cell matrix (`1x1`): Handled correctly as loops iterate safely and flags preserve state.
- Matrices with 1 row or 1 column: Handled seamlessly by the first row/column zeroing logic.
- Matrix already full of zeroes or containing no zeroes: Flags accurately capture state without unnecessary modifications.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def set_zeroes(matrix: list[list[int]]) -> None:
    """Modify matrix in-place so that if an element is 0, its row and col are set to 0."""
    if not matrix or not matrix[0]:
        return

    rows, cols = len(matrix), len(matrix[0])
    first_col_has_zero = False

    for r in range(rows):
        if matrix[r][0] == 0:
            first_col_has_zero = True
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for c in range(cols):
            matrix[0][c] = 0

    if first_col_has_zero:
        for r in range(rows):
            matrix[r][0] = 0
```
