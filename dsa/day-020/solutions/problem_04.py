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
