def maximal_rectangle(matrix: list[list[str]]) -> int:
    """Calculates the area of the largest rectangle containing only '1's in a binary grid."""
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for c in range(cols):
            if row[c] == '1':
                heights[c] += 1
            else:
                heights[c] = 0

        stack = []
        for i in range(cols + 1):
            current_height = heights[i] if i < cols else 0
            while stack and current_height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

    return max_area
