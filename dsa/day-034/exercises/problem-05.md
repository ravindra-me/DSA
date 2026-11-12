# Problem 5: Wiggle Sort II

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | 3-Way Partitioning with Index Mapping | [Day 34: Quick Sort & Quickselect](../README.md) |

## Problem Statement

Given an integer array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`. You may assume the input array always has a valid answer. Perform the reordering in $O(N)$ time complexity and $O(1)$ extra space.

## Input

`nums`: list[int]

## Output

`None`: Modify nums in-place.

## Constraints

- 1 <= len(nums) <= 10^5
- 0 <= nums[i] <= 5000
- A valid answer is guaranteed to exist.

## Examples

**Example 1**

```text
Input:  nums = [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
```

One valid output is [1, 6, 1, 5, 1, 4] or [1, 5, 1, 6, 1, 4].

**Example 2**

```text
Input:  nums = [1, 3, 2, 2, 3, 1]
Output: [2, 3, 1, 3, 1, 2]
```

Valid wiggle pattern where nums[0] < nums[1] > nums[2] < nums[3]...

## Function Signature

```python
def wiggle_sort(nums: list[int]) -> None:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

1. Find the median of the array in $O(N)$ expected time using Quickselect.
2. Use a virtual index mapping function `idx(i) = (1 + 2*i) % (N | 1)` to map original indices to odd indices first, then even indices.
3. Perform 3-way Dutch National Flag partitioning around the median using the virtual index mapping.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
