# Problem 2: Search Insert Position

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Finding lower-bound insertion point in a sorted array | [Day 27: Binary Search](../README.md) |

## Problem Statement

Given a sorted array of distinct integers `nums` and a target value `target`, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with $O(\log n)$ runtime complexity.

## Input

A sorted list of distinct integers `nums` and an integer `target`.

## Output

An integer representing the target's index or its insertion position.

## Constraints

- 1 <= len(nums) <= 10^4
- -10^4 <= nums[i], target <= 10^4
- nums contains distinct values sorted in ascending order.

## Examples

**Example 1**

```text
Input:  nums = [1, 3, 5, 6], target = 5
Output: 2
```

5 is found at index 2.

**Example 2**

```text
Input:  nums = [1, 3, 5, 6], target = 2
Output: 1
```

2 should be inserted at index 1 to maintain sorted order.

**Example 3**

```text
Input:  nums = [1, 3, 5, 6], target = 7
Output: 4
```

7 should be inserted at the end (index 4).

## Function Signature

```python
def search_insert(nums: list[int], target: int) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain bounds such that `low` shifts right whenever `nums[mid] < target`. When loop ends (`low > high`), `low` will be the exact insertion index.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
