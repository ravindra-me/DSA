# Problem 4: Longest Continuous Subarray With Absolute Diff <= Limit

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Dual Monotonic Deques (Min & Max) | [Day 15: Deque & Monotonic Queue](../README.md) |

## Problem Statement

Given an array of integers `nums` and an integer `limit`, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to `limit`.

## Input

`nums: list[int]`, `limit: int`.

## Output

`int` - the maximum length of a valid subarray.

## Constraints

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 0 <= limit <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [8, 2, 4, 7], limit = 4
Output: 2
```

Valid subarrays include [2, 4] with max diff |2 - 4| = 2 <= 4, and [4, 7] with |4 - 7| = 3 <= 4. Longest size is 2.

**Example 2**

```text
Input:  nums = [10, 1, 2, 4, 7, 2], limit = 5
Output: 4
```

Subarray [2, 4, 7, 2] has max element 7 and min element 2. Absolute difference = 5 <= 5. Length is 4.

**Example 3**

```text
Input:  nums = [4, 2, 2, 2, 4, 4, 2, 2], limit = 0
Output: 3
```

Subarray [2, 2, 2] has max diff 0 <= 0.

## Function Signature

```python
def longest_subarray_with_limit(nums: list[int], limit: int) -> int:
    """Return the length of the longest subarray whose max - min <= limit."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a variable-size sliding window with two monotonic deques: one tracking the window's maximum and the other tracking the window's minimum. When `max - min > limit`, advance the left pointer.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
