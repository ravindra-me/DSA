# Solution 4: Modular Exponentiation Matrix Series

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Fast binary exponentiation and modular arithmetic properties

## Approach

We can compute the geometric series sum $S_k = \sum_{i=0}^k a^i \pmod m$ in $O(\log k)$ time using either divide-and-conquer recursion or $2 \times 2$ matrix exponentiation. Representing the transition as $\begin{pmatrix} S_i \\ 1 \end{pmatrix} = \begin{pmatrix} a & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} S_{i-1} \\ 1 \end{pmatrix}$, computing $\begin{pmatrix} a & 1 \\ 0 & 1 \end{pmatrix}^{k+1}$ gives $S_k$ directly modulo $m$ without requiring modular inverses.

## Thought Process

A naive loop takes $O(k)$ time, which TLEs when $k = 10^9$. Because $m$ is not necessarily prime and $\gcd(a - 1, m)$ might not be $1$, the standard closed form $\frac{a^{k+1} - 1}{a - 1}$ cannot simply use modular inverse division.

Two primary $O(\log k)$ approaches exist:
1. **Divide-and-Conquer**: $S(n) = \sum_{i=0}^{n-1} a^i$. When $n$ is even, $S(n) = (1 + a^{n/2}) S(n/2)$. When $n$ is odd, $S(n) = 1 + a \cdot S(n-1)$.
2. **Matrix Exponentiation**: Notice that $S_{i} = a \cdot S_{i-1} + 1$, with $S_0 = 1$. In matrix form:
   $$\begin{pmatrix} S_i \\ 1 \end{pmatrix} = \begin{pmatrix} a & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} S_{i-1} \\ 1 \end{pmatrix}$$
   Repeated multiplication gives:
   $$\begin{pmatrix} S_k \\ 1 \end{pmatrix} = \begin{pmatrix} a & 1 \\ 0 & 1 \end{pmatrix}^k \begin{pmatrix} S_0 \\ 1 \end{pmatrix} = \begin{pmatrix} a & 1 \\ 0 & 1 \end{pmatrix}^k \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$
   Equivalently, setting $S_{-1} = 0$, we have $\begin{pmatrix} a & 1 \\ 0 & 1 \end{pmatrix}^{k+1} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} S_k \\ 1 \end{pmatrix}$, so $S_k$ is the top-right entry of $\begin{pmatrix} a & 1 \\ 0 & 1 \end{pmatrix}^{k+1} \pmod m$.

Binary exponentiation on $2 \times 2$ matrices executes in $\approx 8 \times \log_2(k+1)$ scalar multiplications, cleanly avoiding modular division entirely and handling all cases including $a = 0$ and $a = 1$.

## Algorithm

1. Handle the base reduction $a = a \pmod m$. If $k = 0$, return $1 \pmod m$.
2. Define a helper function to multiply two $2 \times 2$ matrices modulo $m$.
3. Define matrix binary exponentiation to raise a $2 \times 2$ matrix $M$ to power $p$ modulo $m$. Initialize the result as the $2 \times 2$ identity matrix.
4. Form the transition matrix $T = \begin{pmatrix} a \pmod m & 1 \\ 0 & 1 \end{pmatrix}$.
5. Compute $T^{k+1} \pmod m$ using matrix binary exponentiation.
6. Since $S_{-1} = 0$, $T^{k+1} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} S_k \\ 1 \end{pmatrix}$. The value of $S_k \pmod m$ is the element in row 0, column 1 of $T^{k+1}$.
7. Return this value modulo $m$.

## Complexity Analysis

- **Time:** $O(\log k)$ because $2 \times 2$ matrix multiplication is $O(1)$ operations and binary exponentiation takes $O(\log k)$ steps.
- **Space:** $O(1)$ auxiliary memory since we only maintain a few $2 \times 2$ matrices during the exponentiation.

## Edge Cases

- k = 0: Returns 1 % m directly (e.g. 1 % 2 = 1).
- a = 0: The series is 0^0 + 0^1 + ... = 1 + 0 + ... = 1 % m for all k >= 0.
- a = 1: The series is 1 + 1 + ... + 1 = (k + 1) % m. The matrix exponentiation naturally evaluates this as the top-right entry becomes k + 1.
- m divides a (a % m == 0): The series reduces to 1 % m.
- Large k up to 10^9: Handled efficiently in ~30 matrix multiplication steps.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
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
```
