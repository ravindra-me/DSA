# Problem 5: Shortest Path in Grid with Obstacle Elimination Budget

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Multi-dimensional state exploration using FIFO BFS queue | [Day 38: Queue](../README.md) |

## Problem Statement

You are given an `m x n` grid where each cell is either `0` (empty) or `1` (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

You have an obstacle elimination budget `k`, meaning you can walk into and eliminate at most `k` obstacle cells along your path.

Return the minimum number of steps to walk from the upper left corner `(0, 0)` to the lower right corner `(m - 1, n - 1)`. If no such path exists, return `-1`.

Note that you may also eliminate an obstacle at `(0, 0)` or `(m - 1, n - 1)` if one exists there, counting towards your budget `k`.

## Input

A 2D list of integers `grid: list[list[int]]` of dimensions `m x n`, and an integer `k`.

## Output

An integer representing the minimum number of steps, or `-1`.

## Constraints

- m == len(grid)
- n == len(grid[0])
- 1 <= m, n <= 40
- 0 <= k <= m * n
- grid[i][j] is either 0 or 1.

## Examples

**Example 1**

```text
Input:  grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
```

One path with 1 elimination is (0,0)->(0,1)->(0,2)->(1,2)->(2,2)->(3,2: elim)->(4,2), taking 6 steps.

**Example 2**

```text
Input:  grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
```

We need to eliminate at least 2 obstacles to reach the destination, but k = 1.

## Function Signature

```python
def shortest_path_elimination(grid: list[list[int]], k: int) -> int:
    """Calculates shortest path with up to k obstacle eliminations using BFS."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a BFS queue tracking tuples of (row, col, remaining_k, steps). Prune states using a 2D array storing the maximum remaining eliminations seen for each cell.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
