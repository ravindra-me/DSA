# Problem 1: Reverse Integer with Overflow Guard

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Digit extraction and arithmetic overflow handling | [Day 5: Basic Mathematics for DSA](../README.md) |

## Problem Statement

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range $[-2^{31}, 2^{31} - 1]$, then return `0`.

You must not convert `x` into a string or list to reverse it; you must extract and construct digits purely through mathematical operations.

## Input

`x: int` - a signed integer

## Output

`int` - the reversed integer, or `0` if it overflows 32-bit signed bounds

## Constraints

- -2^31 <= x <= 2^31 - 1

## Examples

**Example 1**

```text
Input:  x = 123
Output: 321
```

Extracting 3, then 2, then 1 gives 321.

**Example 2**

```text
Input:  x = -120
Output: -21
```

Trailing zeroes are dropped, and negative sign is preserved.

**Example 3**

```text
Input:  x = 1534236469
Output: 0
```

Reversing 1534236469 gives 9646324351, which exceeds 2^31 - 1 = 2147483647, so return 0.

## Function Signature

```python
def reverse_integer(x: int) -> int:
    """Reverses digits of a 32-bit signed integer mathematically."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Extract digits one by one using modulo 10 and integer division by 10. Build the reversed number step-by-step while guarding against 32-bit signed integer limits.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
