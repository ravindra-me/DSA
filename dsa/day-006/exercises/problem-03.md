# Problem 3: Reverse Bits of a 32-bit Integer

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Bit extraction and bit assembly with shift operators | [Day 6: Bit Manipulation](../README.md) |

## Problem Statement

Reverse the bits of a given 32-bit unsigned integer `n` and return the resulting integer.

For example, the binary representation of `43261596` is `00000010100101000001111010011100`. Reversing these bits gives `00111001011110000010100101000000`, which equals `964176192`.

## Input

A non-negative integer `n` (0 <= n < 2^32).

## Output

An integer representing the bit-reversed 32-bit unsigned number.

## Constraints

- 0 <= n < 2^32

## Examples

**Example 1**

```text
Input:  n = 43261596
Output: 964176192
```

The 32-bit binary pattern is reversed.

**Example 2**

```text
Input:  n = 0
Output: 0
```

All 32 bits are 0, reversal is still 0.

**Example 3**

```text
Input:  n = 1
Output: 2147483648
```

1 is bit 0 set. When reversed, bit 31 is set, which is 2^31.

## Function Signature

```python
def reverse_bits(n: int) -> int:
    """Reverse the bits of a 32-bit unsigned integer."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Iterate across 32 bit positions, extracting the lowest bit with `n & 1`, shifting the result left, and shifting `n` right.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
