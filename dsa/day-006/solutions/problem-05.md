# Solution 5: Maximum XOR of Two Numbers in an Array

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Bitwise prefix matching and greedy evaluation with masks

## Approach

We build the maximum XOR greedily bit-by-bit from the most significant bit (bit 30 down to bit 0). For each bit position, we hypothesize that the bit can be set to 1 in the maximum XOR, and use a hash set of prefixes masked to the current bit to verify in $O(n)$ time if two prefixes exist whose XOR equals this candidate value, exploiting the identity $A \oplus B = C \iff A \oplus C = B$.

## Thought Process

A brute-force solution checks all pairs $(nums[i], nums[j])$, which takes $O(n^2)$ time. Given $n \le 2 \times 10^5$, $O(n^2)$ requires roughly $4 \times 10^{10}$ operations and will time out.

To improve upon this, observe that bitwise XOR can be evaluated greedily from the most significant bit (MSB) to the least significant bit (LSB). A higher bit being 1 is always strictly greater than all lower bits combined ($2^k > \sum_{j=0}^{k-1} 2^j$).

There are two primary $O(32n)$ approaches: a binary Trie (prefix tree) or a bitmask hash set. The bitmask hash set approach works without building an explicit tree: at each bit $i$ from 30 down to 0, we accumulate a bitmask covering bits 30 down to $i$. We formulate a candidate maximum `candidate = max_xor | (1 << i)`. For `candidate` to be achievable, there must exist two prefixes $p_1, p_2$ in our masked prefix set such that $p_1 \oplus p_2 = \text{candidate}$. By properties of XOR, this is equivalent to $p_1 \oplus \text{candidate} = p_2$. Thus, we can check if any $p_1$ satisfies $(p_1 \oplus \text{candidate}) \in \text{prefixes}$ in $O(1)$ average time per element.

## Algorithm

1. Initialize `max_xor = 0` and `mask = 0`.
2. Loop through bit positions `i` from 30 down to 0.
3. Update `mask = mask | (1 << i)` to capture bits from 30 down to `i`.
4. Collect the prefixes of all numbers up to bit `i`: `prefixes = {num & mask for num in nums}`.
5. Set `candidate = max_xor | (1 << i)` as the hopeful maximum XOR down to bit `i`.
6. Iterate through each prefix `p` in `prefixes`. If `(p ^ candidate)` is also in `prefixes`, then two elements exist that achieve `candidate`. Update `max_xor = candidate` and break early.
7. If no such pair exists, `max_xor` retains its previous value with bit `i` as 0.
8. Return `max_xor` after inspecting all 31 bits.

## Complexity Analysis

- **Time:** $O(31 \cdot n) = O(n)$ time since we iterate 31 times (for bits 0 to 30), and in each iteration we perform $O(n)$ work building and querying a hash set.
- **Space:** $O(n)$ space to store the masked prefixes of numbers in the hash set.

## Edge Cases

- Single element array (`len(nums) == 1`): $nums[0] \oplus nums[0] = 0$, the algorithm naturally tests candidate bits which fail, correctly returning 0.
- All elements are identical: every pair XORs to 0, returning 0.
- Contains 0 and maximum possible value ($2^{31} - 1$): handled without integer overflow because 31 bits cover non-negative signed 32-bit integers up to $2^{31}-1$.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def find_maximum_xor(nums: list[int]) -> int:
    """Return the maximum XOR value formed by any two numbers in nums."""
    max_xor = 0
    mask = 0

    for bit in range(30, -1, -1):
        mask |= (1 << bit)
        prefixes = {num & mask for num in nums}
        candidate = max_xor | (1 << bit)

        for prefix in prefixes:
            if (prefix ^ candidate) in prefixes:
                max_xor = candidate
                break

    return max_xor
```
