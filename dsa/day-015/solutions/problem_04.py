from collections import deque


def longest_subarray_with_limit(nums: list[int], limit: int) -> int:
    """Return the length of the longest subarray whose max - min <= limit."""
    if not nums:
        return 0

    max_deque: deque[int] = deque()
    min_deque: deque[int] = deque()
    left = 0
    max_len = 0

    for right, val in enumerate(nums):
        while max_deque and max_deque[-1] < val:
            max_deque.pop()
        max_deque.append(val)

        while min_deque and min_deque[-1] > val:
            min_deque.pop()
        min_deque.append(val)

        while max_deque[0] - min_deque[0] > limit:
            if nums[left] == max_deque[0]:
                max_deque.popleft()
            if nums[left] == min_deque[0]:
                min_deque.popleft()
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
