# Problem 3: Maximum Subarray Min-Product

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Previous/Next Smaller Element with Prefix Sums | [Day 35: Monotonic Stack](../README.md) |

## Problem Statement

The **min-product** of a non-empty subarray is defined as the **minimum value** in the subarray multiplied by the **sum** of the subarray. Given an array of positive integers `nums`, return the maximum min-product among all possible non-empty subarrays. Since the answer may be large, return it modulo $10^9 + 7$.

## Input

nums: list[int]

## Output

int

## Constraints

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^7

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 3, 2]
Output: 14
```

Subarray [2, 3, 2] has minimum 2 and sum (2+3+2)=7. Min-product = 2 * 7 = 14.

**Example 2**

```text
Input:  nums = [2, 3, 3, 1, 2]
Output: 18
```

Subarray [3, 3] has minimum 3 and sum 6. Min-product = 3 * 6 = 18.

## Function Signature

```python
def max_min_product(nums: list[int]) -> int:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Find for each element the contiguous range $[L, R]$ where $nums[i]$ is the minimum using a monotonic stack. Compute subarray sum in $O(1)$ using prefix sums. Calculate maximum min-product before applying modulo $10^9+7$.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
