# Problem 4: Single Number III (Two Unique Elements)

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Partitioning elements by distinguishing bit using lowest set bit | [Day 6: Bit Manipulation](../README.md) |

## Problem Statement

Given an integer array `nums` in which exactly two elements appear only once and all the other elements appear exactly twice, find the two elements that appear only once.

Return the two elements sorted in ascending order `[a, b]` (where $a < b$).

You must design an algorithm that runs in $O(n)$ time and uses only $O(1)$ auxiliary space.

## Input

A list of integers `nums`.

## Output

A list of two integers `[a, b]` with `a < b`.

## Constraints

- 2 <= len(nums) <= 10^5
- len(nums) is even
- -2^31 <= nums[i] <= 2^31 - 1

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 1, 3, 2, 5]
Output: [3, 5]
```

3 and 5 appear once, other elements appear twice.

**Example 2**

```text
Input:  nums = [-1, 0]
Output: [-1, 0]
```

Both elements appear once.

## Function Signature

```python
def single_number_two_uniques(nums: list[int]) -> list[int]:
    """Find the two unique numbers in nums, returned in ascending order."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

XOR all elements to get `x ^ y`. Find the lowest set bit of `x ^ y` using `diff & (-diff)` to partition the array into two groups, then XOR each group separately.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
