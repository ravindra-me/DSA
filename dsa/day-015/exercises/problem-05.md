# Problem 5: Shortest Subarray with Sum at Least K

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Prefix Sums with Monotonic Queue Optimization | [Day 15: Deque & Monotonic Queue](../README.md) |

## Problem Statement

Given an integer array `nums` and an integer `k`, return the length of the shortest non-empty subarray of `nums` with a sum of at least `k`. If there is no such subarray, return `-1`.

A subarray is a contiguous part of an array. Note that `nums` may contain negative numbers.

## Input

`nums: list[int]`, `k: int`.

## Output

`int` - the minimum length, or `-1` if no such subarray exists.

## Constraints

- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
- 1 <= k <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [1], k = 1
Output: 1
```

Subarray [1] has sum 1 >= 1. Length is 1.

**Example 2**

```text
Input:  nums = [1, 2], k = 4
Output: -1
```

Maximum possible subarray sum is 3, which is less than 4.

**Example 3**

```text
Input:  nums = [2, -1, 2], k = 3
Output: 3
```

Subarray [2, -1, 2] has sum 3 >= 3. Length is 3.

**Example 4**

```text
Input:  nums = [84, -37, 32, 40, 95], k = 167
Output: 3
```

Subarray [32, 40, 95] has sum 167 >= 167. Length is 3.

## Function Signature

```python
def shortest_subarray_at_least_k(nums: list[int], k: int) -> int:
    """Return the minimum length of a contiguous subarray with sum at least k, or -1."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Compute prefix sums. Maintain an increasing deque of prefix sum indices. For each index `i`, pop from the front while `prefix[i] - prefix[deque[0]] >= k` to find the shortest subarray ending at `i`. Pop from the back while `prefix[i] <= prefix[deque[-1]]` to maintain an increasing order.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
