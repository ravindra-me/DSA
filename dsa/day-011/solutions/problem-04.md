# Solution 4: Maximum Length of Repeated Subarray

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** dynamic-arrays

## Approach

We use dynamic programming where `dp[j]` represents the length of the longest common suffix between the prefix `nums1[:i]` and `nums2[:j]`. If `nums1[i-1] == nums2[j-1]`, then `dp[j] = dp[j-1] + 1`; otherwise, `dp[j] = 0`. We can compress the 2D DP table to a single 1D array by iterating `j` backwards to reuse values from the previous row.

## Thought Process

A brute-force solution checks all possible subarrays of `nums1` and looks for their occurrences in `nums2`. With $N, M \le 1000$, generating all subarrays takes $O(N^2)$ and comparing them takes $O(M)$, leading to $O(N^2 M)$ or $O(N \cdot M^2)$ time, which is too slow ($10^9$ operations).

To optimize, notice that if `nums1[i-1] == nums2[j-1]`, the longest common subarray ending at index `i-1` in `nums1` and `j-1` in `nums2` extends the longest common subarray ending at `i-2` and `j-2` by 1. That is:
$$\text{dp}[i][j] = \text{dp}[i-1][j-1] + 1 \quad \text{if } nums1[i-1] == nums2[j-1] \text{ else } 0$$

Because computing row $i$ only depends on row $i-1$ and specifically the previous column $j-1$, we can compress the $N \times M$ table into a single 1D array of length $M + 1$. By iterating $j$ from $M$ down to 1, `dp[j-1]` still holds the value from row $i-1$, allowing us to update `dp[j]` in place without overwriting needed data.

## Algorithm

1. Initialize an integer `max_len = 0` to track the maximum contiguous length found.
2. Initialize a 1D array `dp` of size `len(nums2) + 1` filled with zeros.
3. Iterate `num1` through each element of `nums1` (representing index `i` from 1 to `len(nums1)`).
4. In an inner loop, iterate `j` backwards from `len(nums2)` down to 1.
5. If `num1 == nums2[j - 1]`, set `dp[j] = dp[j - 1] + 1` and update `max_len = max(max_len, dp[j])`.
6. Otherwise, set `dp[j] = 0` because no common subarray ends at these positions.
7. Return `max_len` after all iterations complete.

## Complexity Analysis

- **Time:** O(N * M) where N = len(nums1) and M = len(nums2). We have two nested loops of lengths N and M doing O(1) work per step. For N, M <= 1000, N * M <= 1,000,000 operations, which runs in well under 0.5 seconds.
- **Space:** O(M) auxiliary space (or O(min(N, M)) if we choose the shorter array for dp). We maintain only a single 1D array of size M + 1.

## Edge Cases

- No common elements: `dp[j]` will always be reset to 0, correctly returning 0.
- Entire arrays match: `dp[j]` increments all the way to `len(nums1)`, correctly returning the full length.
- Single-element arrays: The loops execute once; returns 1 if elements match, 0 otherwise.
- Duplicate numbers within an array: Handled seamlessly as the condition checks pointwise equality and tracks strictly contiguous matches.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def find_length(nums1: list[int], nums2: list[int]) -> int:
    """Finds the maximum length of a contiguous subarray appearing in both arrays."""
    # Optimization: ensure nums2 is the shorter array to minimize memory
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums2)
    dp = [0] * (m + 1)
    max_len = 0

    for val1 in nums1:
        for j in range(m, 0, -1):
            if val1 == nums2[j - 1]:
                dp[j] = dp[j - 1] + 1
                if dp[j] > max_len:
                    max_len = dp[j]
            else:
                dp[j] = 0

    return max_len
```
