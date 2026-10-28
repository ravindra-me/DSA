def majority_element(nums: list[int]) -> int:
    """Find and return the majority element (> n // 2 times)."""
    candidate = 0
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate
