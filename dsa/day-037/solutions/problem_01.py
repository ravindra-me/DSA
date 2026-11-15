def counting_sort(nums: list[int]) -> list[int]:
    """Sorts integers in O(n + k) time using counting sort."""
    if not nums:
        return []

    min_val = min(nums)
    max_val = max(nums)
    range_len = max_val - min_val + 1

    counts = [0] * range_len
    for num in nums:
        counts[num - min_val] += 1

    result: list[int] = []
    for idx, count in enumerate(counts):
        if count > 0:
            result.extend([idx + min_val] * count)

    return result
