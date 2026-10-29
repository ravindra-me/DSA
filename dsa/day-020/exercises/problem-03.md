# Problem 3: Coprime Component Groups

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | GCD & Prime Factorization Graph Reduction | [Day 20: Basic Mathematics for DSA](../README.md) |

## Problem Statement

You are given a list of positive integers `nums`. Two indices `i` and `j` (`i != j`) are directly connected if $\gcd(\text{nums}[i], \text{nums}[j]) > 1$.

Connectivity is transitive: if `i` is connected to `j`, and `j` is connected to `k`, then `i` and `k` are in the same connected component. Return the size of the largest connected component in `nums`.

Numbers equal to 1 have no prime factors and can never share a GCD > 1 with any number (including another 1).

## Input

A list of integers `nums: list[int]`.

## Output

An integer representing the maximum number of indices in a single connected component.

## Constraints

- 1 <= len(nums) <= 20000
- 1 <= nums[i] <= 100000

## Examples

**Example 1**

```text
Input:  nums = [4, 6, 15, 35]
Output: 4
```

gcd(4,6)=2, gcd(6,15)=3, gcd(15,35)=5. All 4 elements form a single component.

**Example 2**

```text
Input:  nums = [2, 3, 5, 7, 11]
Output: 1
```

All numbers are distinct primes, so gcd of any pair is 1. The maximum component size is 1.

## Function Signature

```python
def largest_coprime_component(nums: list[int]) -> int:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Precompute smallest prime factors via Sieve up to max(nums). Factor each number and connect each number's index to its prime factors using Union-Find (Disjoint Set Union) in near O(N log(max_val)) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
