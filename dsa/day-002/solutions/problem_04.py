def set_zeroes(matrix: list[list[int]]) -> None:
    """Modify matrix in-place so that if an element is 0, its row and col are set to 0."""
    if not matrix or not matrix[0]:
        return

    rows, cols = len(matrix), len(matrix[0])
    first_col_has_zero = False

    for r in range(rows):
        if matrix[r][0] == 0:
            first_col_has_zero = True
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for c in range(cols):
            matrix[0][c] = 0

    if first_col_has_zero:
        for r in range(rows):
            matrix[r][0] = 0
