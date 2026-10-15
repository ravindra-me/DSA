# Solution 3: Reverse Bits of a 32-bit Integer

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Bit extraction and bit assembly with shift operators

## Approach

Iterate across all 32 bit positions, extracting the least significant bit of the input integer `n` with `n & 1`, shifting the accumulated result left by one position, and appending the extracted bit. Then right-shift `n` by one.

## Thought Process

A naive string conversion approach (`bin(n)`, padding with zeros to 32 bits, reversing the string, and converting back via `int(..., 2)`) works but allocates intermediate strings and is non-idiomatic for bit manipulation tasks.

Instead, we can construct the reversed number directly using bitwise operators. In 32 iterations, we make room for the next reversed bit by left-shifting `result` by 1 (`result << 1`), mask the current least significant bit of `n` using `n & 1`, and bitwise-OR it into `result`. Finally, we right-shift `n` by 1 (`n >> 1`) to inspect the next bit on the next iteration.

Alternatively, divide-and-conquer byte/bit swapping (masking and shifting 16, 8, 4, 2, and 1 bits) can achieve $O(1)$ operations without a loop, but a fixed 32-iteration loop is extremely clear, bug-free, and runs in constant time $O(1)$ as well.

## Algorithm

1. Initialize `result = 0`.
2. Loop `_` from 0 to 31 (for a total of 32 bits):
3. Shift `result` to the left by 1 bit: `result = (result << 1) | (n & 1)`.
4. Shift `n` to the right by 1 bit: `n >>= 1`.
5. Return `result`.

## Complexity Analysis

- **Time:** O(1) because the loop executes exactly 32 times regardless of the value of `n`.
- **Space:** O(1) auxiliary space as only a single integer accumulator is maintained.

## Edge Cases

- n = 0: All 32 bits are 0, loop naturally maintains result as 0.
- n = 2^32 - 1 (all 1s, 4294967295): All 32 bits are 1, reversal produces the exact same number 4294967295.
- n = 1: Only the lowest bit is set, which gets shifted 31 times into the highest bit position (yielding 2^31 = 2147483648).
- n = 2^31: Only the highest bit is set, which ends up at the lowest bit position (yielding 1).

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def reverse_bits(n: int) -> int:
    """Reverse the bits of a 32-bit unsigned integer."""
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```
