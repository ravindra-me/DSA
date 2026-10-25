# Problem 4: Subarray Sum Divisible by K

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Prefix sum with modulo hashing | [Day 16: HashMap](../README.md) |

## Problem Statement

Given an integer array `nums` and an integer `k`, return the number of non-empty continuous subarrays whose sum is divisible by `k`. Note that subarrays can contain negative numbers.

## Input

`nums: list[int]` - list of integers.
`k: int` - positive integer divisor.

## Output

`int` - count of contiguous subarrays whose sum is a multiple of `k`.

## Constraints

- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 2 <= k <= 10^4

## Examples

**Example 1**

```text
Input:  nums = [4, 5, 0, -2, -3, 1], k = 5
Output: 7
```

The 7 subarrays are [4, 5, 0, -2, -3, 1] (sum 5), [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3].

**Example 2**

```text
Input:  nums = [5], k = 9
Output: 0
```

Sum is 5, not divisible by 9.

## Function Signature

```python
def subarrays_div_by_k(nums: list[int], k: int) -> int:
    """Return the count of continuous subarrays with sum divisible by k."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use running prefix sums and modular arithmetic. If two prefix sums have the same remainder modulo `k`, the subarray between them is divisible by `k`. Maintain a frequency map of remainders.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
