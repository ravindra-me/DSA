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
