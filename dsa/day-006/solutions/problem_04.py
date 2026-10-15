def single_number_two_uniques(nums: list[int]) -> list[int]:
    """Find the two unique numbers in nums, returned in ascending order."""
    xor_all = 0
    for num in nums:
        xor_all ^= num

    # Isolate the lowest set bit where the two unique numbers differ
    diff_bit = xor_all & (-xor_all)

    num1 = 0
    num2 = 0
    for num in nums:
        if num & diff_bit:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2] if num1 < num2 else [num2, num1]
