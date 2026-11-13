# Problem 4: Maximal Rectangle of Ones in Binary Grid

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | 2D Grid reduction to Monotonic Stack Histogram | [Day 35: Monotonic Stack](../README.md) |

## Problem Statement

Given a 2D binary matrix `matrix` filled with `'0'`s and `'1'`s, find the largest rectangle containing only `'1'`s and return its area.

## Input

matrix: list[list[str]]

## Output

int

## Constraints

- 1 <= R, C <= 200 where R = matrix.length and C = matrix[0].length
- matrix[i][j] is '0' or '1'.

## Examples

**Example 1**

```text
Input:  matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
```

The maximal rectangle of '1's has an area of 6 (located at rows 1..2, cols 2..4).

**Example 2**

```text
Input:  matrix = [["0"]]
Output: 0
```

No '1's exist in the matrix.

## Function Signature

```python
def maximal_rectangle(matrix: list[list[str]]) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a 1D array of column heights updated row by row. For each row, run the standard Monotonic Stack Largest Rectangle in Histogram algorithm in $O(C)$ time.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
