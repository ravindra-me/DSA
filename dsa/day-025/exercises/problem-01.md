# Problem 1: First Occurrence Index

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Basic sequential scan with early exit | [Day 25: Linear Search](../README.md) |

## Problem Statement

Given an unsorted list of integers `nums` and an integer `target`, return the 0-based index of the **first occurrence** of `target`. If `target` is not present in `nums`, return `-1`.

## Input

A list of integers `nums` and an integer `target`.

## Output

An integer representing the first 0-based index of `target`, or `-1` if absent.

## Constraints

- 0 <= len(nums) <= 10^5
- -10^9 <= nums[i], target <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [4, 2, 7, 2, 5], target = 2
Output: 1
```

Target 2 first appears at index 1.

**Example 2**

```text
Input:  nums = [1, 3, 5], target = 4
Output: -1
```

Target 4 is not in nums.

## Function Signature

```python
def find_first_occurrence(nums: list[int], target: int) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Iterate sequentially through the array, returning immediately when target is found. Target complexity: O(n) time, O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
