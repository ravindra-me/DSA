def _sift_down(nums: list[int], n: int, root: int) -> None:
    """Sift down root within the prefix of nums of length n to maintain max-heap."""
    largest = root
    while True:
        left = 2 * root + 1
        right = 2 * root + 2

        if left < n and nums[left] > nums[largest]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right

        if largest == root:
            break

        nums[root], nums[largest] = nums[largest], nums[root]
        root = largest


def heap_sort(nums: list[int]) -> None:
    """Sort nums in ascending order in-place using Heap Sort."""
    n = len(nums)
    if n <= 1:
        return

    # Phase 1: Build max-heap (bottom-up)
    for i in range((n // 2) - 1, -1, -1):
        _sift_down(nums, n, i)

    # Phase 2: Extract elements one by one
    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        _sift_down(nums, end, 0)
