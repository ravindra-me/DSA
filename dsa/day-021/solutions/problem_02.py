def product_except_self(nums: list[int]) -> list[int]:
    """Compute product of all elements except nums[i] without division."""
    n = len(nums)
    result = [1] * n

    # Prefix products: result[i] contains product of elements to the left of i
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    # Suffix products: multiply with running product of elements to the right
    suffix_prod = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix_prod
        suffix_prod *= nums[i]

    return result
