# Problem 2: Single Number II: Elements Appearing Three Times

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Bit counting modulo 3 / finite-state machine with bitwise logic | [Day 23: Bit Manipulation](../README.md) |

## Problem Statement

Given an integer array `nums` where every element appears exactly three times except for one element which appears exactly once, find that single element.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Input

A list of integers `nums`.

## Output

The single unique integer.

## Constraints

- 1 <= nums.length <= 3 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- Each element in nums appears exactly three times except for one which appears once.

## Examples

**Example 1**

```text
Input:  nums = [2, 2, 3, 2]
Output: 3
```

2 appears 3 times, 3 appears once.

**Example 2**

```text
Input:  nums = [0, 1, 0, 1, 0, 1, 99]
Output: 99
```

0 and 1 appear three times; 99 appears once.

**Example 3**

```text
Input:  nums = [-4]
Output: -4
```

A single negative element is correctly identified.

## Function Signature

```python
def single_number_ii(nums: list[int]) -> int:
    """Find the element that appears once among triple duplicates."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Track bit counts across 32 bits modulo 3, or use two bitmasks (`ones`, `twos`) to simulate a base-3 counter in O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
