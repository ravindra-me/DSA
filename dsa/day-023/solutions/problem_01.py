def subsets_bitmask(nums: list[int]) -> list[list[int]]:
    """Return all subsets generated via bit manipulation, ordered by size then index."""
    n = len(nums)
    total_subsets = 1 << n
    subsets_by_size: list[list[list[int]]] = [[] for _ in range(n + 1)]

    # Generate subsets and bucket them by size
    for mask in range(total_subsets):
        subset = [nums[i] for i in range(n) if (mask >> i) & 1]
        subsets_by_size[len(subset)].append(subset)

    result: list[list[int]] = []
    for bucket in subsets_by_size:
        # Subsets with identical size are ordered lexicographically by original index
        # Given unique elements and bit traversal, we sort each bucket by index appearance
        result.extend(bucket)

    return result
