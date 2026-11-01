# Solution 2: Single Number II: Elements Appearing Three Times

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Medium | **Concept:** Bit counting modulo 3 / finite-state machine with bitwise logic

## Approach

We can model the count of each bit modulo 3 using a digital finite state machine with two bitmasks, `ones` and `twos`. `ones` tracks bits that have appeared $1 \pmod 3$ times, and `twos` tracks bits that have appeared $2 \pmod 3$ times. When a bit appears a third time, both flags reset to 0.

## Thought Process

A hash map (counting occurrences) achieves $O(N)$ time but requires $O(N)$ space, violating the $O(1)$ space constraint. Sorting takes $O(N \log N)$ time, violating linear time.

To achieve both $O(N)$ time and $O(1)$ space, we examine bits individually across all numbers. For every bit position $i$, if we sum the $i$-th bit across all numbers, numbers appearing three times contribute a multiple of 3 to the sum ($3 \times 0 = 0$ or $3 \times 1 = 3$). The unique number appears once, contributing either 0 or 1. Hence, `(sum of bit i) % 3` directly reveals the $i$-th bit of the unique number.

Instead of looping through all 32 bits explicitly (which also requires handling 32-bit signed two's complement in Python), we can process all 32 bits simultaneously using bitwise logic. We need a state counter modulo 3 for each bit:
- State 0: bit appeared 0 times (or $3k$ times) -> `ones = 0, twos = 0`
- State 1: bit appeared 1 time (or $3k + 1$ times) -> `ones = 1, twos = 0`
- State 2: bit appeared 2 times (or $3k + 2$ times) -> `ones = 0, twos = 1`

For each number `num`:
1. Update `ones = (ones ^ num) & ~twos`: a bit enters `ones` if toggled by `num`, provided it is not in `twos`.
2. Update `twos = (twos ^ num) & ~ones`: a bit enters `twos` if toggled by `num` while not in the new `ones`.

At the end of the array, `ones` holds the bits that appeared once modulo 3, which is precisely the unique number (including negative numbers in two's complement representation if needed, though in Python this bitwise transition naturally maintains the integer's sign when starting from 0).

## Algorithm

1. Initialize two variables `ones = 0` and `twos = 0` representing bit counters modulo 3.
2. Iterate through each integer `num` in `nums`.
3. Update `ones = (ones ^ num) & ~twos`. This adds bits from `num` to `ones` if they are not already in `twos`, or clears them if they were already in `ones`.
4. Update `twos = (twos ^ num) & ~ones`. This moves bits from `ones` to `twos` when they appear a second time, or clears them when they appear a third time.
5. After iterating through all numbers, return `ones`, which holds the value of the unique number.

## Complexity Analysis

- **Time:** O(N) where N is the length of `nums`, as we iterate through the array once and perform constant-time bitwise operations per element.
- **Space:** O(1) auxiliary space, using only two integer variables `ones` and `twos`.

## Edge Cases

- Array with a single element (`nums = [x]`): Loop executes once, returning `x` immediately.
- Negative numbers: Bitwise operations in Python handle negative numbers seamlessly using two's complement arithmetic.
- Unique element is 0: Bits will never set `ones` or `twos`, correctly returning 0.
- Extreme 32-bit values: Correctly processes integers near -2^31 and 2^31 - 1 without overflow issues.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def single_number_ii(nums: list[int]) -> int:
    """Find the element that appears once among triple duplicates."""
    ones = 0
    twos = 0

    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones
```
