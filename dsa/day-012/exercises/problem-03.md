# Problem 3: Next Greater Element II (Circular Array)

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Monotonic stack on circular / wrapped arrays | [Day 12: Monotonic Stack](../README.md) |

## Problem Statement

Given a circular integer array `nums` (i.e., the next element of `nums[len(nums) - 1]` is `nums[0]`), return the next greater number for every element in `nums`.

The next greater number of an element `x` is the first element greater than `x` traversed in clockwise order. If it does not exist, return `-1` for this number.

## Input

`nums: list[int]` - circular list of integers.

## Output

`list[int]` - list where each entry is the next greater circular element.

## Constraints

- 1 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 1]
Output: [2, -1, 2]
```

The first 1's next greater is 2. 2 has no greater element. The second 1 circles around to find 2.

**Example 2**

```text
Input:  nums = [5, 4, 3, 2, 1]
Output: [-1, 5, 5, 5, 5]
```

5 has no greater element. All others wrap around to find 5.

## Function Signature

```python
def next_greater_elements(nums: list[int]) -> list[int]:
    """Find the next greater circular element for each position."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Iterate twice over the array ($2n$ steps) using modulo indexing `i % n` with a monotonic decreasing stack of indices. Only push indices on the first pass. Target $O(n)$ time and $O(n)$ space.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
