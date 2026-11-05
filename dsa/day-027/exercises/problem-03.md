# Problem 3: Find First and Last Position of Element in Sorted Array

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Boundary searching (lower bound and upper bound) with duplicate values | [Day 27: Binary Search](../README.md) |

## Problem Statement

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with $O(\log n)$ runtime complexity.

## Input

A list of integers `nums` sorted in non-decreasing order and an integer `target`.

## Output

A list of two integers `[first_index, last_index]`.

## Constraints

- 0 <= len(nums) <= 10^5
- -10^9 <= nums[i], target <= 10^9
- nums is sorted in non-decreasing order.

## Examples

**Example 1**

```text
Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]
```

8 first occurs at index 3 and last occurs at index 4.

**Example 2**

```text
Input:  nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
```

6 is not present in the array.

**Example 3**

```text
Input:  nums = [], target = 0
Output: [-1, -1]
```

Array is empty.

## Function Signature

```python
def search_range(nums: list[int], target: int) -> list[int]:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Perform two separate binary searches: one to locate the first occurrence (continue searching left when matching) and one to locate the last occurrence (continue searching right when matching).

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
