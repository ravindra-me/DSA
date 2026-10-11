# Problem 4: Set Matrix Zeroes

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | 2D array state encoding and memory optimization | [Day 2: Arrays](../README.md) |

## Problem Statement

Given an $m \times n$ integer matrix, if an element is `0`, set its entire row and column to `0`'s.

You must do it **in-place**. You cannot allocate another matrix, nor should you use $O(m + n)$ auxiliary memory if you can optimize it to $O(1)$ extra memory.

## Input

`matrix: list[list[int]]`

## Output

`None`: modifies `matrix` in place

## Constraints

- m == len(matrix)
- n == len(matrix[0])
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

## Examples

**Example 1**

```text
Input:  matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
```

Row 1 and Column 1 are set to 0.

**Example 2**

```text
Input:  matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
```

The 0s at (0,0) and (0,3) trigger zeroing of row 0 and columns 0 and 3.

**Example 3**

```text
Input:  matrix = [[1]]
Output: [[1]]
```

Single cell with non-zero remains unchanged.

## Function Signature

```python
def set_zeroes(matrix: list[list[int]]) -> None:
    """Modify matrix in-place so that if an element is 0, its row and col are set to 0."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use the first row and first column of the matrix itself as markers to record which rows and cols must be zeroed, using a single extra variable for the first column's state.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
