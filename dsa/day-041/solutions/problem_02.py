def stable_zero_partition(nums: list[int]) -> int:
    """Partition zeros to the back in-place preserving relative order. Return non-zero count."""
    write_idx = 0
    n = len(nums)
    
    for read_idx in range(n):
        if nums[read_idx] != 0:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
            
    for i in range(write_idx, n):
        nums[i] = 0
        
    return write_idx
