def sift_down(nums: list[int], heap_size: int, i: int) -> None:
    """Sift down the element at index i within the heap boundaries [0, heap_size - 1]."""
    curr = i
    while True:
        left = 2 * curr + 1
        right = 2 * curr + 2
        largest = curr

        if left < heap_size and nums[left] > nums[largest]:
            largest = left
        if right < heap_size and nums[right] > nums[largest]:
            largest = right

        if largest == curr:
            break

        nums[curr], nums[largest] = nums[largest], nums[curr]
        curr = largest
