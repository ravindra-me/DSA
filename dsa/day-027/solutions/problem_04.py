def find_peak_element(nums: list[int]) -> int:
    """Finds a peak element in an array where nums[i] != nums[i+1]."""
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            # We are on an upward slope; peak must be to the right
            left = mid + 1
        else:
            # We are on a downward slope; mid could be the peak
            right = mid
            
    return left
