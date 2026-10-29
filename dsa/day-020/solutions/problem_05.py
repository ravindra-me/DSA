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
