def search_rotated(nums: list[int], target: int) -> int:
    """Return the index of target in rotated sorted array nums, or -1 if not found."""
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Otherwise, the right half must be sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return -1
