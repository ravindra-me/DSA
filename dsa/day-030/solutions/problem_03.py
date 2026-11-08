def split_array(nums: list[int], k: int) -> int:
    """Return the minimized largest sum among k contiguous subarrays."""
    low = max(nums)
    high = sum(nums)

    def can_partition(max_sum: int) -> bool:
        count = 1
        current_sum = 0
        for num in nums:
            if current_sum + num > max_sum:
                count += 1
                current_sum = num
                if count > k:
                    return False
            else:
                current_sum += num
        return True

    while low < high:
        mid = low + (high - low) // 2
        if can_partition(mid):
            high = mid
        else:
            low = mid + 1

    return low
