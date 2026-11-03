# Problem 3: First Local Minima in Matrix

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Linear scan over 2D grid with conditional early exit | [Day 25: Linear Search](../README.md) |

## Problem Statement

Given an $m \times n$ grid of integers `matrix`, find the row and column coordinates `(r, c)` of the **first** element that is strictly smaller than all of its existing orthogonal neighbors (up, down, left, right). Scan row by row from top to bottom, and left to right within each row. Return `[r, c]`. If no local minimum exists, return `[-1, -1]`.

## Input

A 2D list of integers `matrix`.

## Output

A list of two integers `[r, c]`.

## Constraints

- 1 <= m, n <= 500
- -10^9 <= matrix[r][c] <= 10^9

## Examples

**Example 1**

```text
Input:  matrix = [[9, 8, 7], [6, 2, 5], [4, 3, 1]]
Output: [1, 1]
```

matrix[1][1] = 2 is strictly smaller than 8, 6, 5, 3.

**Example 2**

```text
Input:  matrix = [[5, 5], [5, 5]]
Output: [-1, -1]
```

No element is strictly smaller than its neighbors.

## Function Signature

```python
def find_first_local_minimum(matrix: list[list[int]]) -> list[int]:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Perform a row-major 2D linear scan, checking boundary valid neighbors for each cell, early exiting on the first valid cell. Target complexity: O(m * n) time, O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
