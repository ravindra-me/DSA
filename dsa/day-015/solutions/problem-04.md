# Solution 4: Longest Continuous Subarray With Absolute Diff <= Limit

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Dual Monotonic Deques (Min & Max)

## Approach

Use a sliding window maintained by two monotonic deques: one strictly decreasing (preserving maximums at the front) and one strictly increasing (preserving minimums at the front). As the right boundary expands, update both deques. When the difference between the current maximum and minimum exceeds `limit`, increment the left boundary and pop out-of-window elements from the fronts of the deques.

## Thought Process

A brute-force solution checks all $O(n^2)$ subarrays, taking $O(n)$ or $O(\log n)$ per subarray to find the minimum and maximum, resulting in $O(n^3)$ or $O(n^2)$ time, which is too slow for $n = 10^5$.

Notice that if a subarray `nums[left..right]` violates the condition `max - min <= limit`, any larger subarray containing it with the same `left` will also have a range at least as large, meaning we should advance `left`. This monotonic property suggests a sliding window `[left, right]`.

To check the validity in $O(1)$ amortized time, we must maintain the maximum and minimum of the current window as elements are added at `right` and removed at `left`. A monotonic queue (deque) allows inserting at the back in amortized $O(1)$ and obtaining the extreme value at the front in $O(1)$. By maintaining two deques—`min_deque` and `max_deque`—we can inspect the window's max (`max_deque[0]`) and min (`min_deque[0]`) in $O(1)$ time, yielding an optimal $O(n)$ two-pointer algorithm.

## Algorithm

1. Initialize two empty deques: `min_deque` (maintaining increasing elements) and `max_deque` (maintaining decreasing elements).
2. Initialize `left = 0` and `max_len = 0`.
3. Iterate with `right` through indices $0$ to $len(nums) - 1$:
4. While `max_deque` is not empty and its back element is less than `nums[right]`, pop from the back of `max_deque`.
5. Append `nums[right]` to `max_deque`.
6. While `min_deque` is not empty and its back element is greater than `nums[right]`, pop from the back of `min_deque`.
7. Append `nums[right]` to `min_deque`.
8. While `max_deque[0] - min_deque[0] > limit`:
9. If `nums[left] == max_deque[0]`, pop the front of `max_deque`.
10. If `nums[left] == min_deque[0]`, pop the front of `min_deque`.
11. Increment `left` by 1.
12. Update `max_len = max(max_len, right - left + 1)`.
13. Return `max_len`.

## Complexity Analysis

- **Time:** O(n) where n is the length of `nums`. Each element is pushed and popped at most once from each deque, and both `left` and `right` pointers traverse the array at most once.
- **Space:** O(n) in the worst case to store elements in the two deques.

## Edge Cases

- Empty array: returns 0 immediately.
- Single element: always valid with difference 0 <= limit; returns 1.
- limit = 0: only contiguous identical values are valid.
- All elements within limit: window expands to the entire array of length n without shrinking.
- Strictly decreasing or increasing sequence: handles monotonic deque updates cleanly without stale indices.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
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
```
