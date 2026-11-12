# Problem 2: Kth Smallest Element (Quickselect)

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Quickselect | [Day 34: Quick Sort & Quickselect](../README.md) |

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k`-th smallest element in the array (1-indexed). You must solve this in $O(N)$ average time complexity using the Quickselect algorithm.

## Input

`nums`: list[int], `k`: int

## Output

`int`: the k-th smallest element

## Constraints

- 1 <= k <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 2
```

Sorted array is [1, 2, 3, 4, 5, 6]. The 2nd smallest element is 2.

**Example 2**

```text
Input:  nums = [7, 10, 4, 3, 20, 15], k = 4
Output: 10
```

Sorted array is [3, 4, 7, 10, 15, 20]. The 4th smallest element is 10.

## Function Signature

```python
def find_kth_smallest(nums: list[int], k: int) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use Quickselect with randomized pivot selection. Partition the current search range `[low, high]`. Compare the pivot's position with `k - 1` to decide whether to search left or right half.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
