# Problem 1: Two Sum Target Difference

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Complement lookup via HashMap | [Day 16: HashMap](../README.md) |

## Problem Statement

Given an integer array `nums` and an integer `diff`, return a pair of indices `(i, j)` such that `nums[i] - nums[j] == diff` and `i != j`. If multiple such pairs exist, return the pair with the smallest `i`, and breaking ties with the smallest `j`. If no such pair exists, return `None`.

## Input

`nums: list[int]` - a list of integers.
`diff: int` - the required difference.

## Output

`tuple[int, int] | None` - the 0-based index pair `(i, j)` or `None`.

## Constraints

- 2 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9
- -10^9 <= diff <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [1, 5, 3, 4, 2], diff = 2
Output: (1, 2)
```

nums[1] - nums[2] = 5 - 3 = 2. Pair of indices is (1, 2).

**Example 2**

```text
Input:  nums = [2, 4, 6], diff = 5
Output: None
```

No two numbers have a difference of 5.

**Example 3**

```text
Input:  nums = [3, 3], diff = 0
Output: (1, 0)
```

nums[1] - nums[0] = 3 - 3 = 0.

## Function Signature

```python
def find_difference_pair(nums: list[int], diff: int) -> tuple[int, int] | None:
    """Find (i, j) such that nums[i] - nums[j] == diff."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Iterate through `nums` while keeping track of seen values and their indices. For each index `i`, check if `nums[i] - diff` or `nums[i] + diff` has appeared, prioritizing the smallest `i` in single-pass or two-pass lookup.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
