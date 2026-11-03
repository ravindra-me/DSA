# Problem 4: Longest Equal Element Sequence under Skip Constraint

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Linear scan state tracking with limited dynamic state | [Day 25: Linear Search](../README.md) |

## Problem Statement

Given an array of integers `nums` and an integer `k`, find the length of the longest contiguous subsegment consisting of identical values if you are allowed to skip (ignore) at most `k` non-matching elements during the sequence scan. The skipped elements do not change the sequence value.

## Input

A list of integers `nums` and an integer `k`.

## Output

An integer representing max contiguous equal length.

## Constraints

- 1 <= len(nums) <= 10^5
- 0 <= k <= 10^5
- 0 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 1, 1, 3, 1], k = 1
Output: 5
```

For target 1: elements at indices 0, 2, 3, 5 with '2' skipped (1 skip total used) gives length 5.

**Example 2**

```text
Input:  nums = [4, 4, 4], k = 2
Output: 3
```

All elements equal.

## Function Signature

```python
def max_equal_frequency_with_skips(nums: list[int], k: int) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Track dynamic frequency windows or perform dynamic linear pass for distinct numbers using two-pointers / linear state scan. Target complexity: O(n) time, O(n) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
