# Problem 4: Longest Consecutive Sequence

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | O(1) lookups and sequence boundary detection with HashSet | [Day 18: HashSet](../README.md) |

## Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in **$O(N)$ time**.

## Input

`nums: list[int]` - an unsorted array of integers.

## Output

`int` - the length of the longest sequence of consecutive integers.

## Constraints

- 0 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [100, 4, 200, 1, 3, 2]
Output: 4
```

The longest consecutive sequence is [1, 2, 3, 4], with length 4.

**Example 2**

```text
Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
```

The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8], with length 9.

**Example 3**

```text
Input:  nums = []
Output: 0
```

Empty list has length 0.

## Function Signature

```python
def longest_consecutive(nums: list[int]) -> int:
    """Return length of longest consecutive elements sequence in O(N) time."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Put all numbers into a HashSet. Only start counting a sequence from numbers that are sequence starts (i.e. x - 1 not in set). Target O(N) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
