# Problem 5: Subarrays with K Different Integers

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | exact-K window via at-most reduction | [Day 24: Sliding Window](../README.md) |

## Problem Statement

Given an integer array `nums` and an integer `k`, return the number of good contiguous subarrays of `nums`.

A good array is an array where the number of different integers in that array is exactly `k`.

For example, `[1, 2, 3, 1, 2]` has 3 different integers: 1, 2, and 3.

## Input

An array of integers `nums: list[int]` and an integer `k: int`.

## Output

An integer representing the total count of good subarrays.

## Constraints

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= nums.length
- 1 <= k <= nums.length

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 1, 2, 3], k = 2
Output: 7
```

Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

**Example 2**

```text
Input:  nums = [1, 2, 1, 3, 4], k = 3
Output: 3
```

Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

## Function Signature

```python
def subarrays_with_k_distinct(nums: list[int], k: int) -> int:
    """Counts the number of contiguous subarrays having exactly k distinct integers."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Reduce the exact condition to counting subarrays with at most K distinct integers minus at most (K - 1) distinct integers: exact(k) = at_most(k) - at_most(k - 1). Implement at_most using variable sliding window in O(N) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
