# Problem 5: First Missing Positive

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | index-as-hash-key / cycle placement in-place | [Day 2: Arrays](../README.md) |

## Problem Statement

Given an unsorted integer array `nums`, return the smallest positive integer that is **not present** in `nums`.

You must implement an algorithm that runs in $O(n)$ time and uses $O(1)$ auxiliary space.

## Input

`nums: list[int]`

## Output

`int`: smallest missing positive integer

## Constraints

- 1 <= len(nums) <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 0]
Output: 3
```

Numbers 1 and 2 are present; 3 is the smallest missing positive integer.

**Example 2**

```text
Input:  nums = [3, 4, -1, 1]
Output: 2
```

1 is present, but 2 is missing.

**Example 3**

```text
Input:  nums = [7, 8, 9, 11, 12]
Output: 1
```

The smallest positive integer 1 is missing.

## Function Signature

```python
def first_missing_positive(nums: list[int]) -> int:
    """Return the smallest missing positive integer in O(n) time and O(1) space."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use the array itself as a hash table: swap each valid number x into its matching index (x - 1) in $O(n)$ time until every element is in its rightful place.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
