# Solution 3: Sum of Hamming Distances of All Pairs

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium/Hard | **Concept:** Bit-by-bit contribution counting across array elements

## Approach

Instead of computing the Hamming distance between every pair $(i, j)$ directly, evaluate the contribution of each bit position independently. For a fixed bit position $k$, count how many numbers have a `1` at that position ($c$) and how many have a `0` ($n - c$). Each $(1, 0)$ pairing across this bit contributes $1$ to the total Hamming distance, so this bit position contributes $c \times (n - c)$ in total.

## Thought Process

A brute-force solution checks all $\binom{n}{2} = \frac{n(n - 1)}{2}$ pairs, computing `bin(nums[i] ^ nums[j]).count('1')` for each. With $n = 10^4$, there are roughly $5 \times 10^7$ pairs, each taking up to 30 bit operations—leading to over $1.5 \times 10^9$ operations, which easily times out.

To optimize, use the linearity of summation: the total Hamming distance is the sum over all bit positions $k$ of the number of pairs $(i, j)$ whose $k$-th bits differ. Since $nums[i] \le 10^9 < 2^{30}$, we only need to inspect bit positions $0$ through $29$ (or $30$).

For bit $k$, let $c_k$ be the count of elements with the $k$-th bit set. The remaining $n - c_k$ elements have the $k$-th bit unset. Any pair formed by picking one element from the set group and one from the unset group will differ at bit $k$. Pairs within the set group or within the unset group will have identical bits at position $k$ and contribute $0$. Hence, bit $k$ contributes exactly $c_k \times (n - c_k)$ to the global sum. Summing this over all 30 bit positions takes $O(30n)$ time, which requires only about $3 \times 10^5$ operations and runs well within a few milliseconds.

## Algorithm

1. Initialize `total_distance = 0` and `n = len(nums)`.
2. Loop over each bit position `bit` from $0$ up to $29$ (since $10^9 < 2^{30}$).
3. For the current bit position, count how many numbers in `nums` have the bit set: `ones = sum((num >> bit) & 1 for num in nums)`.
4. Add `ones * (n - ones)` to `total_distance`.
5. Return `total_distance` after inspecting all relevant bit positions.

## Complexity Analysis

- **Time:** O(B * n), where B is the number of bits needed to represent the maximum integer (B <= 30 for <= 10^9) and n is the length of nums. With n = 10,000, 30 * 10,000 = 3 * 10^5 operations, running in a fraction of a second.
- **Space:** O(1) auxiliary space, requiring only a few integer counters.

## Edge Cases

- Single element array (n = 1): returns 0 because no pairs exist (ones * (1 - ones) is always 0).
- All identical elements (e.g., all zeros or duplicate values): returns 0 because for every bit, either ones = 0 or ones = n.
- Maximum values (up to 10^9): bit 29 is exercised correctly since 2^29 <= 10^9 < 2^30.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def total_hamming_distance(nums: list[int]) -> int:
    """Calculate total Hamming distance across all pairs."""
    n = len(nums)
    if n < 2:
        return 0

    total_distance = 0
    # nums[i] <= 10^9 < 2^30, so 30 bits (0 through 29) are sufficient.
    for bit in range(30):
        ones = sum((x >> bit) & 1 for x in nums)
        total_distance += ones * (n - ones)

    return total_distance
```
