def kth_digit_geometric_product(a: int, r: int, n: int, k: int) -> int:
    """Compute the last k digits of the product of the first n terms of a geometric sequence.

    The sequence is a, a*r, a*r^2, ..., a*r^(n-1).
    The product is a^n * r^(n*(n-1)/2).
    """
    mod = 10**k
    exp_r = n * (n - 1) // 2
    term_a = pow(a, n, mod)
    term_r = pow(r, exp_r, mod)
    return (term_a * term_r) % mod
