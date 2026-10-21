def largest_rectangle_area(heights: list[int]) -> int:
    """Find the area of the largest rectangle in a histogram."""
    stack: list[int] = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        current_height = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > current_height:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)

    return max_area
