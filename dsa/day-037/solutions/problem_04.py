def _insertion_sort(bucket: list[float]) -> None:
    """Sorts a bucket in-place using insertion sort."""
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def bucket_sort(nums: list[float]) -> list[float]:
    """Sorts floats in [0, 1) in average O(n) time using Bucket Sort."""
    n = len(nums)
    if n <= 1:
        return list(nums)

    buckets: list[list[float]] = [[] for _ in range(n)]

    for x in nums:
        index = int(x * n)
        if index >= n:
            index = n - 1
        buckets[index].append(x)

    result: list[float] = []
    for bucket in buckets:
        _insertion_sort(bucket)
        result.extend(bucket)

    return result
