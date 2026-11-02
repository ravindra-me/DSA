# Problem 1: Maximum Average Subarray I

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | fixed-size window | [Day 24: Sliding Window](../README.md) |

## Problem Statement

Given an integer array `nums` consisting of $n$ elements, and an integer $k$, find a contiguous subarray whose length is equal to $k$ that has the maximum average value, and return this value.

Any answer with a calculation error less than $10^{-5}$ will be accepted.

## Input

An array of integers `nums: list[int]` and an integer `k: int`.

## Output

A float representing the maximum average value.

## Constraints

- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Examples

**Example 1**

```text
Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75
```

Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75.

**Example 2**

```text
Input:  nums = [5], k = 1
Output: 5.0
```

The only subarray of length 1 is [5], average is 5.0.

## Function Signature

```python
def find_max_average(nums: list[int], k: int) -> float:
    """Finds the maximum average of any contiguous subarray of length k."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a fixed-size sliding window of size k. Track the running sum by adding the new element and subtracting the element leaving the window. Target O(N) time and O(1) extra space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
