def partition_lomuto(nums: list[int], pivot_index: int) -> int:
    """Partition nums in-place using Lomuto scheme with the given pivot index.

    Returns the final index of the pivot element after partitioning.
    """
    n = len(nums)
    pivot_val = nums[pivot_index]
    
    # Move pivot to the end
    nums[pivot_index], nums[-1] = nums[-1], nums[pivot_index]
    
    i = 0
    for j in range(n - 1):
        if nums[j] <= pivot_val:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            
    # Move pivot to its final place
    nums[i], nums[-1] = nums[-1], nums[i]
    return i
