# Problem 5: Minimum XOR Sum of Two Arrays

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Bitmask Dynamic Programming over permutations | [Day 23: Bit Manipulation](../README.md) |

## Problem Statement

You are given two integer arrays `nums1` and `nums2` of equal length $n$.

The **XOR sum** of the two arrays is the sum of `(nums1[i] ^ nums2[perm[i]])` for all $0 \le i < n$, where `perm` is some permutation of `[0, 1, ..., n - 1]`.

Return the minimum possible XOR sum after choosing the optimal permutation of `nums2`.

## Input

Two lists of integers `nums1` and `nums2` of equal length $n$.

## Output

An integer representing the minimum XOR sum.

## Constraints

- 1 <= n == nums1.length == nums2.length <= 14
- 0 <= nums1[i], nums2[i] <= 10^7

## Examples

**Example 1**

```text
Input:  nums1 = [1, 2], nums2 = [2, 3]
Output: 2
```

Pair (1, 3) and (2, 2): (1 ^ 3) + (2 ^ 2) = 2 + 0 = 2.

**Example 2**

```text
Input:  nums1 = [1, 0, 3], nums2 = [5, 3, 4]
Output: 8
```

Best pairing: (1 ^ 5) + (0 ^ 4) + (3 ^ 3) = 4 + 4 + 0 = 8.

**Example 3**

```text
Input:  nums1 = [7], nums2 = [7]
Output: 0
```

Single elements: 7 ^ 7 = 0.

## Function Signature

```python
def minimum_xor_sum(nums1: list[int], nums2: list[int]) -> int:
    """Calculate the minimum XOR sum using bitmask dynamic programming."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Bitmask dynamic programming: let dp[mask] be the minimum XOR sum pairing the first k elements of nums1 (where k = popcount(mask)) with the elements of nums2 indicated by the set bits of mask.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
