# Problem 1: First and Last Position of Target

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | first-last-occurrence | [Day 28: Binary Search Variations](../README.md) |

## Problem Statement

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with $O(\log N)$ runtime complexity.

## Input

A sorted list of integers `nums` and an integer `target`.

## Output

A list of two integers `[first_index, last_index]`.

## Constraints

- 0 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is sorted in non-decreasing order.
- -10^9 <= target <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]
```

Target 8 appears starting at index 3 and ending at index 4.

**Example 2**

```text
Input:  nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
```

Target 6 is not in nums.

**Example 3**

```text
Input:  nums = [], target = 0
Output: [-1, -1]
```

An empty array has no elements.

## Function Signature

```python
def search_range(nums: list[int], target: int) -> list[int]:
    """Return the first and last 0-based indices of target in nums."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use binary search twice: once to find the leftmost (first) occurrence of target, and once to find the rightmost (last) occurrence. Maintain candidate answers during execution.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
