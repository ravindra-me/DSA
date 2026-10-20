# Problem 4: Maximum Length of Repeated Subarray

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | dynamic-arrays | [Day 11: Arrays](../README.md) |

## Problem Statement

Given two integer arrays `nums1` and `nums2`, return the maximum length of a subarray (contiguous segment) that appears in both arrays.

Solve this with optimal dynamic programming using space-optimized 1D arrays.

## Input

Two lists of integers `nums1` and `nums2`.

## Output

An integer representing the maximum length of a common contiguous subarray.

## Constraints

- 1 <= len(nums1), len(nums2) <= 1000
- 0 <= nums1[i], nums2[i] <= 100

## Examples

**Example 1**

```text
Input:  nums1 = [1, 2, 3, 2, 1], nums2 = [3, 2, 1, 4, 7]
Output: 3
```

The repeated subarray with maximum length is [3, 2, 1].

**Example 2**

```text
Input:  nums1 = [0, 0, 0, 0, 0], nums2 = [0, 0, 0, 0, 0]
Output: 5
```

The entire array is identical, maximum common length is 5.

## Function Signature

```python
def find_length(nums1: list[int], nums2: list[int]) -> int:
    """Finds the maximum length of a contiguous subarray appearing in both arrays."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use dynamic programming where dp[i][j] represents the length of longest common suffix ending at nums1[i-1] and nums2[j-1]. Optimize space from O(M*N) down to O(N) by traversing backwards across a single 1D array.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
