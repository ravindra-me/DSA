# Solution 5: Subarrays with K Different Integers

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** exact-K window via at-most reduction

## Approach

Counting subarrays with *exactly* $K$ distinct elements directly with a sliding window is difficult because expanding or shrinking the window doesn't yield a monotonic condition. However, `exactly(K) = at_most(K) - at_most(K - 1)`. Counting subarrays with *at most* $K$ distinct elements is a classic sliding window problem, as any subsegment of a valid window with at most $K$ distinct elements is also valid.

## Thought Process

A brute-force approach considers all $O(N^2)$ contiguous subarrays and counts distinct integers in each using a set/hash map, resulting in $O(N^2)$ time. 

To optimize, we attempt a sliding window approach. However, if a window contains exactly $K$ distinct elements, shrinking the window from the left might reduce the distinct count below $K$ or keep it at $K$ (if the removed element still exists elsewhere in the window). This lack of monotonicity makes standard two-pointer templates tricky for exact counts.

By rephrasing the problem: every subarray with *exactly* $K$ distinct integers is contained in the set of subarrays with *at most* $K$ distinct integers, but not in the set of subarrays with *at most* $K - 1$ distinct integers. 

For a fixed right pointer `right`, if the smallest left pointer that keeps the window having at most $K$ distinct elements is `left`, then all subarrays ending at `right` and starting at indices `left, left + 1, ..., right` have at most $K$ distinct elements. The number of such subarrays is simply `right - left + 1`. Summing this over all `right` positions gives the total count in $O(N)$ time.

## Algorithm

1. Define a helper function `at_most_k(nums, k)` that returns the number of contiguous subarrays with at most `k` distinct integers.
2. If `k <= 0`, `at_most_k` returns `0`.
3. In `at_most_k`, initialize a hash map `freq` to track counts of elements, `left = 0`, and `count = 0`.
4. Iterate `right` from `0` to `len(nums) - 1`:
5. Add `nums[right]` to `freq`.
6. While `len(freq) > k`, decrement `freq[nums[left]]`. If `freq[nums[left]]` drops to 0, remove `nums[left]` from `freq`. Increment `left`.
7. Add `(right - left + 1)` to `count`.
8. Return `at_most_k(nums, k) - at_most_k(nums, k - 1)`.

## Complexity Analysis

- **Time:** O(N) where N is the length of `nums`. Each element is processed at most twice by the `right` and `left` pointers in both calls to `at_most_k`.
- **Space:** O(K) auxiliary space to store the frequency map of distinct elements inside the current sliding window.

## Edge Cases

- k = 1: `at_most_k(nums, 0)` naturally returns 0, correctly leaving `at_most_k(nums, 1)`.
- k > len(nums): Handled naturally; `at_most_k` will never exceed the total number of subarrays, and `at_most_k(nums, k) - at_most_k(nums, k - 1)` will yield 0 if no subarray has k distinct elements.
- Single element array: Works correctly, returning 1 if k = 1 and 0 if k > 1.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
from collections import Counter

def subarrays_with_k_distinct(nums: list[int], k: int) -> int:
    """Counts the number of contiguous subarrays having exactly k distinct integers."""
    def at_most_k(k_val: int) -> int:
        if k_val <= 0:
            return 0
        
        freq = Counter()
        left = 0
        total_subarrays = 0
        
        for right in range(len(nums)):
            freq[nums[right]] += 1
            while len(freq) > k_val:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            total_subarrays += (right - left + 1)
            
        return total_subarrays

    return at_most_k(k) - at_most_k(k - 1)
```
