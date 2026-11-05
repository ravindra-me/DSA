# Problem 1: Standard Binary Search

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Basic search space halving on a distinct sorted array | [Day 27: Binary Search](../README.md) |

## Problem Statement

Given an array of distinct integers `nums` sorted in ascending order and an integer `target`, write a function to search `target` in `nums`. If `target` exists, return its index. Otherwise, return `-1`.

You must write an algorithm with $O(\log n)$ runtime complexity.

## Input

A list of distinct integers `nums` sorted in ascending order and an integer `target`.

## Output

An integer representing the index of `target`, or `-1` if not present.

## Constraints

- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i], target <= 10^4
- All integers in nums are unique.
- nums is sorted in ascending order.

## Examples

**Example 1**

```text
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
```

9 exists in nums and its index is 4

**Example 2**

```text
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
```

2 does not exist in nums so return -1

## Function Signature

```python
def search(nums: list[int], target: int) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use standard two-pointer iterative binary search maintains `low <= high` with `mid` calculation.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
