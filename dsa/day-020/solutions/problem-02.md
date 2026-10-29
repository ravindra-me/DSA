# Solution 2: Kth Digit of a Geometric Product

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Medium | **Concept:** Fast Modular Exponentiation and Logarithmic Math

## Approach

We need to compute $P = a^n \cdot r^{\frac{n(n-1)}{2}} \pmod{10^k}$. Since $10^k$ is composite and Euler's totient theorem with modular exponentiation in the exponent can get tricky, we can directly compute the exponent $E = \frac{n(n-1)}{2}$ using standard integer arithmetic (since Python supports arbitrarily large integers and $n \le 10^9$ means $E \approx 5 \cdot 10^{17}$, which fits within standard 64-bit integer ranges) and use binary exponentiation (`pow(base, exp, mod)`) modulo $10^k$.

## Thought Process

A naive approach might multiply the sequence term by term, taking modulo $10^k$ at each step. However, $n$ can be up to $10^9$, making an $O(n)$ loop impossible to finish within standard time limits (1-2 seconds).

The closed-form formula gives $P = a^n \cdot r^{n(n-1)/2}$. Notice that $n(n-1)$ is always an even number, so $E = n(n-1) // 2$ is an exact integer without fractional parts. In Python, integers have arbitrary precision, and $n \le 10^9$ yields an exponent of at most $\approx 5 \cdot 10^{17}$.

Modular exponentiation $\text{pow}(x, y, m)$ runs in $O(\log y)$ time using repeated squaring. Thus, we can compute $T_1 = a^n \pmod{10^k}$ and $T_2 = r^E \pmod{10^k}$ separately, each taking $O(\log(\text{exponent}))$ steps. Finally, the result is $(T_1 \cdot T_2) \pmod{10^k}$.

## Algorithm

1. Compute the modulus $M = 10^k$.
2. Compute the exponent $E = n \cdot (n - 1) // 2$ using exact integer arithmetic.
3. Compute $T_1 = a^n \pmod M$ using fast modular exponentiation (`pow(a, n, M)`).
4. Compute $T_2 = r^E \pmod M$ using fast modular exponentiation (`pow(r, E, M)`).
5. Return $(T_1 \cdot T_2) \pmod M$.

## Complexity Analysis

- **Time:** $O(\log n)$ because binary exponentiation of $a^n \pmod M$ takes $O(\log n)$ steps and $r^{O(n^2)} \pmod M$ takes $O(\log(n^2)) = O(\log n)$ steps.
- **Space:** $O(1)$ auxiliary space as we only store a few scalar integer variables.

## Edge Cases

- $n = 1$: The exponent $n(n-1)//2 = 0$, so $r^0 = 1$, correctly giving $a^1 \pmod{10^k}$.
- $k = 9$: $M = 10^9$, operations easily fit within 64-bit bounds and Python handles them without overflow.
- $a, r, n$ at maximum constraint $10^9$: Exponent is $\approx 5 \cdot 10^{17}$, handled in $\approx 60$ multiplications via binary exponentiation.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
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
```
