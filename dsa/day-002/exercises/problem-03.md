# Problem 3: Spiral Matrix Traversal

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | 2D array boundary simulation | [Day 2: Arrays](../README.md) |

## Problem Statement

Given an $m \times n$ matrix of integers, return all elements of the matrix in **spiral order** (starting from top-left, proceeding clockwise inward).

## Input

`matrix: list[list[int]]`

## Output

`list[int]`: elements in clockwise spiral order

## Constraints

- m == len(matrix)
- n == len(matrix[i])
- 1 <= m, n <= 100
- -100 <= matrix[i][j] <= 100

## Examples

**Example 1**

```text
Input:  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

Traverse top row [1,2,3], right col [6,9], bottom row [8,7], left col [4], then inner element [5].

**Example 2**

```text
Input:  matrix = [[1]]
Output: [1]
```

A 1x1 matrix contains only one element.

**Example 3**

```text
Input:  matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

Clockwise perimeter followed by inner segment.

## Function Signature

```python
def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Return all elements of matrix in spiral order."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain four boundary pointers (top, bottom, left, right) and shrink them inward after each directional pass in $O(m \times n)$ time and $O(1)$ extra space.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
