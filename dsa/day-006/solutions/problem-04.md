# Solution 4: Single Number III (Two Unique Elements)

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Partitioning elements by distinguishing bit using lowest set bit

## Approach

XOR all elements together to obtain `xor_all = a ^ b`, where `a` and `b` are the two unique numbers. Because `a != b`, `xor_all` is non-zero and has at least one set bit, which indicates a bit position where `a` and `b` differ. We isolate the lowest set bit using `diff_bit = xor_all & (-xor_all)`. We then partition the array into two subsets based on whether that bit is set or not; XORing within each partition isolates `a` and `b` separately.

## Thought Process

A brute-force solution using a hash map or frequency counter would track counts in $O(n)$ time and $O(n)$ space, or sorting would take $O(n \log n)$ time and $O(1)$ space. However, the problem strictly requires $O(n)$ time and $O(1)$ auxiliary space.

From the properties of XOR ($x \oplus x = 0$ and $x \oplus 0 = x$), XORing every number in the array cancels out all elements that appear twice, leaving `xor_all = a ^ b`. Since $a \neq b$, `xor_all` cannot be 0, meaning there is at least one bit position where $a$ and $b$ differ (one has a 1, the other a 0 at that position).

We can pick any distinguishing bit—most conveniently, the lowest set bit via `diff_bit = xor_all & (-xor_all)`. Every element in `nums` either has this bit set or unset. Elements that appear twice will fall into the same group and cancel each other out when XORed within that group. Furthermore, `a` and `b` will fall into different groups. Thus, XORing all elements with `num & diff_bit != 0` yields one unique number, and XORing the rest yields the other.

## Algorithm

1. Compute `xor_all = functools.reduce(lambda x, y: x ^ y, nums, 0)`.
2. Isolate the lowest set bit of `xor_all`: `diff_bit = xor_all & (-xor_all)`.
3. Initialize two accumulators `num1 = 0` and `num2 = 0`.
4. Iterate through each number in `nums`: if `num & diff_bit` is non-zero, XOR it into `num1`; otherwise, XOR it into `num2`.
5. Return `[min(num1, num2), max(num1, num2)]` to guarantee ascending order.

## Complexity Analysis

- **Time:** $O(n)$ because we iterate through the list of length $n$ twice (once to compute total XOR, once to partition).
- **Space:** $O(1)$ auxiliary space as we only use a few integer variables (`xor_all`, `diff_bit`, `num1`, `num2`).

## Edge Cases

- Negative numbers and zero: Two's complement bitwise arithmetic in Python handles negative integers cleanly with `xor_all & (-xor_all)`.
- Minimum array size of 2: Contains only the two unique elements, both are extracted correctly.
- Boundary values: Extreme 32-bit signed integers ($-2^{31}$ and $2^{31}-1$) are handled naturally without overflow issues in Python.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def single_number_two_uniques(nums: list[int]) -> list[int]:
    """Find the two unique numbers in nums, returned in ascending order."""
    xor_all = 0
    for num in nums:
        xor_all ^= num

    # Isolate the lowest set bit where the two unique numbers differ
    diff_bit = xor_all & (-xor_all)

    num1 = 0
    num2 = 0
    for num in nums:
        if num & diff_bit:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2] if num1 < num2 else [num2, num1]
```
