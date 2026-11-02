# Solution 2: Minimum Size Subarray Sum

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** variable-size window (shortest subarray)

## Approach

We use a variable-size sliding window with two pointers (`left` and `right`). We expand `right` to accumulate numbers into `current_sum`. As soon as `current_sum >= target`, we try to shrink the window from the left by advancing `left` while keeping track of the minimum window length found so far.

## Thought Process

A brute-force approach evaluates all possible subarrays of `nums`, taking $O(N^2)$ time by computing sums, or $O(N^3)$ without prefix sums. However, because all numbers in `nums` are strictly positive, adding an element strictly increases the window sum, and removing an element strictly decreases it. This monotonic property allows us to use two pointers: `right` expands the window until the sum meets or exceeds `target`, and `left` contracts the window to find the smallest valid length starting at or after `left`. Since both `left` and `right` traverse the array at most once, the time complexity drops from $O(N^2)$ to $O(N)$.

## Algorithm

1. Initialize `min_len` to infinity (or `len(nums) + 1`), `current_sum` to 0, and `left` pointer to 0.
2. Iterate `right` from 0 to `len(nums) - 1`, adding `nums[right]` to `current_sum`.
3. While `current_sum >= target`, update `min_len = min(min_len, right - left + 1)`, subtract `nums[left]` from `current_sum`, and increment `left` by 1.
4. After the loop finishes, return `min_len` if it was updated, otherwise return 0.

## Complexity Analysis

- **Time:** $O(N)$ where $N$ is the length of `nums`. Each element is added to `current_sum` once by `right` and subtracted at most once by `left`.
- **Space:** $O(1)$ auxiliary space as we only store a few variables (`left`, `right`, `current_sum`, `min_len`).

## Edge Cases

- No valid subarray exists (sum of entire array < target): Returns 0.
- Single element array: Correctly checks if `nums[0] >= target` returning 1 or 0.
- Exact match target: Window contracts immediately when reaching exact target value.
- Large values of `target` and `nums`: Solved in linear time without stack overflow or excess space.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def min_sub_array_len(target: int, nums: list[int]) -> int:
    """Returns the minimum length of a contiguous subarray whose sum is >= target, or 0 if none."""
    n = len(nums)
    min_len = n + 1
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len <= n else 0
```
