def sentinel_search(nums: list[int], target: int) -> bool:
    """Perform linear search using the sentinel technique to eliminate bound checks."""
    if not nums:
        return False
    
    last_idx = len(nums)
    nums.append(target)
    
    i = 0
    while nums[i] != target:
        i += 1
    
    nums.pop()
    return i < last_idx
