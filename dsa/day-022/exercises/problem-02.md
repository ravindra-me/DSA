# Problem 2: Remove Duplicates from Sorted Array II

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Same-direction read/write pointers with frequency thresholding | [Day 22: Two Pointers](../README.md) |

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove duplicates in-place such that each unique element appears **at most twice**. The relative order of the elements should be kept the same.

You must modify the array in-place such that the first `k` elements of `nums` contain the final result. Return the integer `k` (the number of valid elements).

Elements beyond index `k - 1` do not matter.

## Input

`nums: list[int]` — sorted list of integers in non-decreasing order.

## Output

`int` — the count `k` of retained elements. In addition, the first `k` elements of `nums` must hold the retained elements.

## Constraints

- 1 <= len(nums) <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.

## Examples

**Example 1**

```text
Input:  nums = [1, 1, 1, 2, 2, 3]
Output: 5
```

nums becomes [1, 1, 2, 2, 3, ...]. The first 5 elements are retained.

**Example 2**

```text
Input:  nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
Output: 7
```

nums becomes [0, 0, 1, 1, 2, 3, 3, ...].

**Example 3**

```text
Input:  nums = [1]
Output: 1
```

Single-element array remains unchanged.

## Function Signature

```python
def remove_duplicates_at_most_two(nums: list[int]) -> int:
    """Modify nums in-place so each element appears at most twice. Return new length."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a write pointer starting at index 2 (or 0 for general cases). A candidate at read index is valid if it is greater than the element at write - 2. Operates in O(n) time and O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
