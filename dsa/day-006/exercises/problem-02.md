# Problem 2: Single Number from Pairs

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | XOR cancellation property | [Day 6: Bit Manipulation](../README.md) |

## Problem Statement

Given a non-empty array of integers `nums`, every element appears exactly twice except for one unique element which appears exactly once. Find and return that unique element.

You must implement a solution with $O(n)$ time complexity and $O(1)$ auxiliary space.

## Input

A list of integers `nums`.

## Output

The single unique integer.

## Constraints

- 1 <= len(nums) <= 10^5
- len(nums) is odd
- -2^31 <= nums[i] <= 2^31 - 1

## Examples

**Example 1**

```text
Input:  nums = [4, 1, 2, 1, 2]
Output: 4
```

1 and 2 appear twice, 4 appears once.

**Example 2**

```text
Input:  nums = [99]
Output: 99
```

Only one element exists.

## Function Signature

```python
def single_number(nums: list[int]) -> int:
    """Find the single element that appears only once in nums."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

XOR all elements together. Paired numbers cancel out to 0 because x ^ x = 0 and x ^ 0 = x.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
