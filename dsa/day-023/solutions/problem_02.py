def single_number_ii(nums: list[int]) -> int:
    """Find the element that appears once among triple duplicates."""
    ones = 0
    twos = 0

    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones
