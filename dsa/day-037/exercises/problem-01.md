# Problem 1: Sort Colors and Frequencies

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Counting Sort with shift offset and key preservation | [Day 37: Counting, Bucket & Radix Sort](../README.md) |

## Problem Statement

Given a list of integers `nums` where values can be both positive and negative within a relatively small range $[-10^4, 10^4]$, sort the array in non-decreasing order using Counting Sort.

You must return a new sorted list.

## Input

A list of integers `nums`.

## Output

A new list containing the elements of `nums` sorted in ascending order.

## Constraints

- 0 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4

## Examples

**Example 1**

```text
Input:  nums = [4, -1, 2, 0, -1, 3]
Output: [-1, -1, 0, 2, 3, 4]
```

Values are counted and reconstructed in ascending order taking negative numbers into account.

**Example 2**

```text
Input:  nums = []
Output: []
```

An empty array is already sorted.

## Function Signature

```python
def counting_sort(nums: list[int]) -> list[int]:
    """Sorts integers in O(n + k) time using counting sort."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Find min and max, shift elements by min to use non-negative indices in a count array, and rebuild the sorted array in O(n + k) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
