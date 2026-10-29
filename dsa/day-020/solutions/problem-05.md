# Solution 5: Modular Combination Sequence Queries

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Modular Arithmetic, Factorial Precomputation & Fermat's Inverse

## Approach

Precompute factorials and modular inverse factorials up to the maximum $N$ in $O(N)$ time. Then answer each combination query in $O(1)$ using the formula $\binom{n}{k} \equiv n! \cdot (k!)^{-1} \cdot ((n-k)!)^{-1} \pmod P$.

## Thought Process

A naive approach calculates $\binom{n}{k} = \frac{n!}{k!(n-k)!} \pmod P$ for each query independently using repeated multiplication or modular exponentiation via Fermat's Little Theorem ($a^{-1} \equiv a^{P-2} \pmod P$). Computing this for each of the $Q = 10^5$ queries would take $O(Q \log P)$ or $O(Q \cdot N)$, leading to $10^5 \times 30 \approx 3 \times 10^6$ operations or worse, which is inefficient if repeated from scratch.

Since $P = 10^9 + 7$ is prime and fixed across queries, we can precompute factorials `fact[i]` up to $\max(n)$ in $O(\max N)$ time. We can also precompute inverse factorials `inv_fact[i]` in $O(\max N)$ total time by computing $\text{inv\_fact}[M] = (M!)^{-1} \pmod P$ once with `pow(fact[M], P - 2, P)` and iterating backwards: $\text{inv\_fact}[i-1] = \text{inv\_fact}[i] \cdot i \pmod P$.

With these two lookup arrays, each query is answered in $O(1)$ time by checking boundary conditions ($k < 0$ or $k > n$) and evaluating `fact[n] * inv_fact[k] % P * inv_fact[n - k] % P`.

## Algorithm

1. Find the maximum $n$ among all queries, bounded by at least 1 and up to the problem constraint (or simply precompute up to $\max(n)$). If $n\_vals$ is empty, return an empty list.
2. Allocate `fact` and `inv_fact` arrays of size $\max(n) + 1$.
3. Compute `fact[0] = 1` and `fact[i] = (fact[i - 1] * i) % MOD` for $i$ from 1 to $\max(n)$.
4. Compute `inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)` using Fermat's Little Theorem.
5. Backpropagate inverse factorials: for $i$ from $\max(n)$ down to 1, set `inv_fact[i - 1] = (inv_fact[i] * i) % MOD`.
6. Iterate through the pairs $(n_i, k_i)$: if $k_i < 0$ or $k_i > n_i$, append 0; otherwise, append `(fact[n_i] * inv_fact[k_i] % MOD) * inv_fact[n_i - k_i] % MOD`.
7. Return the collected results.

## Complexity Analysis

- **Time:** $O(M + Q)$ where $M = \max(n) \le 200,000$ and $Q$ is the number of queries. Precomputing factorials and inverse factorials takes $O(M)$ time with a single $O(\log P)$ modular exponentiation call, and answering each of the $Q$ queries takes $O(1)$ time.
- **Space:** $O(M + Q)$ to store the precomputed factorial arrays of size $M + 1$ and the result list of length $Q$.

## Edge Cases

- k > n or k < 0: returns 0 as specified by the combination definition.
- k == 0 or k == n: returns 1 (correctly evaluated since 0! = 1 and inv_fact[0] = 1).
- n == 0 and k == 0: handled correctly, yields 1.
- All n_vals and k_vals are maximum values (200,000): precomputation covers the entire range without array out-of-bounds.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def batch_combinations_modulo(n_vals: list[int], k_vals: list[int]) -> list[int]:
    """Compute C(n, k) % (10^9 + 7) for multiple queries in O(max(N) + Q) time."""
    if not n_vals:
        return []

    mod = 1_000_000_007
    max_n = max(n_vals)
    if max_n == 0:
        return [1 if k == 0 else 0 for k in k_vals]

    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = (fact[i - 1] * i) % mod

    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = pow(fact[max_n], mod - 2, mod)
    for i in range(max_n, 0, -1):
        inv_fact[i - 1] = (inv_fact[i] * i) % mod

    res = []
    for n, k in zip(n_vals, k_vals):
        if k < 0 or k > n:
            res.append(0)
        else:
            val = (fact[n] * inv_fact[k]) % mod
            val = (val * inv_fact[n - k]) % mod
            res.append(val)

    return res
```
