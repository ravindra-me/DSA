# Solution 4: Prime Digit Circular Shifts

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Sieve of Eratosthenes & Digit Manipulation

## Approach

Precompute all primes up to the maximum potential cyclic rotation value using the Sieve of Eratosthenes. Then, check each prime below `limit` by generating all its cyclic digit rotations and verifying whether each rotation is prime. Pruning numbers containing even digits (0, 2, 4, 6, 8) or 5 (for multi-digit candidates) avoids unnecessary rotations.

## Thought Process

A naive approach would test primality on the fly for each number and its rotations using trial division. Given `limit` up to $1,000,000$, testing each number independently would be too slow. 

Instead, we can use the Sieve of Eratosthenes to precompute primality for all numbers in $O(N \log \log N)$ time. Notice that cyclic rotations of a number $< 1,000,000$ could theoretically exceed `limit` (e.g. if `limit = 100`, 97 rotates to 79 and 97, both $< 100$, but for arbitrary `limit` like 80, 79 rotates to 97 which is $\ge 80$). However, any rotation has the exact same number of digits as the original number, so a rotation of a number $< 1,000,000$ will never exceed $10^6 - 1$ (except when `limit = 1,000,000`, the maximum rotation cannot exceed $999,999$). Thus, sieving up to `limit` or at most $10^{\lceil \log_{10} \text{limit} \rceil}$ is sufficient. To be completely safe and avoid out-of-bounds indexing, we sieve up to $10^{\text{digits of } (\text{limit}-1)}$, which for $\text{limit} \le 1,000,000$ is at most $1,000,000$.

Furthermore, for numbers with more than one digit, any rotation ending in an even digit (0, 2, 4, 6, 8) or 5 cannot be prime. Since all digits cyclically rotate to the units place, any candidate containing 0, 2, 4, 5, 6, or 8 can be discarded immediately.

## Algorithm

1. If limit <= 2, return 0 immediately since there are no primes strictly less than 2.
2. Determine the maximum value a cyclic rotation could take: for any number n < limit, its rotation has the same number of digits, so max_val = 10 ** len(str(limit - 1)) - 1 (or at least limit).
3. Compute a boolean prime sieve array `is_prime` up to max_val using the Sieve of Eratosthenes.
4. Initialize `count = 0`.
5. Iterate through candidate primes p from 2 up to limit - 1:
6. If `is_prime[p]` is False, continue.
7. If p is a single digit (2, 3, 5, 7), it is a circular prime; increment `count`.
8. For multi-digit primes p, check if any digit is in {'0', '2', '4', '5', '6', '8'}. If so, p cannot be circular; continue.
9. Compute all cyclic rotations by taking string s = str(p) and length L = len(s). Check if int(s[i:] + s[:i]) is prime for all 1 <= i < L.
10. If all rotations are prime, increment `count`.
11. Return `count`.

## Complexity Analysis

- **Time:** O(N log log N) where N = 10^(ceil(log10(limit))). Sieve runs in O(N log log N). For limit <= 1,000,000, N <= 1,000,000. Checking each prime takes at most 6 rotations of 6 digits, taking O(d) per prime where d <= 6. Thus the overall time complexity is well within a fraction of a second.
- **Space:** O(N) to store the boolean sieve array up to 1,000,000, which requires around 1 MB.

## Edge Cases

- limit <= 2: No primes strictly less than 2, returns 0.
- Single-digit primes (2, 3, 5, 7): They have only one rotation (themselves) and are valid circular primes; 2 and 5 are handled properly despite containing digits 2 and 5.
- Power of 10 boundaries (e.g., limit = 10, limit = 100, limit = 1000): Handled accurately without index out-of-bounds.
- limit = 1,000,000 (maximum constraint): Handled efficiently well within time limits.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def count_circular_primes(limit: int) -> int:
    """Count circular primes strictly less than limit."""
    if limit <= 2:
        return 0

    # Any rotation of a number < limit has the same number of digits.
    # The maximum value of a rotation of any number < limit is bounded by 10^D - 1,
    # where D is the number of digits in (limit - 1).
    max_digits = len(str(limit - 1))
    max_sieve = max(limit, 10**max_digits)

    is_prime = [True] * max_sieve
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_sieve**0.5) + 1):
        if is_prime[i]:
            is_prime[i * i : max_sieve : i] = [False] * len(range(i * i, max_sieve, i))

    invalid_multi_digits = {'0', '2', '4', '5', '6', '8'}
    count = 0

    for p in range(2, limit):
        if not is_prime[p]:
            continue

        if p < 10:
            count += 1
            continue

        s = str(p)
        if any(c in invalid_multi_digits for c in s):
            continue

        length = len(s)
        is_circular = True
        for i in range(1, length):
            rot = int(s[i:] + s[:i])
            if not is_prime[rot]:
                is_circular = False
                break

        if is_circular:
            count += 1

    return count
```
