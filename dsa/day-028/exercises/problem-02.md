# Problem 2: Search in Rotated Sorted Array

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | rotated-sorted-array | [Day 28: Binary Search Variations](../README.md) |

## Problem Statement

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < len(nums)`).

For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with $O(\log N)$ runtime complexity.

## Input

A list of distinct integers `nums` (rotated sorted) and an integer `target`.

## Output

An integer representing the 0-based index of `target`, or `-1` if not found.

## Constraints

- 1 <= len(nums) <= 5 * 10^4
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- -10^4 <= target <= 10^4

## Examples

**Example 1**

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
```

Target 0 is located at index 4.

**Example 2**

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
```

Target 3 is not present in the array.

**Example 3**

```text
Input:  nums = [1], target = 0
Output: -1
```

Single element array not matching target.

## Function Signature

```python
def search_rotated(nums: list[int], target: int) -> int:
    """Return the index of target in rotated sorted array nums, or -1 if not found."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use binary search. At index `mid`, determine which half of the array is sorted by comparing `nums[left]` and `nums[mid]`. Check if `target` lies within that sorted range to halve the search space.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
