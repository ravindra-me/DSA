def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    """Return the number of contiguous subarrays with product strictly less than k."""
    if k <= 1:
        return 0

    left = 0
    product = 1
    count = 0

    for right, val in enumerate(nums):
        product *= val
        while product >= k and left <= right:
            product //= nums[left]
            left += 1
        count += right - left + 1

    return count
