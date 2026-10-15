# Solution 2: Single Number from Pairs

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** XOR cancellation property

## Approach

We leverage the XOR operation's algebraic properties: $x \oplus x = 0$ (self-inverse) and $x \oplus 0 = x$ (identity). By computing the cumulative XOR of all elements in the array, every number that appears twice cancels itself out to $0$, leaving only the single element that appears once.

## Thought Process

A naive approach might count the frequencies of every element using a hash map or sorting the array. A hash map requires $O(n)$ time and $O(n)$ auxiliary space. Sorting takes $O(n \log n)$ time and $O(1)$ or $O(n)$ extra space depending on the sorting algorithm.

The problem statement strictly requires $O(n)$ time complexity and $O(1)$ auxiliary space. This constraint hints at bitwise operations, specifically the bitwise XOR (`^`).

XOR is both commutative ($a \oplus b = b \oplus a$) and associative ($(a \oplus b) \oplus c = a \oplus (b \oplus c)$). Because every paired element appears twice, their XOR sum is $v \oplus v = 0$. Consequently, XORing all elements together can be rearranged into $(v_1 \oplus v_1) \oplus (v_2 \oplus v_2) \oplus \dots \oplus u = 0 \oplus 0 \oplus \dots \oplus u = u$, directly isolating the unique value in a single pass without extra memory.

## Algorithm

1. Initialize an accumulator variable `unique_val = 0`.
2. Iterate through each number `num` in `nums`.
3. Update `unique_val` by XORing it with `num` (`unique_val ^= num`).
4. Return `unique_val` after processing all elements in the array.

## Complexity Analysis

- **Time:** $O(n)$ because we iterate through the list of length $n$ exactly once, performing an $O(1)$ XOR operation at each step.
- **Space:** $O(1)$ auxiliary space because we only maintain a single accumulator integer variable.

## Edge Cases

- Single element array (`len(nums) == 1`): The loop executes once, XORing 0 with the single element, correctly returning it.
- Negative numbers: In two's complement arithmetic, XOR handles negative numbers and bit representations identically to positive numbers.
- Zero as an element or as the unique answer: $0 \oplus 0 = 0$ and $x \oplus 0 = x$, meaning zero correctly participates in pairing and cancellation without special-case logic.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def single_number(nums: list[int]) -> int:
    """Find the single element that appears only once in nums."""
    unique_val = 0
    for num in nums:
        unique_val ^= num
    return unique_val
```
