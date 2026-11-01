# Solution 5: Minimum XOR Sum of Two Arrays

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Bitmask Dynamic Programming over permutations

## Approach

We use Dynamic Programming with Bitmasking. A bitmask of length $n$ represents which elements from `nums2` have already been paired. The number of set bits (popcount) in `mask` indicates how many elements of `nums1` have been processed, meaning the current element to pair is `nums1[i]` where `i = popcount(mask)`. We iterate through all unset bits $j$ in `mask`, transition to state `mask | (1 << j)` by adding `nums1[i] ^ nums2[j]`, and minimize the result.

## Thought Process

A naive solution checks all $n!$ permutations of `nums2`. For $n = 14$, $14! \approx 8.71 \times 10^{10}$, which is far too slow.

Notice that when pairing `nums1[0 ... i-1]` with a specific subset of `nums2` of size $i$, the optimal cost to pair the remaining elements depends ONLY on which subset of `nums2` was used, not on the exact matching order within that subset. 

Since $n \le 14$, a subset of `nums2` can be represented as an integer bitmask from `0` to $2^n - 1$. The state `dp[mask]` represents the minimum XOR sum to pair the first `popcount(mask)` elements of `nums1` using the subset of `nums2` defined by `mask`. The total number of states is $2^{14} = 16,384$, and from each state there are at most 14 transitions. This gives an overall complexity of $O(n 2^n)$, which easily runs well within time limits.

## Algorithm

1. Let $n$ be the length of `nums1` (and `nums2`).
2. Initialize a DP array `dp` of size $2^n$ with infinity (`float('inf')`), and set `dp[0] = 0`.
3. Iterate through all state masks from `0` to $2^n - 1$.
4. For each `mask`, compute `i = mask.bit_count()`, which is the index of the next element in `nums1` to be paired.
5. If `i == n`, skip since all elements are paired.
6. Iterate over each bit index $j$ from $0$ to $n - 1$.
7. If the $j$-th bit of `mask` is not set (`(mask & (1 << j)) == 0`), compute the cost of pairing `nums1[i]` with `nums2[j]`.
8. Update `dp[mask | (1 << j)] = min(dp[mask | (1 << j)], dp[mask] + (nums1[i] ^ nums2[j]))`.
9. Return `dp[(1 << n) - 1]`.

## Complexity Analysis

- **Time:** $
O(n 2^n)$ where $n \le 14$. For $n = 14$, $14 \times 2^{14} \approx 2.29 \times 10^5$ operations, taking $< 0.01$ seconds.
- **Space:** $
O(2^n)$ to store the DP array of size $2^{14} = 16,384$ integers.

## Edge Cases

- Smallest input size $n = 1$: handled correctly, bitmask ranges from 0 to 1.
- Duplicate numbers in input arrays: DP logic automatically considers all index permutations cleanly without extra checks.
- Array elements are 0: XOR with 0 yields the value itself, bitwise operators execute correctly.
- Maximum values ($10^7$): bitwise XOR operations natively handle large integers up to constraints.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def minimum_xor_sum(nums1: list[int], nums2: list[int]) -> int:
    """Calculate the minimum XOR sum using bitmask dynamic programming."""
    n = len(nums1)
    num_states = 1 << n
    dp = [float('inf')] * num_states
    dp[0] = 0
    
    for mask in range(num_states):
        i = mask.bit_count()
        if i == n:
            continue
        
        val1 = nums1[i]
        for j in range(n):
            if not (mask & (1 << j)):
                next_mask = mask | (1 << j)
                cost = dp[mask] + (val1 ^ nums2[j])
                if cost < dp[next_mask]:
                    dp[next_mask] = cost
                    
    return int(dp[num_states - 1])
```
