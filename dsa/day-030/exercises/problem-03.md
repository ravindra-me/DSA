# Problem 3: Split Array Largest Sum

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Minimize the maximum subarray sum (partitioning) | [Day 30: Binary Search on the Answer](../README.md) |

## Problem Statement

Given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty contiguous subarrays such that the largest sum of any subarray is **minimized**.

Return the minimized largest sum.

## Input

`nums: list[int]`, `k: int`

## Output

`int`: minimized largest subarray sum

## Constraints

- 1 <= len(nums) <= 10^5
- 1 <= k <= min(50, len(nums))
- 0 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [7, 2, 5, 10, 8], k = 2
Output: 18
```

Split into [7, 2, 5] (sum 14) and [10, 8] (sum 18). The maximum sum is 18.

**Example 2**

```text
Input:  nums = [1, 4, 4], k = 3
Output: 4
```

Split into [1], [4], and [4]. The maximum sum is 4.

## Function Signature

```python
def split_array(nums: list[int], k: int) -> int:
    """Return the minimized largest sum among k contiguous subarrays."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Binary search on the maximum subarray sum in range $[\max(\text{nums}), \sum(\text{nums})]$. Feasibility check uses a greedy running sum to count partitions.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
