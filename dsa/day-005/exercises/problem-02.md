# Problem 2: Pairwise Array Reduction

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Euclidean GCD and LCM across multiple values | [Day 5: Basic Mathematics for DSA](../README.md) |

## Problem Statement

You are given a non-empty array of positive integers `nums`. You must find two values:
1. The Greatest Common Divisor (GCD) of all numbers in the array.
2. The Least Common Multiple (LCM) of all numbers in the array.

Return the answer as a tuple `(overall_gcd, overall_lcm)`.

## Input

`nums: list[int]` - a list of positive integers

## Output

`tuple[int, int]` - a 2-tuple containing `(overall_gcd, overall_lcm)`

## Constraints

- 1 <= len(nums) <= 10^4
- 1 <= nums[i] <= 10^6

## Examples

**Example 1**

```text
Input:  nums = [12, 18, 24]
Output: (6, 72)
```

gcd(12, 18, 24) = 6. lcm(12, 18, 24) = 72.

**Example 2**

```text
Input:  nums = [7]
Output: (7, 7)
```

A single element is its own GCD and LCM.

**Example 3**

```text
Input:  nums = [4, 6, 8, 12]
Output: (2, 24)
```

gcd is 2 and lcm is 24.

## Function Signature

```python
def array_gcd_lcm(nums: list[int]) -> tuple[int, int]:
    """Computes the overall GCD and LCM of an array of positive integers."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use the Euclidean algorithm to compute gcd(a, b). Accumulate the GCD and LCM iteratively across the array using the identity lcm(a, b) = (a // gcd(a, b)) * b.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
