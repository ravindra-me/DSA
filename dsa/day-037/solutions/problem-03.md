# Solution 3: Radix Sort 32-bit Integers

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** LSD Radix Sort with bitwise shifts or base representation

## Approach

LSD (Least Significant Digit) Radix Sort sorts fixed-width integers by processing chunks of bits from least significant to most significant using a stable sorting algorithm (Counting Sort) as a subroutine. By using an 8-bit chunk size (base 256), any 32-bit integer is fully sorted in exactly 4 linear-time passes.

## Thought Process

Comparison-based sorts require $\Omega(n \log n)$ operations in the worst case. When keys are fixed-width integers, we can avoid comparisons by utilizing their digit or bit representation.

In LSD Radix Sort, numbers are sorted starting from the least significant digit (LSD) up to the most significant digit (MSD). Crucially, the sorting algorithm used for each digit position must be stable—meaning elements with identical current digits preserve their relative ordering from earlier passes. Counting Sort is ideal for this subroutine because the radix (digit alphabet size) is small.

Choosing a radix base is a trade-off: base 10 requires up to 10 passes for 32-bit integers and involves modulo/division operations. In binary representation, choosing chunks of $k=8$ bits gives a radix base $b = 2^8 = 256$. For 32-bit integers, this requires only $d = 32 / 8 = 4$ passes. Extraction of the $i$-th chunk is fast via bitwise shift and mask: `(x >> (8 * i)) & 0xFF`.

## Algorithm

1. Handle the edge cases: if `nums` is empty or has length 1, return a copy of `nums` immediately.
2. Determine the number of passes needed based on the maximum value in `nums`, or default to 4 passes (for full 32-bit integers). If the maximum value is 0, return `nums.copy()`.
3. Choose a radix chunk size of 8 bits (`MASK = 0xFF`, `RADIX = 256`). Compute `max_val = max(nums)` to determine how many 8-bit shifts are actually needed (at most 4 passes for 32-bit values).
4. For each pass `shift` in `0, 8, 16, 24` (up to `max_val.bit_length()`):
5. Initialize a frequency array `counts` of size 256 with zeros.
6. Count occurrences of each byte: `counts[(num >> shift) & 0xFF] += 1`.
7. Convert counts into prefix sums (starting positions in the output array).
8. Iterate through `nums` in reverse order (to preserve stability) or place into `output` using the prefix sums, decrementing prefix pointers.
9. Set `nums = output` and repeat for the next byte shift.
10. Return the fully sorted list `nums`.

## Complexity Analysis

- **Time:** $O(d \cdot (n + b))$ where $d \le 4$ is the number of 8-bit passes, $n$ is the number of elements, and $b = 256$ is the radix base. For 32-bit integers, $d$ is constant, making overall time $O(n)$.
- **Space:** $O(n + b)$ auxiliary space for the output buffer of size $n$ and the frequency bucket count array of size $b = 256$.

## Edge Cases

- Empty list: returns empty list immediately without error.
- Single element: returns a single-element list copy.
- All identical elements (e.g., all 0s): frequency array maps all elements to bucket 0 in each pass, leaving elements sorted and preserving stability.
- Maximum 32-bit integer values (e.g., $2^{31} - 1$): bit shifting and masking handles up to 31/32 bits seamlessly across all 4 passes.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def radix_sort(nums: list[int]) -> list[int]:
    """Sorts non-negative integers using LSD Radix Sort."""
    if len(nums) <= 1:
        return list(nums)

    max_val = max(nums)
    if max_val == 0:
        return list(nums)

    current = list(nums)
    n = len(current)
    bits = max_val.bit_length()
    shift = 0
    radix = 256
    mask = 0xFF

    while shift < bits:
        count = [0] * radix
        output = [0] * n

        for num in current:
            digit = (num >> shift) & mask
            count[digit] += 1

        for i in range(1, radix):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            num = current[i]
            digit = (num >> shift) & mask
            count[digit] -= 1
            output[count[digit]] = num

        current = output
        shift += 8

    return current
```
