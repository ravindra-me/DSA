import math

def maximum_gap(nums: list[int]) -> int:
    """Finds the maximum gap in sorted order in linear O(n) time."""
    n = len(nums)
    if n < 2:
        return 0

    min_val = min(nums)
    max_val = max(nums)
    if min_val == max_val:
        return 0

    bucket_size = max(1, (max_val - min_val) // (n - 1))
    bucket_count = (max_val - min_val) // bucket_size + 1

    bucket_min = [math.inf] * bucket_count
    bucket_max = [-math.inf] * bucket_count

    for num in nums:
        idx = (num - min_val) // bucket_size
        if num < bucket_min[idx]:
            bucket_min[idx] = num
        if num > bucket_max[idx]:
            bucket_max[idx] = num

    max_gap = 0
    prev_max = min_val

    for b_min, b_max in zip(bucket_min, bucket_max):
        if b_min == math.inf:
            continue
        max_gap = max(max_gap, int(b_min - prev_max))
        prev_max = b_max

    return max_gap
