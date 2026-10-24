from collections import deque
import math

def shortest_subarray_at_least_k(nums: list[int], k: int) -> int:
    """Return the minimum length of a contiguous subarray with sum at least k, or -1."""
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    min_len = math.inf
    q: deque[int] = deque()

    for i in range(n + 1):
        # Check if the smallest prefix sums in deque can form a valid subarray
        while q and prefix[i] - prefix[q[0]] >= k:
            min_len = min(min_len, i - q.popleft())

        # Maintain strictly increasing order of prefix sums in the deque
        while q and prefix[i] <= prefix[q[-1]]:
            q.pop()

        q.append(i)

    return min_len if min_len != math.inf else -1
