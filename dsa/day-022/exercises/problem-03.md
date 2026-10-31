# Problem 3: Two Sum II - Input Array Is Sorted

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Opposite-direction convergent search on sorted sequences | [Day 22: Two Pointers](../README.md) |

## Problem Statement

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number.

Return the indices of the two numbers, `[index1, index2]`, as a 1-indexed array of length 2 where `1 <= index1 < index2 <= len(numbers)`.

You may not use the same element twice. There is guaranteed to be exactly one valid solution.

## Input

`numbers: list[int]` — sorted list of integers.
`target: int` — target sum to achieve.

## Output

`list[int]` — 1-based indices `[index1, index2]`.

## Constraints

- 2 <= len(numbers) <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -2000 <= target <= 2000
- The tests are generated such that there is exactly one solution.

## Examples

**Example 1**

```text
Input:  numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
```

The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

**Example 2**

```text
Input:  numbers = [2, 3, 4], target = 6
Output: [1, 3]
```

The sum of 2 and 4 is 6. index1 = 1, index2 = 3. Return [1, 3].

**Example 3**

```text
Input:  numbers = [-1, 0], target = -1
Output: [1, 2]
```

The sum of -1 and 0 is -1. Return [1, 2].

## Function Signature

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    """Find 1-based indices of two numbers in sorted list adding up to target."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Initialize pointers at the start and end of the array. Adjust left or right pointer based on whether the current sum is less than or greater than target. Solves in O(n) time and O(1) auxiliary space.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
