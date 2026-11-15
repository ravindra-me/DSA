# Problem 5: Maximum Gap in Linear Time

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Pigeonhole Principle with Bucket Partitioning | [Day 37: Counting, Bucket & Radix Sort](../README.md) |

## Problem Statement

Given an integer array `nums`, return the maximum difference between two successive elements in its sorted form. If the array contains less than 2 elements, return `0`.

You must solve this in $O(n)$ time and $O(n)$ extra space without using comparison sorts ($O(n \log n)$ is unacceptable).

## Input

A list of integers `nums`.

## Output

An integer representing the maximum gap between adjacent elements in sorted order.

## Constraints

- 1 <= len(nums) <= 10^5
- 0 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [3, 6, 9, 1]
Output: 3
```

Sorted form is [1, 3, 6, 9]. The maximum difference is between (3, 6) or (6, 9), which is 3.

**Example 2**

```text
Input:  nums = [10]
Output: 0
```

Array contains less than 2 elements, so return 0.

**Example 3**

```text
Input:  nums = [1, 1, 1, 1]
Output: 0
```

All elements are equal, so the successive difference is 0.

## Function Signature

```python
def maximum_gap(nums: list[int]) -> int:
    """Finds the maximum gap in sorted order in linear O(n) time."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use the bucket principle: bucket size = max(1, (max_val - min_val) // (n - 1)). Track only min and max in each bucket. The max gap must occur between the maximum of one bucket and the minimum of the next non-empty bucket.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
