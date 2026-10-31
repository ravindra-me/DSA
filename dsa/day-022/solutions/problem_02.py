def remove_duplicates_at_most_two(nums: list[int]) -> int:
    """Modify nums in-place so each element appears at most twice. Return new length."""
    if len(nums) <= 2:
        return len(nums)

    write = 2
    for read in range(2, len(nums)):
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1

    return write
