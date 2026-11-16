# Solution 5: Shortest Path in Grid with Obstacle Elimination Budget

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Multi-dimensional state exploration using FIFO BFS queue

## Approach

We model the problem as finding the shortest path in an unweighted state graph using Breadth-First Search (BFS). Instead of tracking just cell coordinates `(r, c)`, each state in our queue includes the remaining obstacle elimination budget: `(r, c, remaining_k)`. We keep track of the maximum remaining elimination budget seen so far for each cell to avoid re-visiting states with fewer or equal remaining eliminations.

## Thought Process

A standard 2D grid BFS tracks visited cells `(r, c)` to find the shortest path. However, here a cell `(r, c)` can be visited multiple times with different remaining obstacle elimination budgets. A path arriving at `(r, c)` with more remaining eliminations `k'` is strictly superior to or as good as arriving with fewer eliminations `k'' <= k'`. Thus, the state space is expanded to `(r, c, k)`. If `k >= m + n - 2`, we can reach the destination directly in Manhattan distance `(m - 1) + (n - 1)` steps without worrying about obstacles, giving an immediate optimal shortcut.

## Algorithm

1. Check if grid is 1x1: return 0 immediately.
2. If k is greater than or equal to (m + n - 2), return (m + n - 2) directly as Manhattan distance path is optimal.
3. Initialize a deque `queue` with the initial state `(r=0, c=0, remaining_k=k - grid[0][0], steps=0)`.
4. Maintain a 2D array or hash map `max_k_at[r][c]` initialized to -1 to store the maximum remaining eliminations when visiting `(r, c)`.
5. While `queue` is not empty, pop the left element `(r, c, rem_k, steps)`.
6. If `(r, c)` is `(m - 1, n - 1)`, return `steps`.
7. For each of the four orthogonal neighbors `(nr, nc)` of `(r, c)`:
8. Compute `next_k = rem_k - grid[nr][nc]`.
9. If `next_k >= 0` and `next_k > max_k_at[nr][nc]`:
10. Set `max_k_at[nr][nc] = next_k`.
11. Append `(nr, nc, next_k, steps + 1)` to `queue`.
12. If queue becomes empty without reaching the target, return -1.

## Complexity Analysis

- **Time:** $O(m \cdot n \cdot \min(k, m + n))$: There are $O(m \cdot n \cdot \min(k, m + n))$ distinct states. Each state is processed once in constant time.
- **Space:** $O(m \cdot n \cdot \min(k, m + n))$: To store visited states and the BFS queue.

## Edge Cases

- Grid of size 1x1: Return 0 immediately.
- Grid start (0,0) or end (m-1, n-1) contains an obstacle: Grid[0][0] decreases the initial budget k.
- k is large enough to walk straight to target: Handled by Manhattan distance shortcut.
- No valid path exists even with k eliminations: BFS finishes and returns -1.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
from collections import deque

def shortest_path_elimination(grid: list[list[int]], k: int) -> int:
    """Calculates shortest path with up to k obstacle eliminations using BFS."""
    m, n = len(grid), len(grid[0])
    
    start_k = k - grid[0][0]
    if start_k < 0:
        return -1
    
    if m == 1 and n == 1:
        return 0
    
    # If budget is large enough to eliminate all cells along a Manhattan path
    if k >= m + n - 1:
        return m + n - 2
    
    # queue stores (r, c, remaining_k, steps)
    queue = deque([(0, 0, start_k, 0)])
    # max_k_at[r][c] tracks max remaining_k with which (r, c) was visited
    max_k_at = [[-1] * n for _ in range(m)]
    max_k_at[0][0] = start_k
    
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    while queue:
        r, c, rem_k, steps = queue.popleft()
        
        if r == m - 1 and c == n - 1:
            return steps
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                next_k = rem_k - grid[nr][nc]
                if next_k >= 0 and next_k > max_k_at[nr][nc]:
                    max_k_at[nr][nc] = next_k
                    queue.append((nr, nc, next_k, steps + 1))
                    
    return -1
```
