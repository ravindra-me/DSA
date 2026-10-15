def find_maximum_xor(nums: list[int]) -> int:
    """Return the maximum XOR value formed by any two numbers in nums."""
    max_xor = 0
    mask = 0

    for bit in range(30, -1, -1):
        mask |= (1 << bit)
        prefixes = {num & mask for num in nums}
        candidate = max_xor | (1 << bit)

        for prefix in prefixes:
            if (prefix ^ candidate) in prefixes:
                max_xor = candidate
                break

    return max_xor
