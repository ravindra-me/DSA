def total_hamming_distance(nums: list[int]) -> int:
    """Calculate total Hamming distance across all pairs."""
    n = len(nums)
    if n < 2:
        return 0

    total_distance = 0
    # nums[i] <= 10^9 < 2^30, so 30 bits (0 through 29) are sufficient.
    for bit in range(30):
        ones = sum((x >> bit) & 1 for x in nums)
        total_distance += ones * (n - ones)

    return total_distance
