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
