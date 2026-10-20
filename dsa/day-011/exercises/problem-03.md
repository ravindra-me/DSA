# Problem 3: Diagonal Matrix Traverse

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | 2d-matrix-manipulation | [Day 11: Arrays](../README.md) |

## Problem Statement

Given an $M \times N$ matrix `mat`, return an array of all the elements of the array in a diagonal order.

The traversal proceeds along diagonals running from bottom-left to top-right and top-right to bottom-left alternately. The first diagonal starts at `(0, 0)` moving upward/rightward.

## Input

A list of lists of integers `mat` representing an $M \times N$ matrix.

## Output

A list of integers representing the diagonal traversal order.

## Constraints

- 1 <= mat.length <= 10^4
- 1 <= mat[i].length <= 10^4
- 1 <= mat.length * mat[i].length <= 10^5
- -10^5 <= mat[i][j] <= 10^5

## Examples

**Example 1**

```text
Input:  mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [1, 2, 4, 7, 5, 3, 6, 8, 9]
```

Diagonals grouped by r + c: sum 0: [1]; sum 1: [2, 4] flipped to [2, 4]; sum 2: [7, 5, 3] etc.

**Example 2**

```text
Input:  mat = [[1, 2], [3, 4]]
Output: [1, 2, 3, 4]
```

Diagonal groups: [1], [2, 3], [4].

## Function Signature

```python
def find_diagonal_order(mat: list[list[int]]) -> list[int]:
    """Returns elements of the 2D matrix ordered by alternating diagonal sweeps."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Notice that elements on the same diagonal share the same sum of row and column indices (r + c). Group elements by this sum and alternate direction, or step coordinate pointers with directional bouncing.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
