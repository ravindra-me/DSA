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
