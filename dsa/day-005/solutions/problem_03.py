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
