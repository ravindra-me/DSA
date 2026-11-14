def is_valid_max_heap(nums: list[int]) -> bool:
    """Return True if nums represents a valid max-heap."""
    n = len(nums)
    for j in range(1, n):
        parent = (j - 1) // 2
        if nums[j] > nums[parent]:
            return False
    return True
