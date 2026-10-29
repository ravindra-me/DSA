# Problem 5: Modular Combination Sequence Queries

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Modular Arithmetic, Factorial Precomputation & Fermat's Inverse | [Day 20: Basic Mathematics for DSA](../README.md) |

## Problem Statement

You need to answer multiple queries computing the binomial coefficient modulo a fixed prime $P = 10^9 + 7$.

You are given two integer lists `n_vals` and `k_vals` of equal length $Q$, where the $i$-th query asks for $\binom{n_i}{k_i} \pmod{10^9 + 7}$. If $k_i > n_i$ or $k_i < 0$, $\binom{n_i}{k_i} = 0$.

Your solution should answer all queries efficiently.

## Input

`n_vals: list[int]` and `k_vals: list[int]` both of length `q`.

## Output

`list[int]` of length `q` where result[i] is $\binom{n_i}{k_i} \pmod{10^9 + 7}$.

## Constraints

- 1 <= len(n_vals) == len(k_vals) <= 100000
- 0 <= n_vals[i] <= 200000
- 0 <= k_vals[i] <= 200000

## Examples

**Example 1**

```text
Input:  n_vals = [5, 3, 10], k_vals = [2, 5, 0]
Output: [10, 0, 1]
```

C(5,2)=10; C(3,5)=0 since k > n; C(10,0)=1.

**Example 2**

```text
Input:  n_vals = [0], k_vals = [0]
Output: [1]
```

C(0,0) = 1.

## Function Signature

```python
def batch_combinations_modulo(n_vals: list[int], k_vals: list[int]) -> list[int]:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Precompute factorials and inverse factorials up to max(n) in O(max(n)) using Fermat's Little Theorem, then answer each query in O(1) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
