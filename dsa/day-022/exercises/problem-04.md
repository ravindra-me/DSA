# Problem 4: Sort Colors (Dutch National Flag)

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Three-way partitioning using multi-pointer invariants | [Day 22: Two Pointers](../README.md) |

## Problem Statement

Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem in-place without using Python's library `sort` function and using only a single pass with constant extra space.

## Input

`nums: list[int]` — list containing only values 0, 1, or 2.

## Output

`None` — modify `nums` in-place.

## Constraints

- 1 <= len(nums) <= 300
- nums[i] is either 0, 1, or 2.

## Examples

**Example 1**

```text
Input:  nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
```

Array sorted in-place.

**Example 2**

```text
Input:  nums = [2, 0, 1]
Output: [0, 1, 2]
```

Array sorted in-place.

**Example 3**

```text
Input:  nums = [0]
Output: [0]
```

Single element array is already sorted.

## Function Signature

```python
def sort_colors(nums: list[int]) -> None:
    """Sort nums in-place containing 0s, 1s, and 2s using Dutch National Flag algorithm."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain three pointers: low, mid, and high. Partition the array into regions <1, ==1, and >1 in a single pass in O(n) time and O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
