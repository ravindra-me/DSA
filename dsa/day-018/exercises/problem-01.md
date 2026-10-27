# Problem 1: Contains Duplicate

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Basic membership testing and seen-before pattern | [Day 18: HashSet](../README.md) |

## Problem Statement

Given an integer array `nums`, determine if any value appears at least twice in the array. Return `True` if any value appears at least twice, and `False` if every element is distinct.

## Input

`nums: list[int]` - a list of integers.

## Output

`bool` - `True` if duplicates exist, `False` otherwise.

## Constraints

- 1 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 3, 1]
Output: True
```

1 appears at index 0 and index 3.

**Example 2**

```text
Input:  nums = [1, 2, 3, 4]
Output: False
```

All elements are distinct.

**Example 3**

```text
Input:  nums = [42]
Output: False
```

A single-element array has no duplicates.

## Function Signature

```python
def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any value appears at least twice in nums."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Iterate through the array while tracking seen elements in a set. Target O(N) time and O(N) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
