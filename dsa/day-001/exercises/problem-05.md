# Problem 5: First Missing Positive

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | In-place cyclic indexing to achieve O(n) time and O(1) auxiliary space | [Day 1: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Given an unsorted integer array `nums`, return the smallest positive integer that is not present in `nums`.

You must implement an algorithm that runs in $O(n)$ time and uses strictly $O(1)$ auxiliary space (i.e. without allocating new data structures proportional to $n$).

## Input

`nums: list[int]` - an unsorted list of integers

## Output

`int` - the smallest positive integer missing from the list

## Constraints

- 1 <= len(nums) <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 0]
Output: 3
```

Numbers 1 and 2 are present, so the smallest missing positive integer is 3.

**Example 2**

```text
Input:  nums = [3, 4, -1, 1]
Output: 2
```

1 is in the array, but 2 is missing.

**Example 3**

```text
Input:  nums = [7, 8, 9, 11, 12]
Output: 1
```

1 is missing from the array.

**Example 4**

```text
Input:  nums = [1]
Output: 2
```

Edge case: 1 is present, the next smallest positive is 2.

## Function Signature

```python
def first_missing_positive(nums: list[int]) -> int:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Reposition elements in-place using bucket/cyclic sort so that positive integer x is placed at index x - 1, then identify the first mismatched position in a second pass.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
