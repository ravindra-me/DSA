# Problem 1: Subarray Product Less Than K

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Two Pointers / Sliding Window amortized complexity analysis | [Day 8: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Given an array of positive integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

Your solution must run in strictly $O(N)$ time, despite the nested movement of pointers.

## Input

`nums: list[int]`, `k: int`

## Output

`int`: count of valid contiguous subarrays

## Constraints

- 1 <= len(nums) <= 3 * 10^4
- 1 <= nums[i] <= 1000
- 0 <= k <= 10^6

## Examples

**Example 1**

```text
Input:  nums = [10, 5, 2, 6], k = 100
Output: 8
```

The 8 subarrays with product < 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].

**Example 2**

```text
Input:  nums = [1, 2, 3], k = 0
Output: 0
```

Since all elements are positive, no product can be strictly less than 0.

## Function Signature

```python
def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a sliding window with two pointers where the left pointer advances only as needed. Note that each pointer moves at most N times total, achieving O(N) amortized time.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
