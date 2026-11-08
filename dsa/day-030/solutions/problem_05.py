def smallest_distance_pair(nums: list[int], k: int) -> int:
    """Return the k-th smallest distance among all pairs."""
    nums.sort()
    n = len(nums)

    def count_less_or_equal(dist: int) -> int:
        count = 0
        left = 0
        for right in range(n):
            while nums[right] - nums[left] > dist:
                left += 1
            count += right - left
        return count

    low = 0
    high = nums[-1] - nums[0]

    while low < high:
        mid = (low + high) // 2
        if count_less_or_equal(mid) >= k:
            high = mid
        else:
            low = mid + 1

    return low
