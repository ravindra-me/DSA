def next_greater_elements(nums: list[int]) -> list[int]:
    """Find the next greater circular element for each position."""
    n = len(nums)
    result = [-1] * n
    stack: list[int] = []

    for i in range(2 * n):
        val = nums[i % n]
        while stack and nums[stack[-1]] < val:
            prev_index = stack.pop()
            result[prev_index] = val
        if i < n:
            stack.append(i)

    return result
