def partial_heap_sort(nums: list[int], k: int) -> None:
    """Place the k largest elements of nums in ascending order at nums[len(nums)-k:] in-place."""
    n = len(nums)
    if k <= 0 or n <= 1:
        return

    # Ensure k does not exceed array length
    k = min(k, n)

    def _sift_down(arr: list[int], root: int, end: int) -> None:
        while True:
            left_child = 2 * root + 1
            right_child = left_child + 1
            largest = root

            if left_child < end and arr[left_child] > arr[largest]:
                largest = left_child
            if right_child < end and arr[right_child] > arr[largest]:
                largest = right_child

            if largest == root:
                break

            arr[root], arr[largest] = arr[largest], arr[root]
            root = largest

    # 1. Build max-heap in-place: O(n)
    for i in range((n - 2) // 2, -1, -1):
        _sift_down(nums, i, n)

    # 2. Extract k largest elements: O(k log n)
    for i in range(n - 1, n - 1 - k, -1):
        nums[0], nums[i] = nums[i], nums[0]
        _sift_down(nums, 0, i)
