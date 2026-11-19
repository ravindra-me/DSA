# Problem 1: Sliding Window Max-Min Spread

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Amortized O(1) per element with Monotonic Deques | [Day 41: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Given an integer array `nums` and a window size `k`, return an array `spreads` where `spreads[i]` is the difference between the maximum and minimum elements in the sliding window `nums[i : i + k]`. You must achieve an overall time complexity of $O(n)$ and $O(k)$ auxiliary space.

## Input

An array of integers `nums` and a positive integer `k` (`1 <= k <= len(nums)`).

## Output

A list of integers representing `max(window) - min(window)` for each valid sliding window of length `k`.

## Constraints

- 1 <= k <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [4, 6, 8, 8, 3, 4]
```

Windows: [1, 3, -1] -> 3 - (-1) = 4; [3, -1, -3] -> 3 - (-3) = 6; [-1, -3, 5] -> 5 - (-3) = 8; [-3, 5, 3] -> 5 - (-3) = 8; [5, 3, 6] -> 6 - 3 = 3; [3, 6, 7] -> 7 - 3 = 4.

**Example 2**

```text
Input:  nums = [4, 4, 4, 4], k = 2
Output: [0, 0, 0]
```

Every window of size 2 has max = 4 and min = 4, spread = 0.

## Function Signature

```python
def max_min_spread(nums: list[int], k: int) -> list[int]:
    """Compute max - min for each window of size k in O(n) time."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain two monotonic deques (one strictly decreasing for max, one strictly increasing for min) over the sliding window to achieve O(1) amortized updates per element.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
