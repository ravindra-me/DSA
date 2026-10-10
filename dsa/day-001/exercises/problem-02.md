# Problem 2: Sorted Pair Target Sum

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Two-pointer linear scan vs quadratic brute force | [Day 1: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number.

Return the indices of the two numbers, 1-indexed, as a tuple `(index1, index2)` where `index1 < index2`. If no such pair exists, return `None`.

Your solution must operate with $O(n)$ time complexity and $O(1)$ auxiliary space without using a hash table.

## Input

`numbers: list[int]` - a sorted list of integers in non-decreasing order
`target: int` - the desired sum

## Output

`tuple[int, int] | None` - 1-based indices of the two numbers or None

## Constraints

- 2 <= len(numbers) <= 10^5
- -10^9 <= numbers[i] <= 10^9
- -2 * 10^9 <= target <= 2 * 10^9

## Examples

**Example 1**

```text
Input:  numbers = [2, 7, 11, 15], target = 9
Output: (1, 2)
```

The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

**Example 2**

```text
Input:  numbers = [2, 3, 4], target = 6
Output: (1, 3)
```

The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3.

**Example 3**

```text
Input:  numbers = [1, 2, 3], target = 10
Output: None
```

No two numbers add up to 10.

## Function Signature

```python
def two_sum_sorted(numbers: list[int], target: int) -> tuple[int, int] | None:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use two pointers starting at the opposite ends of the sorted array, moving inward based on the comparison of the current sum with the target.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
