# Solution 3: Diagonal Matrix Traverse

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium/Hard | **Concept:** 2d-matrix-manipulation

## Approach

Elements lying along the same anti-diagonal share an identical sum of row and column indices: $r + c = d$. Across the $M \times N$ grid, $d$ ranges from $0$ to $M + N - 2$. For each diagonal $d$, collect elements or traverse them directly, reversing the traversal order every alternating step (moving up-right when $d$ is even, and down-left when $d$ is odd).

## Thought Process

A brute-force or simulation approach might track a current position $(r, c)$ and direction $\Delta r, \Delta c \in \{(-1, 1), (1, -1)\}$, bouncing off edges when boundary conditions are violated. While $O(M \times N)$, boundary condition edge cases can be error-prone to implement.

Instead, observe that all coordinates $(r, c)$ on the same diagonal satisfy $r + c = d$ for some diagonal index $d \in [0, M + N - 2]$. For an up-right sweep (even $d$), we move from larger row indices to smaller row indices (bottom-left to top-right). For a down-left sweep (odd $d$), we move from smaller row indices to larger row indices.

For a given sum $d$, what are the valid row indices $r$? Since $c = d - r$ and $0 \le c < N$, we must have $d - (N - 1) \le r \le d$. Also, $0 \le r < M$. Combining these bounds, the valid row index range is $r \in [\max(0, d - N + 1), \min(M - 1, d)]$. Iterating directly over this range allows deterministic, clean $O(1)$ transitions per element without allocating auxiliary buckets.

## Algorithm

1. Check if the input matrix is empty or has empty rows; if so, return an empty list.
2. Let $M$ be the number of rows and $N$ be the number of columns.
3. Initialize an empty list `result` to store the elements.
4. Iterate through diagonal sum $d$ from $0$ to $M + N - 2$.
5. Calculate the starting and ending row indices for diagonal $d$: $r_{\min} = \max(0, d - N + 1)$ and $r_{\max} = \min(M - 1, d)$.
6. If $d$ is even (upward/rightward traversal), iterate $r$ from $r_{\max}$ down to $r_{\min}$ with step $-1$, appending `mat[r][d - r]` to `result`.
7. If $d$ is odd (downward/leftward traversal), iterate $r$ from $r_{\min}$ up to $r_{\max}$ with step $1$, appending `mat[r][d - r]` to `result`.
8. Return `result`.

## Complexity Analysis

- **Time:** O(M * N) because every element in the matrix is visited exactly once.
- **Space:** O(1) auxiliary space beyond the output array.

## Edge Cases

- Empty matrix or empty rows: gracefully returns `[]`.
- Single element matrix `[[x]]`: single loop iteration $d=0$ produces `[x]`.
- Single row matrix `1 x N`: correctly alternates across individual columns.
- Single column matrix `M x 1`: correctly steps downward along single-element diagonals.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def find_diagonal_order(mat: list[list[int]]) -> list[int]:
    """Returns elements of the 2D matrix ordered by alternating diagonal sweeps."""
    if not mat or not mat[0]:
        return []

    m, n = len(mat), len(mat[0])
    result = []

    for d in range(m + n - 1):
        r_min = max(0, d - n + 1)
        r_max = min(m - 1, d)

        if d % 2 == 0:
            for r in range(r_max, r_min - 1, -1):
                result.append(mat[r][d - r])
        else:
            for r in range(r_min, r_max + 1):
                result.append(mat[r][d - r])

    return result
```
