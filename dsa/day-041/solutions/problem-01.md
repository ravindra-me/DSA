# Solution 1: Sliding Window Max-Min Spread

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy/Medium | **Concept:** Amortized O(1) per element with Monotonic Deques

## Approach

Maintain two double-ended queues (deques) storing indices of elements in the current window: one monotonically decreasing to track the maximum element, and one monotonically increasing to track the minimum element. For each new index, pop smaller/larger elements from the back of the respective deques, purge indices that fall outside the window from the front, and record `nums[max_deque[0]] - nums[min_deque[0]]` once the window reaches size `k`.

## Thought Process

A naive approach recalculates the maximum and minimum for every window of size $k$ by inspecting all $k$ elements, taking $O(n \cdot k)$ time. In the worst case where $k = n / 2$, this degrades to $O(n^2)$, which is too slow for $n = 10^5$.

To improve this, recognize that as the window slides, elements enter and exit sequentially. We can track the extrema using monotonic deques. For the maximum, any element in the deque that is smaller than the newly arriving element can never be the maximum in the current or any future window that contains the new element, so it can be evicted from the back. The front of the deque will always point to the index of the maximum element in the active window. The same logic inverted applies to maintaining the window's minimum.

Because each index is pushed to and popped from each deque at most once, the amortized cost per element is $O(1)$, leading to an overall $O(n)$ time complexity and $O(k)$ auxiliary space.

## Algorithm

1. Initialize two empty deques: `max_dq` (storing indices in decreasing order of values) and `min_dq` (storing indices in increasing order of values), along with a result list `spreads`.
2. Iterate through the array with index `i` and value `val = nums[i]`.
3. Remove indices from the front of both `max_dq` and `min_dq` that are out of bounds (i.e., index `<= i - k`).
4. Maintain monotonicity for `max_dq`: while `max_dq` is not empty and `nums[max_dq[-1]] <= val`, pop from the back.
5. Maintain monotonicity for `min_dq`: while `min_dq` is not empty and `nums[min_dq[-1]] >= val`, pop from the back.
6. Append index `i` to the back of both deques.
7. Once `i >= k - 1` (the initial window of length `k` has formed), calculate the spread as `nums[max_dq[0]] - nums[min_dq[0]]` and append it to `spreads`.
8. Return `spreads`.

## Complexity Analysis

- **Time:** O(n) - Each element's index is added to and removed from each deque at most once, ensuring amortized O(1) operations per window step.
- **Space:** O(k) - Auxiliary space for the two deques, which at any time store at most k indices each (excluding the O(n - k + 1) output list).

## Edge Cases

- k = 1: Every window has size 1, so the maximum equals the minimum and every spread is 0.
- k = len(nums): Exactly one window spanning the entire array, returning a single element.
- All identical elements: Differences are consistently 0, properly handled by non-strict comparisons.
- Strictly increasing or decreasing array: One deque retains all k elements while the other pops frequently, maintaining correct boundaries and amortized cost.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
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
```
