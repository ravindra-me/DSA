# Problem 2: Majority Element Identifier

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | majority element counting and Boyer-Moore voting | [Day 19: Frequency Counting](../README.md) |

## Problem Statement

Given an array `nums` of size $n$, return the majority element.

The majority element is the element that appears strictly more than $\lfloor n / 2 \rfloor$ times. You may assume that the majority element always exists in the array.

## Input

A list of integers `nums` of length $n \ge 1$.

## Output

An integer representing the majority element.

## Constraints

- 1 <= len(nums) <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9
- The majority element is guaranteed to exist.

## Examples

**Example 1**

```text
Input:  nums = [3, 2, 3]
Output: 3
```

3 appears 2 times, which is > 3 // 2 = 1.

**Example 2**

```text
Input:  nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
```

2 appears 4 times, which is > 7 // 2 = 3.

**Example 3**

```text
Input:  nums = [1]
Output: 1
```

Single-element array always has that element as the majority.

## Function Signature

```python
def majority_element(nums: list[int]) -> int:
    """Find and return the majority element (> n // 2 times)."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a hash map counter in O(n) time, or use Boyer-Moore Voting Algorithm to achieve O(n) time with O(1) extra space.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
