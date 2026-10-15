def single_number(nums: list[int]) -> int:
    """Find the single element that appears only once in nums."""
    unique_val = 0
    for num in nums:
        unique_val ^= num
    return unique_val
