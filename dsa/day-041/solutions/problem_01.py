from collections import deque


def max_min_spread(nums: list[int], k: int) -> list[int]:
    """Compute max - min for each window of size k in O(n) time."""
    if not nums or k <= 0:
        return []

    max_dq: deque[int] = deque()
    min_dq: deque[int] = deque()
    spreads: list[int] = []

    for i, val in enumerate(nums):
        # Evict indices that have fallen outside the current window
        while max_dq and max_dq[0] <= i - k:
            max_dq.popleft()
        while min_dq and min_dq[0] <= i - k:
            min_dq.popleft()

        # Maintain monotonic decreasing order for max_dq
        while max_dq and nums[max_dq[-1]] <= val:
            max_dq.pop()
        max_dq.append(i)

        # Maintain monotonic increasing order for min_dq
        while min_dq and nums[min_dq[-1]] >= val:
            min_dq.pop()
        min_dq.append(i)

        # Record difference once the first window is formed
        if i >= k - 1:
            spreads.append(nums[max_dq[0]] - nums[min_dq[0]])

    return spreads
