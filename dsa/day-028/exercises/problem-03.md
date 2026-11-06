# Problem 3: Find Minimum in Rotated Sorted Array

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | rotated-sorted-array | [Day 28: Binary Search Variations](../README.md) |

## Problem Statement

Suppose an array of length $N$ sorted in ascending order is rotated between $1$ and $N$ times.

Given the rotated sorted array `nums` of **unique** elements, return the minimum element of this array.

You must write an algorithm that runs in $O(\log N)$ time.

## Input

A rotated sorted list of unique integers `nums`.

## Output

The minimum integer in `nums`.

## Constraints

- 1 <= len(nums) <= 5 * 10^4
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.

## Examples

**Example 1**

```text
Input:  nums = [3, 4, 5, 1, 2]
Output: 1
```

The original array was [1, 2, 3, 4, 5] rotated 3 times.

**Example 2**

```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2]
Output: 0
```

The minimum element is 0.

**Example 3**

```text
Input:  nums = [11, 13, 15, 17]
Output: 11
```

The array is rotated 4 times (or 0 times), so it remains sorted.

## Function Signature

```python
def find_min(nums: list[int]) -> int:
    """Return the minimum element in the rotated sorted array nums."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Compare `nums[mid]` with `nums[right]`. If `nums[mid] > nums[right]`, the minimum element must be in the right half (`mid + 1` to `right`). Otherwise, it's in the left half including `mid` (`left` to `mid`).

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
