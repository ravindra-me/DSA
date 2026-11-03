# Problem 2: Sentinel Target Search

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Sentinel search technique to eliminate bound checks | [Day 25: Linear Search](../README.md) |

## Problem Statement

Implement linear search using the **sentinel technique**. Given a list of integers `nums` and an integer `target`, temporarily place `target` as a sentinel at the end of the collection (or modify access) so that the loop condition does not need to check array bounds. Return `True` if `target` originally existed in `nums`, and `False` otherwise. You must restore `nums` to its original state before returning.

## Input

A list of integers `nums` and an integer `target`.

## Output

A boolean indicating whether target was in original `nums`.

## Constraints

- 0 <= len(nums) <= 10^5
- -10^9 <= nums[i], target <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [10, 20, 30], target = 20
Output: True
```

20 exists in the list.

**Example 2**

```text
Input:  nums = [], target = 5
Output: False
```

Empty list contains no elements.

## Function Signature

```python
def sentinel_search(nums: list[int], target: int) -> bool:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Handle empty list edge case. Append target as sentinel, scan with a simple while loop matching target, pop sentinel, then check index. Target complexity: O(n) time, O(1) auxiliary space.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
