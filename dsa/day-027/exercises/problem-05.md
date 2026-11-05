# Problem 5: Search in Rotated Sorted Array

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Modified binary search on a shifted/rotated sorted domain | [Day 27: Binary Search](../README.md) |

## Problem Statement

There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed).

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with $O(\log n)$ runtime complexity.

## Input

A list of distinct integers `nums` (rotated sorted array) and an integer `target`.

## Output

An integer index of `target`, or `-1` if not found.

## Constraints

- 1 <= len(nums) <= 5000
- -10^4 <= nums[i], target <= 10^4
- All values of nums are unique.
- nums is an ascending sorted array that has been rotated between 0 and n times.

## Examples

**Example 1**

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
```

0 is located at index 4.

**Example 2**

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
```

3 is not in the array.

**Example 3**

```text
Input:  nums = [1], target = 0
Output: -1
```

Target 0 is not in single-element array.

## Function Signature

```python
def search_rotated(nums: list[int], target: int) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

At any `mid`, at least one half (`[low..mid]` or `[mid..high]`) is strictly sorted. Check which half is sorted, then check if `target` falls within that sorted half to decide which direction to narrow.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
