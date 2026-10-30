# Problem 3: Subarray Sum Equals K

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Prefix Sum with Hash Map | [Day 21: Prefix & Suffix Techniques](../README.md) |

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the total number of non-empty contiguous subarrays whose sum equals `k`.

Note that elements may be positive, negative, or zero.

## Input

`nums`: list of integers.
`k`: integer target sum.

## Output

`int`: count of contiguous subarrays whose sum equals `k`.

## Constraints

- 1 <= len(nums) <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

## Examples

**Example 1**

```text
Input:  nums = [1, 1, 1], k = 2
Output: 2
```

Subarrays [1, 1] at indices [0..1] and [1..2] both sum to 2.

**Example 2**

```text
Input:  nums = [1, -1, 0], k = 0
Output: 3
```

Valid subarrays are [1, -1] (sum 0), [0] (sum 0), and [1, -1, 0] (sum 0).

## Function Signature

```python
def subarray_sum(nums: list[int], k: int) -> int:
    """Count the number of contiguous subarrays summing to k."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Track the running cumulative sum while storing frequencies of previously seen prefix sums in a hash map. For each step, add the occurrences of (current_sum - k) to the count.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
