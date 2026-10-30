# Problem 1: Immutable Range Sum Query

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | 1D Prefix Sum | [Day 21: Prefix & Suffix Techniques](../README.md) |

## Problem Statement

Given an integer array `nums`, handle multiple queries to calculate the sum of elements between indices `left` and `right` inclusive, where `left <= right`.

Implement the `NumArray` class:
- `__init__(self, nums: list[int])`: Initializes the object with the integer array `nums`.
- `sum_range(self, left: int, right: int) -> int`: Returns the sum of the elements of `nums` between indices `left` and `right` inclusive (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`). Each call to `sum_range` must run in $O(1)$ time.

## Input

`nums`: list of integers for initialization.
`left`, `right`: integers representing 0-indexed boundaries for range query.

## Output

`int`: The sum of the subsegment.

## Constraints

- 1 <= len(nums) <= 10^5
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < len(nums)
- At most 10^5 calls will be made to sum_range.

## Examples

**Example 1**

```text
Input:  nums = [-2, 0, 3, -5, 2, -1]
queries: sum_range(0, 2), sum_range(2, 5), sum_range(0, 5)
Output: 1, -1, -3
```

sum_range(0, 2) -> (-2) + 0 + 3 = 1
sum_range(2, 5) -> 3 + (-5) + 2 + (-1) = -1
sum_range(0, 5) -> (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

**Example 2**

```text
Input:  nums = [5]
queries: sum_range(0, 0)
Output: 5
```

Single-element array query over [0, 0] returns 5.

## Function Signature

```python
class NumArray:
    def __init__(self, nums: list[int]) -> None:
        ...

    def sum_range(self, left: int, right: int) -> int:
        ...
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Precompute an array of cumulative sums with a padded zero at index 0 in O(N) time during initialization, then compute each range query as prefix[right + 1] - prefix[left] in O(1) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
