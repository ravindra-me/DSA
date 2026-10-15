# Solution 1: Power of Two and Hamming Weight

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Power of two checking and bit counting using bitwise operations

## Approach

A positive integer is a power of two if and only if it has exactly one set bit, which can be checked in $O(1)$ time via `n > 0 and (n & (n - 1)) == 0`. To count set bits (Hamming weight) without converting to a string, we can use Brian Kernighan's algorithm (`n &= n - 1`), which iterates once per set bit, or Python's built-in `int.bit_count()`.

## Thought Process

When examining powers of two in binary ($1, 2, 4, 8, \dots = 1_2, 10_2, 100_2, 1000_2$), each consists of a single `1` followed by zeroes. Subtracting 1 flips the lowest set bit and sets all lower zero bits to 1 (e.g., $1000_2 - 1 = 0111_2$). Performing a bitwise AND between `n` and `n - 1` clears the lowest set bit: `n & (n - 1) == 0` for any single-bit positive number. Note that `n = 0` also satisfies `0 & -1 == 0`, but 0 is not a power of two, so we must explicitly ensure `n > 0`.

For counting set bits, iterating bit by bit takes 31 iterations. Instead, Brian Kernighan's trick repeatedly executes `n &= n - 1` until `n` becomes 0, executing in time proportional only to the number of set bits (at most 31). Alternatively, Python 3.10+ provides `n.bit_count()`, which is an efficient C-level population count operation. Using `bit_count()` (or Kernighan's loop) combined with the bitwise power-of-two check achieves $O(1)$ time and $O(1)$ space.

## Algorithm

1. Check if `n > 0 and (n & (n - 1)) == 0` to determine `is_power_of_two`.
2. Compute `count_set_bits` using Brian Kernighan's bit-clearing loop: initialize `count = 0`, repeatedly set `temp &= temp - 1` and increment `count` until `temp` reaches 0 (or use `n.bit_count()`).
3. Return the tuple `(is_power_of_two, count_set_bits)`.

## Complexity Analysis

- **Time:** O(k) where k is the number of set bits (at most 31 for 32-bit integers), or effectively O(1).
- **Space:** O(1) auxiliary space as only a few scalar variables are used.

## Edge Cases

- n = 0: Not a power of two, set bit count is 0.
- n = 1: Smallest power of two (2^0), set bit count is 1.
- n = 2^31 - 1: Maximum constraint value, has 31 set bits, not a power of two.
- Consecutive powers of two (e.g. 2, 4, 1024, 2^30).

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def analyze_bits(n: int) -> tuple[bool, int]:
    """Return whether n is a power of two and its number of set bits."""
    is_power_of_two = n > 0 and (n & (n - 1)) == 0
    
    # Count set bits using Brian Kernighan's algorithm
    count = 0
    current = n
    while current > 0:
        current &= current - 1
        count += 1
        
    return is_power_of_two, count
```
