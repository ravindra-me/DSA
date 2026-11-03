# Solution 3: First Local Minima in Matrix

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Linear scan over 2D grid with conditional early exit

## Approach

Perform a row-by-row, column-by-column linear scan over the grid. For each cell `(r, c)`, check its existing orthogonal neighbors (up, down, left, right). The first cell that is strictly smaller than all existing neighbors is returned immediately.

## Thought Process

The problem asks for the *first* local minimum encountered in row-major order (top-to-bottom, left-to-right). Although a single local minimum in a 2D grid can be found faster using divide and conquer (e.g., $O(m \log n)$), finding the *first* one according to a specific scan order requires evaluating cells in that exact order until a valid candidate is found. Checking orthogonal neighbors for a given cell takes $O(1)$ time, yielding an overall worst-case linear scan of $O(m \times n)$ time and $O(1)$ extra space.

## Algorithm

1. Iterate through rows `r` from `0` to `m - 1`.
2. Iterate through columns `c` from `0` to `n - 1`.
3. For the current cell `matrix[r][c]`, check all orthogonal neighbors `(nr, nc)` that are within bounds: `(r-1, c)`, `(r+1, c)`, `(r, c-1)`, `(r, c+1)`.
4. If `matrix[r][c] < matrix[nr][nc]` for all valid neighbors, return `[r, c]` immediately.
5. If the loop finishes without finding any local minimum, return `[-1, -1]`.

## Complexity Analysis

- **Time:** $\mathcal{O}(m \times n)$ worst-case, as we may check every cell in the matrix once. Each cell neighbor check takes $\mathcal{O}(1)$ standard operations.
- **Space:** $\mathcal{O}(1)$ auxiliary space as no additional data structures are created.

## Edge Cases

- 1x1 Matrix: The single element has no neighbors, so it trivially satisfies the condition of being strictly smaller than all existing neighbors. Returns `[0, 0]`.
- Flat values / No local minima: e.g., all elements equal. Returns `[-1, -1]`.
- Local minimum at boundary: Correctly checks only valid orthogonal neighbors within grid limits.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def find_first_local_minimum(matrix: list[list[int]]) -> list[int]:
    """Find the row and col coordinates of the first local minimum in row-major order."""
    if not matrix or not matrix[0]:
        return [-1, -1]
    
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for r in range(rows):
        for c in range(cols):
            val = matrix[r][c]
            is_local_min = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if val >= matrix[nr][nc]:
                        is_local_min = False
                        break
            if is_local_min:
                return [r, c]
                
    return [-1, -1]
```
