# Problem 1: Subsets Generation via Bitmasks

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Power set generation using binary integers as inclusion/exclusion masks | [Day 23: Bit Manipulation](../README.md) |

## Problem Statement

Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. You must generate subsets iteratively by treating integers from `0` to `2^n - 1` as bitmasks. Return the subsets sorted by size ascending; for subsets of equal size, maintain lexicographical order according to their original array indices.

## Input

A list of unique integers `nums`.

## Output

A list of lists of integers representing all subsets, ordered by size and then index order.

## Constraints

- 1 <= nums.length <= 15
- -100 <= nums[i] <= 100
- All elements of nums are unique.

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

Masks range from 000 to 111. Grouped by number of set bits (size), then order.

**Example 2**

```text
Input:  nums = [0]
Output: [[], [0]]
```

2^1 = 2 subsets.

## Function Signature

```python
def subsets_bitmask(nums: list[int]) -> list[list[int]]:
    """Return all subsets generated via bit manipulation."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Iterate through masks from 0 to 2^n - 1, using bit tests `(mask >> i) & 1` to construct each subset, then sort by length.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
