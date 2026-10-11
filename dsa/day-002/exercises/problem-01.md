# Problem 1: Remove Element In-Place

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | in-place updates and overwrite pointers | [Day 2: Arrays](../README.md) |

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The relative order of the remaining elements may be changed.

Return the number of elements in `nums` which are not equal to `val` (let this be `k`). After execution, the first `k` elements of `nums` must hold the elements that are not equal to `val`. The elements beyond index `k - 1` do not matter.

## Input

`nums: list[int]`, `val: int`

## Output

`int`: the count $k$ of remaining elements

## Constraints

- 0 <= len(nums) <= 10^5
- 0 <= nums[i] <= 100
- 0 <= val <= 100

## Examples

**Example 1**

```text
Input:  nums = [3, 2, 2, 3], val = 3
Output: 2
```

Your function should return k = 2, with the first two elements of nums containing 2.

**Example 2**

```text
Input:  nums = [], val = 0
Output: 0
```

An empty array contains 0 non-matching elements.

**Example 3**

```text
Input:  nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
Output: 5
```

k = 5, with the first five elements containing [0, 1, 3, 0, 4] in any valid order.

## Function Signature

```python
def remove_element(nums: list[int], val: int) -> int:
    """Remove all occurrences of val in-place and return the count of remaining elements."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a write index pointer while scanning through the array, overwriting target matches in $O(n)$ time and $O(1)$ space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
