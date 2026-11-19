# Problem 2: Strict In-Place Zero Partition

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | In-place array partitioning with strict O(1) auxiliary space | [Day 41: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Given an integer array `nums`, rearrange its elements in-place such that all non-zero integers appear before all zero integers, while preserving the original relative order of the non-zero integers. In addition, you must return the count of non-zero integers.

To satisfy strict $O(1)$ auxiliary space, you cannot allocate any new list, set, or other collections. All modifications must be made directly on `nums` in $O(n)$ time.

## Input

A list of integers `nums`.

## Output

An integer representing the count of non-zero elements. (The list `nums` must also be modified in-place).

## Constraints

- 1 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [0, 1, 0, 3, 12]
Output: 3
```

nums becomes [1, 3, 12, 0, 0]. Count of non-zeros is 3.

**Example 2**

```text
Input:  nums = [0, 0, 0]
Output: 0
```

nums remains [0, 0, 0]. Count is 0.

## Function Signature

```python
def stable_zero_partition(nums: list[int]) -> int:
    """Partition zeros to the back in-place preserving relative order. Return non-zero count."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a two-pointer approach where a write-pointer tracks the target position for the next non-zero element, followed by zero-filling the tail.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
