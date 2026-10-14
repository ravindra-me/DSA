# Solution 3: Prime Factor Counting Queries

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Sieve of Eratosthenes with precomputed Smallest Prime Factor (SPF)

## Approach

Precompute the Smallest Prime Factor (SPF) for every integer up to $n$ using a modified Sieve of Eratosthenes in $O(n \log \log n)$ time. For each query $x$, repeatedly divide by $\text{spf}[x]$ to extract distinct prime factors in $O(\log x)$ operations.

## Thought Process

A naive approach checks prime factors for each query number $x$ independently using trial division up to $\sqrt{x}$. With up to $10^5$ queries and $x \le 10^6$, doing $O(\sqrt{x})$ work per query could take up to $10^5 \times 1000 = 10^8$ operations, which risks timing out in Python.

Because multiple queries are asked over a fixed domain $[2, n]$, we can preprocess using a Sieve of Eratosthenes. Instead of merely marking primality, we compute the smallest prime factor $\text{spf}[i]$ for every $i \in [2, n]$.

When querying a value $x$, its smallest prime factor $p = \text{spf}[x]$ is retrieved in $O(1)$. We increment the count of distinct prime factors by 1, and divide $x$ by $p$ until $x$ is no longer divisible by $p$. We repeat this until $x = 1$. The factorization requires at most $\log_2(x)$ divisions per query, making the per-query time proportional to the total number of prime factors.

## Algorithm

1. Initialize an array `spf` of size `n + 1` where `spf[i] = i` for all $i \in [0, n]$.
2. Run a sieve: for each even number $i \ge 4$ with step 2, set `spf[i] = 2`.
3. For odd $i$ from 3 up to $\lfloor\sqrt{n}\rfloor$: if `spf[i] == i` (meaning $i$ is prime), iterate through multiples $j = i \times i$ up to $n$ in increments of $2i$, and if `spf[j] == j`, set `spf[j] = i`.
4. For each query $x$ in `queries`, initialize `count = 0`.
5. While $x > 1$, let $p = \text{spf}[x]$, increment `count`, and while $x \% p == 0$, divide $x //= p$.
6. Append `count` to the result list and return it.

## Complexity Analysis

- **Time:** Precomputation takes $O(n \log \log n)$ time to compute the SPF array using the Sieve of Eratosthenes. Each query $x$ is factorized in $O(\log x)$ time (or specifically $O(\Omega(x))$, the number of prime factors with multiplicity). Overall time is $O(n \log \log n + Q \log(\max(x)))$, well within the 1-second budget for $n = 10^6$ and $Q = 10^5$.
- **Space:** $O(n)$ auxiliary space to store the `spf` array of length $n + 1$.

## Edge Cases

- Smallest $n = 2$: the array `spf` has length 3 and handles $x = 2$ correctly.
- Prime queries: handled immediately in 1 step because $\text{spf}[x] = x$, resulting in a count of 1.
- Prime powers (e.g. $16 = 2^4$): the inner loop consumes all repeated prime factors, counting $p$ only once.
- Duplicate query values: correctly processed identically and independently.
- Single query list: returns a 1-element list.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def count_distinct_prime_factors(n: int, queries: list[int]) -> list[int]:
    """Precomputes sieve/SPF up to n and answers distinct prime factor counts for each query."""
    spf = list(range(n + 1))

    for i in range(4, n + 1, 2):
        spf[i] = 2

    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if spf[i] == i:
            step = 2 * i
            for j in range(i * i, n + 1, step):
                if spf[j] == j:
                    spf[j] = i

    results = []
    for x in queries:
        distinct_count = 0
        while x > 1:
            p = spf[x]
            distinct_count += 1
            while x % p == 0:
                x //= p
        results.append(distinct_count)

    return results
```
