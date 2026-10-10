# Problem 1: Single Missing Number

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Linear time vs constant space trade-offs | [Day 1: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Given an array `nums` containing $n$ distinct numbers taken from the inclusive range $[0, n]$, return the only number in the range that is missing from the array.

Your solution must run in $O(n)$ time and use strictly $O(1)$ auxiliary space. You may not modify the input list.

## Input

`nums: list[int]` - a list of $n$ distinct integers from $0$ to $n$

## Output

`int` - the single missing integer

## Constraints

- n == len(nums)
- 1 <= n <= 10^5
- 0 <= nums[i] <= n
- All numbers in nums are unique.

## Examples

**Example 1**

```text
Input:  nums = [3, 0, 1]
Output: 2
```

n = 3 since there are 3 numbers. The range is [0, 3]. 2 is missing.

**Example 2**

```text
Input:  nums = [0, 1]
Output: 2
```

n = 2. Range is [0, 2]. 2 is missing.

**Example 3**

```text
Input:  nums = [1]
Output: 0
```

Edge case: n = 1, range is [0, 1]. 0 is missing.

## Function Signature

```python
def find_missing_number(nums: list[int]) -> int:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Calculate expected total sum or bitwise XOR across the range [0, n] and compare with the actual array sum in a single pass to achieve O(n) time and O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
