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
