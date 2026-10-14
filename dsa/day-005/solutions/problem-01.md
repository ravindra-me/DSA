# Solution 1: Reverse Integer with Overflow Guard

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Digit extraction and arithmetic overflow handling

## Approach

Repeatedly extract the least significant digit of `|x|` using modulo 10 and construct the reversed integer by multiplying the running result by 10 and adding the extracted digit. To guard against 32-bit signed integer overflow ($[-2^{31}, 2^{31}-1]$), check whether the reversed magnitude would exceed the bounds before applying the sign.

## Thought Process

A common string-based approach converts `x` to a string, reverses it, converts back to an integer, and checks bounds. However, the problem explicitly forbids string or sequence conversions. Instead, we use base-10 arithmetic operations: `digit = n % 10` and `n = n // 10`.

Because Python handles arbitrarily large integers automatically, we can either check for overflow before multiplying by 10 (as strictly required in C/C++ without 64-bit integers) or check against $2^{31} - 1$ and $-2^{31}$ during/after reversal. To simulate a strict 32-bit overflow guard purely mathematically, we can track the sign, work with `abs(x)`, and ensure the value never exceeds $2^{31} - 1$ (or $2^{31}$ for negative numbers). If it does, we immediately return 0.

## Algorithm

1. Identify the sign of `x`: if `x < 0`, set `sign = -1`, else `sign = 1`.
2. Work with the absolute value `n = abs(x)` and initialize `reversed_num = 0`.
3. Define 32-bit integer limits: `MAX_INT = 2**31 - 1` (2147483647) and `MIN_INT = -2**31` (-2147483648).
4. Loop while `n > 0`:
  a. Extract the last digit: `digit = n % 10`.
  b. Check overflow before shifting: if `sign == 1` and `reversed_num > (MAX_INT - digit) // 10`, return 0.
  c. If `sign == -1` and `reversed_num > (-MIN_INT - digit) // 10`, return 0.
  d. Update `reversed_num = reversed_num * 10 + digit`.
  e. Remove the last digit: `n //= 10`.
5. Return `sign * reversed_num`.

## Complexity Analysis

- **Time:** O(log10(|x|)) - A 32-bit integer has at most 10 decimal digits, so the loop executes at most 10 times, which is O(1) in practice.
- **Space:** O(1) - Only a few integer variables are maintained in memory.

## Edge Cases

- Zero: `x = 0` terminates the loop immediately and returns 0.
- Single-digit numbers (positive and negative): Loop runs once and correctly returns `x`.
- Trailing zeroes (e.g. 120): The first extracted digit is 0, which becomes a leading zero and is naturally swallowed mathematically.
- Overflow: Values like 1534236469 whose reversed forms exceed 2^31 - 1 return 0.
- Minimum 32-bit integer (-2^31 = -2147483648): Handled without overflow, reverses to a value exceeding bounds and returns 0.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def reverse_integer(x: int) -> int:
    """Reverses digits of a 32-bit signed integer mathematically."""
    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    sign = -1 if x < 0 else 1
    n = abs(x)
    reversed_num = 0
    max_limit = -INT_MIN if sign == -1 else INT_MAX

    while n > 0:
        digit = n % 10
        if reversed_num > (max_limit - digit) // 10:
            return 0
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return sign * reversed_num
```
