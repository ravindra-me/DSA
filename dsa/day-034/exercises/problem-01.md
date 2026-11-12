# Problem 1: Lomuto Partition Scheme

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Lomuto Partitioning | [Day 34: Quick Sort & Quickselect](../README.md) |

## Problem Statement

Given an array of integers `nums` and a pivot index `pivot_index`, partition the array using the Lomuto partitioning scheme such that all elements less than or equal to the pivot value are placed before elements greater than the pivot value. First move the pivot element to the end of the sub-array, execute the standard Lomuto partition over the entire array, and return the final index of the pivot element after partitioning.

## Input

`nums`: list[int], `pivot_index`: int

## Output

`int`: final index of the pivot element after partitioning

## Constraints

- 1 <= len(nums) <= 10^4
- 0 <= pivot_index < len(nums)
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [3, 8, 2, 5, 1, 4], pivot_index = 5
Output: 3
```

Pivot element is nums[5] = 4. After partitioning, nums becomes [3, 2, 1, 4, 8, 5] (or equivalent valid Lomuto arrangement) and pivot is at index 3.

**Example 2**

```text
Input:  nums = [2, 1], pivot_index = 0
Output: 1
```

Pivot element is 2. Swap to end -> [1, 2]. Partitioning leaves pivot 2 at index 1.

## Function Signature

```python
def partition_lomuto(nums: list[int], pivot_index: int) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Swap pivot to the end of array. Maintain pointer `i = low - 1`. Iterate `j` from `low` to `high - 1`. If `nums[j] <= pivot`, increment `i` and swap `nums[i]` with `nums[j]`. Finally swap `nums[i + 1]` with `nums[high]` and return `i + 1`.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
