# Solution 5: Constrained Subsequence Sum with Width Limit

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Monotonic Stack/Deque with Dynamic Programming

## Approach

We maintain a dynamic programming array `dp[i]` representing the maximum constrained subsequence sum ending at index `i`. The state transition is `dp[i] = nums[i] + max(0, max(dp[j]))` for `i - k <= j < i`. To compute `max(dp[j])` in $O(1)$ time per index, we maintain a monotonically decreasing double-ended queue (deque) containing indices of candidate previous values.

## Thought Process

A naive DP state calculates `dp[i]` by looking back up to `k` elements, which takes $O(k)$ per element and $O(n \cdot k)$ overall time. Since $N, k \le 10^5$, an $O(N \cdot k)$ approach will time out. We need to find the maximum value in a sliding window of size `k` over the array `dp`. This is the classic sliding window maximum problem, which can be solved efficiently using a monotonic deque (or a max-heap with lazy deletion). The monotonic deque stores DP values in strictly decreasing order. When moving to index `i`, we pop elements from the front of the deque if their indices fall outside the allowed window `[i - k, i - 1]`. We use the maximum DP value at the front of the deque to compute `dp[i]`, and then maintain the deque's monotonic property by popping elements from the back that are smaller than `dp[i]` before pushing `i`.

## Algorithm

1. Initialize a deque `dq` to store indices of DP values.
2. Initialize `max_sum` to negative infinity (or `nums[0]`).
3. For each index `i` from `0` to `len(nums) - 1`:
4. Remove indices from the front of `dq` if they are less than `i - k` (out of the sliding window).
5. Compute `dp[i] = nums[i] + (dp[dq[0]] if dq and dp[dq[0]] > 0 else 0)`.
6. Update `max_sum = max(max_sum, dp[i])`.
7. While `dq` is not empty and `dp[dq[-1]] <= dp[i]`, pop from the back of `dq` to maintain decreasing order.
8. Append index `i` to `dq`.
9. Return `max_sum`.

## Complexity Analysis

- **Time:** O(N) where N is the length of `nums`. Each index is pushed and popped from the deque at most once.
- **Space:** O(N) to store the `dp` array and up to O(k) for the monotonic deque.

## Edge Cases

- All negative numbers: Subsequence must be non-empty, so the max single negative element should be returned.
- k >= len(nums): The sliding window covers all previous elements.
- k = 1: Subsequence elements must be strictly adjacent, reducing to max subarray sum with non-negative extensions.
- Single element array: Returns `nums[0]` directly.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
from collections import deque

def constrained_subset_sum(nums: list[int], k: int) -> int:
    """Compute maximum sum of a non-empty subsequence with distance <= k between indices."""
    n = len(nums)
    dp = [0] * n
    dq = deque()  # stores indices, dp[dq] is strictly decreasing
    max_sum = float('-inf')
    
    for i in range(n):
        # Remove indices outside the k-window
        if dq and dq[0] < i - k:
            dq.popleft()
        
        # Max value in window is dp[dq[0]] if positive
        max_prev = dp[dq[0]] if dq and dp[dq[0]] > 0 else 0
        dp[i] = nums[i] + max_prev
        
        max_sum = max(max_sum, dp[i])
        
        # Maintain monotonic decreasing order in deque
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
            
        dq.append(i)
        
    return max_sum
```
