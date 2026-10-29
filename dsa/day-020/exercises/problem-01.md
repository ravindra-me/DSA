# Problem 1: Subarray Sum Divisibility Counter

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Modular Arithmetic with Hash Map Prefix Sums | [Day 20: Basic Mathematics for DSA](../README.md) |

## Problem Statement

Given an integer array `nums` and an integer `k`, return the number of non-empty continuous subarrays whose sum is divisible by `k`.

Remember that subarrays can contain negative values, so your modular arithmetic must handle remainders correctly.

## Input

An array of integers `nums: list[int]` and a positive integer `k: int`.

## Output

An integer representing the count of subarrays divisible by `k`.

## Constraints

- 1 <= len(nums) <= 30000
- -10^4 <= nums[i] <= 10^4
- 2 <= k <= 10000

## Examples

**Example 1**

```text
Input:  nums = [4, 5, 0, -2, -3, 1], k = 5
Output: 7
```

The 7 subarrays are: [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3].

**Example 2**

```text
Input:  nums = [5], k = 9
Output: 0
```

No subarray has a sum divisible by 9.

## Function Signature

```python
def count_subarrays_divisible(nums: list[int], k: int) -> int:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a running prefix sum modulo k, store counts of remainders in a frequency map, and normalize negative remainders in O(n) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
