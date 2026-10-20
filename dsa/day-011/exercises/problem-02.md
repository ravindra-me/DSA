# Problem 2: Product of Array Except Self

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | prefix-suffix-products | [Day 11: Arrays](../README.md) |

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in $O(N)$ time and without using the division operation.

## Input

A list of integers `nums`.

## Output

A list of integers `answer` where `answer[i]` is the product of all elements except `nums[i]`.

## Constraints

- 2 <= len(nums) <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

Prefix products combined with suffix products exclude each element individually.

**Example 2**

```text
Input:  nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

Zero handled naturally without division-by-zero errors.

## Function Signature

```python
def product_except_self(nums: list[int]) -> list[int]:
    """Computes product of all array elements except self in O(N) time without division."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Accumulate prefix products into the output array from left to right, then sweep from right to left maintaining a running suffix product accumulator in O(1) extra space.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
