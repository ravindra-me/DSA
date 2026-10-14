# Solution 5: Prime Counting in Ranges (Segmented Sieve)

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Segmented Sieve of Eratosthenes

## Approach

A segmented sieve computes primes in the interval `[low, high]` by first finding all prime numbers up to `sqrt(high)` using a standard Sieve of Eratosthenes. Then, it uses an array of size `high - low + 1` to mark multiples of those small primes within `[low, high]`.

## Thought Process

When `high` can reach $10^9$, allocating an array of size $10^9$ for a standard sieve requires gigabytes of memory and would exceed limits. However, the interval length $R = high - low + 1$ is at most $10^5 + 1$. Any composite number $n \le high$ must have a prime factor $p \le \sqrt{high} \le \sqrt{10^9} \approx 31622$. Therefore, we only need to precompute primes up to $\lfloor\sqrt{high}\rfloor$ using a standard sieve (which takes negligible memory and time, $< 32000$ operations). For each prime $p$, we find its smallest multiple in $[low, high]$ that is greater than or equal to $\max(p^2, \lceil low / p \rceil \times p)$. We then cross out all its multiples in a boolean array of size $R$, mapping index $i$ to number $low + i$. Finally, we count how many numbers remain unmarked (taking care to also mark $1$ as not prime if $low = 1$).

## Algorithm

1. Compute limit = floor(sqrt(high)).
2. Use a standard Sieve of Eratosthenes to generate all prime numbers up to limit.
3. Allocate a boolean array `is_prime` of length `range_len = high - low + 1`, initialized to `True`.
4. For each precomputed prime `p`: determine the first multiple of `p` in `[low, high]` that is greater than or equal to `p * p`, or `ceil(low / p) * p` (ensuring we do not mark `p` itself as composite if `p >= low`).
5. Step through multiples of `p` by `p`, setting `is_prime[multiple - low] = False`.
6. If `low <= 1`, ensure index `1 - low` (number 1) is marked `False` because 1 is not prime.
7. Return the sum of `True` entries in `is_prime`.

## Complexity Analysis

- **Time:** O(sqrt(high) * log(log(sqrt(high))) + (high - low) * log(log(sqrt(high)))) which is roughly O(31622 + 10^5 * log(log(31622))) operations, comfortably executing in a few milliseconds.
- **Space:** O(sqrt(high) + (high - low + 1)) auxiliary space to store primes up to sqrt(high) and the segmented boolean array, requiring less than 1 MB.

## Edge Cases

- `low = 1`: 1 is not prime and must be explicitly unmarked (`is_prime[1 - low] = False`).
- `low == high`: The range has length 1. Handled naturally by creating an array of size 1.
- `high <= 3`: `sqrt(high)` can be 1, in which case the list of primes up to `sqrt(high)` is empty, correctly handled.
- `p` itself is inside `[low, high]`: The starting multiple must be at least `2 * p` (or `p * p`) so the prime itself is not crossed off.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
import math

def count_primes_in_range(low: int, high: int) -> int:
    """Counts primes in [low, high] using a segmented sieve."""
    if high < 2 or low > high:
        return 0

    limit = math.isqrt(high)

    # Step 1: Standard sieve to find all primes up to sqrt(high)
    sieve_limit = [True] * (limit + 1)
    if limit >= 0:
        sieve_limit[0] = False
    if limit >= 1:
        sieve_limit[1] = False

    for i in range(2, math.isqrt(limit) + 1):
        if sieve_limit[i]:
            for j in range(i * i, limit + 1, i):
                sieve_limit[j] = False

    primes = [i for i, is_p in enumerate(sieve_limit) if is_p]

    # Step 2: Segmented sieve for [low, high]
    range_len = high - low + 1
    is_prime = [True] * range_len

    for p in primes:
        # Smallest multiple of p that is >= low and >= p * p
        start = max(p * p, ((low + p - 1) // p) * p)
        for multiple in range(start, high + 1, p):
            is_prime[multiple - low] = False

    # Step 3: Handle 1 if in range (1 is not prime)
    if low == 1:
        is_prime[0] = False

    return sum(is_prime)
```
