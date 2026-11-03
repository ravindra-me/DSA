def find_first_occurrence(nums: list[int], target: int) -> int:
    """Return the 0-based index of the first occurrence of target in nums, or -1 if absent."""
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1
