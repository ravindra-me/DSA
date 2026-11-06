# Problem 5: Search a 2D Matrix II

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | matrix-binary-search | [Day 28: Binary Search Variations](../README.md) |

## Problem Statement

Write an efficient algorithm that searches for a `target` value in an `m x n` integer matrix `matrix`. This matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

## Input

A 2D list of integers `matrix` and an integer `target`.

## Output

A boolean: `True` if `target` exists in `matrix`, `False` otherwise.

## Constraints

- m == len(matrix)
- n == len(matrix[i])
- 1 <= m, n <= 300
- -10^9 <= matrix[i][j] <= 10^9
- -10^9 <= target <= 10^9

## Examples

**Example 1**

```text
Input:  matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
```

Target 5 exists at row 1, column 1.

**Example 2**

```text
Input:  matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
```

Target 20 is not present in the matrix.

**Example 3**

```text
Input:  matrix = [[-5]], target = -5
Output: true
```

Single cell matrix matching target.

## Function Signature

```python
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Return True if target exists in matrix, else False."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Start at the top-right corner `(0, n-1)` (or bottom-left corner). Compare current cell with `target`. If equal, return `True`. If current cell is larger than `target`, move left. If smaller, move down. This eliminates a row or column each step in $O(m + n)$ time.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
