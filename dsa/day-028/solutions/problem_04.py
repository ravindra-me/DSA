def find_peak_element(nums: list[int]) -> int:
    """Return the 0-based index of any peak element in nums."""
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
