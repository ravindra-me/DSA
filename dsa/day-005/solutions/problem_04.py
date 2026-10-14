def geometric_sum_mod(a: int, k: int, m: int) -> int:
    """Computes (sum_{i=0}^k a^i) % m in O(log k) time."""
    if m <= 0:
        raise ValueError("Modulo m must be positive.")
    if k < 0:
        raise ValueError("Exponent k must be non-negative.")
    if k == 0:
        return 1 % m

    a_mod = a % m

    def mat_mul_2x2(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
        return [
            [
                (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % m,
                (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % m,
            ],
            [
                (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % m,
                (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % m,
            ],
        ]

    def mat_pow_2x2(M: list[list[int]], power: int) -> list[list[int]]:
        res = [[1, 0], [0, 1]]
        base = [[M[0][0] % m, M[0][1] % m], [M[1][0] % m, M[1][1] % m]]
        while power > 0:
            if power & 1:
                res = mat_mul_2x2(res, base)
            base = mat_mul_2x2(base, base)
            power >>= 1
        return res

    # Transition matrix: [[a, 1], [0, 1]]
    # [[a, 1], [0, 1]]^(k+1) * [[0], [1]] = [[S_k], [1]]
    # Therefore, S_k is the top-right element of T^(k + 1).
    transition = [[a_mod, 1 % m], [0, 1 % m]]
    result_matrix = mat_pow_2x2(transition, k + 1)
    return result_matrix[0][1]
