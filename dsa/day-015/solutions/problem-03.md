# Solution 3: Sliding Window Maximum

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Monotonic Decreasing Deque

## Approach

Maintain a monotonic decreasing deque that stores indices of elements within the current sliding window. The front of the deque always holds the index of the maximum element for the current window. When sliding the window, prune expired indices from the front and smaller values from the back before inserting the current index.

## Thought Process

A naive approach checks all `k` elements in each window, resulting in $O(n \times k)$ time complexity, which times out when $n = 10^5$ and $k \approx 5 \times 10^4$. A max-heap would allow $O(n \log k)$ or $O(n \log n)$, but we can do better in $O(n)$ using a deque.

Notice that if an element $nums[i]$ arrives and is greater than or equal to an earlier element $nums[j]$ ($j < i$), $nums[j]$ can never be the maximum of any subsequent window because $nums[i]$ is both larger and will stay in the window longer. Thus, $nums[j]$ is redundant and can be discarded.

By keeping indices in decreasing order of their corresponding values in a deque:
1. The maximum element is always at `deque[0]`.
2. Before adding index `i`, we pop all indices from the back whose values are $\le nums[i]$.
3. We evict the front if its index has fallen out of the window (`index <= i - k`).
4. Once the first window is formed (`i >= k - 1`), we record `nums[deque[0]]` to our result.

## Algorithm

1. Initialize an empty double-ended queue `deq = collections.deque()` to store indices, and an empty list `result`.
2. Iterate through the array with index `i` and value `x`.
3. Remove indices from the front of `deq` that are outside the current window: while `deq` is non-empty and `deq[0] <= i - k`, pop from the left.
4. Maintain the decreasing property: while `deq` is non-empty and `nums[deq[-1]] <= x`, pop from the right.
5. Append index `i` to the back of `deq`.
6. If the current index `i >= k - 1`, the window is fully formed; append `nums[deq[0]]` to `result`.
7. Return `result`.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the length of `nums`. Each index is pushed into the deque once and popped at most once across the entire iteration.
- **Space:** $O(k)$ auxiliary space for the deque, which stores at most $k$ indices at any time (excluding the $O(n - k + 1)$ space for the returned result list).

## Edge Cases

- k = 1: Every element forms its own window; the output is identical to nums.
- k = len(nums): Exactly one window spanning the entire array; output contains just one element (the global max).
- All elements equal: The deque stays size 1 or updates cleanly without violating bounds.
- Strictly decreasing or increasing elements: Monotonic property naturally maintains order or triggers immediate evictions.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Return the maximum element in every contiguous window of size k."""
    if not nums or k <= 0:
        return []
    
    window_indices: deque[int] = deque()
    result: list[int] = []
    
    for i, val in enumerate(nums):
        # Evict indices that have slipped out of the window
        while window_indices and window_indices[0] <= i - k:
            window_indices.popleft()
        
        # Maintain monotonic decreasing order by value
        while window_indices and nums[window_indices[-1]] <= val:
            window_indices.pop()
            
        window_indices.append(i)
        
        # Once window has reached size k, record the maximum
        if i >= k - 1:
            result.append(nums[window_indices[0]])
            
    return result
```
