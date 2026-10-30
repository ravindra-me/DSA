# Problem 4: 2D Matrix Block Sum Queries

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | 2D Prefix Sum (Integral Image) | [Day 21: Prefix & Suffix Techniques](../README.md) |

## Problem Statement

Given an $m \times n$ integer matrix `matrix`, handle multiple queries of the following type:
- Calculate the sum of the elements of `matrix` inside the rectangle defined by its upper-left corner `(row1, col1)` and lower-right corner `(row2, col2)` inclusive.

Implement the `NumMatrix` class:
- `__init__(self, matrix: list[list[int]])`: Initializes the object with the integer matrix `matrix`.
- `sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int`: Returns the sum of elements inside the specified rectangle in $O(1)$ time.

## Input

`matrix`: 2D list of integers.
`row1`, `col1`, `row2`, `col2`: boundary indices representing the query rectangle.

## Output

`int`: The sum of the subgrid.

## Constraints

- m == len(matrix)
- n == len(matrix[0])
- 1 <= m, n <= 200
- -10^4 <= matrix[i][j] <= 10^4
- 0 <= row1 <= row2 < m
- 0 <= col1 <= col2 < n
- At most 10^4 calls will be made to sum_region.

## Examples

**Example 1**

```text
Input:  matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
queries: sum_region(2, 1, 4, 3), sum_region(1, 1, 2, 2)
Output: 8, 11
```

sum_region(2, 1, 4, 3) covers rows 2..4, cols 1..3 with sum (2+0+1 + 1+0+1 + 0+3+0) = 8.
sum_region(1, 1, 2, 2) covers rows 1..2, cols 1..2 with sum (6+3 + 2+0) = 11.

**Example 2**

```text
Input:  matrix = [[-5]]
queries: sum_region(0, 0, 0, 0)
Output: -5
```

Single cell matrix returns its single value.

## Function Signature

```python
class NumMatrix:
    def __init__(self, matrix: list[list[int]]) -> None:
        ...

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ...
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Precompute an (m+1) x (n+1) 2D prefix sum grid using inclusion-exclusion principle in O(m * n) time, then answer each query in O(1) arithmetic operations.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
