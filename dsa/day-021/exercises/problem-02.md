# Problem 2: Product of Array Except Self

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Prefix-Suffix Accumulation | [Day 21: Prefix & Suffix Techniques](../README.md) |

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 64-bit integer.

You must write an algorithm that runs in $O(N)$ time and without using the division operator.

## Input

`nums`: list of integers where `2 <= len(nums) <= 10^5`.

## Output

`list[int]`: list of products of all elements except each corresponding index.

## Constraints

- 2 <= len(nums) <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix fits in a 64-bit integer.
- You must not use division.

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

For index 0: 2*3*4 = 24. For index 1: 1*3*4 = 12. For index 2: 1*2*4 = 8. For index 3: 1*2*3 = 6.

**Example 2**

```text
Input:  nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

Index 2 excludes 0, product of remaining is (-1)*1*(-3)*3 = 9. All other indices include 0, so their product is 0.

## Function Signature

```python
def product_except_self(nums: list[int]) -> list[int]:
    """Compute product of all elements except nums[i] without division."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Construct running prefix products from left to right, then sweep from right to left maintaining a running suffix product to compute each result without division in O(N) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
