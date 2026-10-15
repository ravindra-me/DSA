# Problem 1: Power of Two and Hamming Weight

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Power of two checking and bit counting using bitwise operations | [Day 6: Bit Manipulation](../README.md) |

## Problem Statement

Given a non-negative integer `n`, return a tuple `(is_power_of_two, count_set_bits)` where:
- `is_power_of_two` is a boolean indicating whether `n` is an integer power of two ($2^k$ for some integer $k \ge 0$).
- `count_set_bits` is the number of set bits (1s) in the binary representation of `n`.

You must not convert `n` to a string.

## Input

An integer `n`.

## Output

A tuple `(bool, int)`.

## Constraints

- 0 <= n <= 2^31 - 1

## Examples

**Example 1**

```text
Input:  n = 16
Output: (True, 1)
```

16 in binary is 10000_2, which is 2^4 and has exactly 1 set bit.

**Example 2**

```text
Input:  n = 0
Output: (False, 0)
```

0 is not a power of two and has 0 set bits.

**Example 3**

```text
Input:  n = 11
Output: (False, 3)
```

11 in binary is 1011_2, not a power of two, has 3 set bits.

## Function Signature

```python
def analyze_bits(n: int) -> tuple[bool, int]:
    """Return whether n is a power of two and its number of set bits."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use `n & (n - 1)` for checking powers of two and Brian Kernighan's algorithm to count set bits in O(k) time where k is the number of set bits.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
