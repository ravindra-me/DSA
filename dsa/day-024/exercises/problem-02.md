# Problem 2: Minimum Size Subarray Sum

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | variable-size window (shortest subarray) | [Day 24: Sliding Window](../README.md) |

## Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray `[nums[l], nums[l+1], ..., nums[r-1], nums[r]]` of which the sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

## Input

An integer `target: int` and a list of positive integers `nums: list[int]`.

## Output

An integer representing the minimal length, or 0 if none exists.

## Constraints

- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

## Examples

**Example 1**

```text
Input:  target = 7, nums = [2, 3, 1, 2, 4, 3]
Output: 2
```

The subarray [4, 3] has the minimal length under the problem constraints.

**Example 2**

```text
Input:  target = 100, nums = [1, 2, 3, 4, 5]
Output: 0
```

Total sum is 15, which is less than 100, so return 0.

## Function Signature

```python
def min_sub_array_len(target: int, nums: list[int]) -> int:
    """Returns the minimum length of a contiguous subarray whose sum is >= target, or 0 if none."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Expand the right pointer while accumulating sum. When sum >= target, update minimum length and contract the window from the left. Target O(N) time and O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
