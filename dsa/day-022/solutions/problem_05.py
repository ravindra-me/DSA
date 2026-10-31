def max_area(height: list[int]) -> int:
    """Compute the maximum water volume a container can hold."""
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        h_left = height[left]
        h_right = height[right]
        width = right - left

        if h_left < h_right:
            area = h_left * width
            left += 1
        else:
            area = h_right * width
            right -= 1

        if area > max_water:
            max_water = area

    return max_water
