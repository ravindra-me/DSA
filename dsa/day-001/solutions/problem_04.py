def find_peak_element(nums: list[int]) -> int:
    """Find the index of any peak element in strictly O(log n) time."""
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
