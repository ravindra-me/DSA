import heapq


def sort_k_messed_array(nums: list[int], k: int) -> list[int]:
    """Sort an array where each element is at most k places away from sorted position."""
    n = len(nums)
    if n <= 1 or k == 0:
        return nums

    window_size = min(k + 1, n)
    heap = nums[:window_size]
    heapq.heapify(heap)

    write_idx = 0
    for read_idx in range(window_size, n):
        nums[write_idx] = heapq.heapreplace(heap, nums[read_idx])
        write_idx += 1

    while heap:
        nums[write_idx] = heapq.heappop(heap)
        write_idx += 1

    return nums
