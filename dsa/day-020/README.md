# Day 20: Day 20: Basic Mathematics for DSA (Revision & Advanced Applications)

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 20 | 2026-10-29 | Fundamentals | Revision (stage 1) | progressive | Python 3.12 |

> **Revision day.** You first studied this topic earlier; today recaps the essentials and gives you brand-new problems. (spaced revision due on day 12 of 'math-basics' (learned on day 5))

Mathematical principles form the backbone of efficient algorithm design, allowing us to bypass brute-force loops and compute solutions analytically. This revision solidifies your intuition for prime factorization, modular arithmetic, GCD/LCM, and logarithmic-time exponentiation, combining them with hash maps, arrays, and queues to tackle non-trivial interview challenges.

## Topic

**Basic Mathematics for DSA**: GCD/LCM, primes & sieve, modular arithmetic, fast exponentiation, digit manipulation

## Learning Objectives

By the end of this lesson you should be able to:

- Leverage the Euclidean algorithm and prime factorization properties to resolve divisibility and frequency problems efficiently.
- Correctly apply modular arithmetic rules (addition, multiplication, modular inverse) without falling into negative modulo or precision traps.
- Implement binary exponentiation iteratively and recursively in $O(\log n)$ time.
- Combine prime sieving and digit manipulation with hash maps and frequency counting to construct optimal multi-step algorithms.

## Concept Explanation

### What it is

Basic mathematics in DSA encompasses number theory tools—such as Greatest Common Divisor (GCD), the Sieve of Eratosthenes, modular arithmetic, fast exponentiation (binary exponentiation), and digit decomposition—that turn exponential or linear processes into logarithmic or sublinear solutions.

### Why it exists

Without mathematical properties, computing $a^b$ takes $O(b)$ operations, checking primality up to $N$ takes $O(N \sqrt{N})$, and large values overflow integer limits or exceed execution time budgets. Math primitives reduce complex combinatorial or repetitive operations into bounded, closed-form, or logarithmic algorithms.

### When to use it

Use these tools when problem statements mention remainders ($X \pmod M$), pairs satisfying divisibility rules, powers of large integers, prime factors, counting digit patterns, or cycle detection via modular periods.

### When NOT to use it

Do not over-engineer with number theory when simple two-pointer or sliding-window approaches suffice on unstructured data. Avoid full factorizations when testing small, finite prime sets or simple modulo conditions.

### How it works internally

1. **Euclidean GCD**: $\gcd(a, b) = \gcd(b, a \pmod b)$, terminating when remainder is 0 in $O(\log(\min(a, b)))$.\n2. **Binary Exponentiation**: Express exponent $n$ in base 2; compute $a^n$ by repeatedly squaring the base and multiplying whenever the current bit of $n$ is 1.\n3. **Sieve of Eratosthenes**: Mark multiples of each prime starting from $p^2$ up to $N$; runs in $O(N \log \log N)$.\n4. **Modular Arithmetic**: Distribute modulo across addition and multiplication: $(a \cdot b) \pmod m = ((a \pmod m) \cdot (b \pmod m)) \pmod m$. Division requires modular inverse via Fermat's Little Theorem ($a^{m-2} \pmod m$) when $m$ is prime.

### Common mistakes

- Negative modulo handling: In Python, `-1 % k` is positive, but in languages like C++/Java it is negative. Always ensure consistency when designing modular mappings: `(val % k + k) % k`.
- Division under modulo: Dividing directly before taking modulo (i.e. `(a / b) % MOD`) gives incorrect results; you must multiply by the modular inverse of `b`.
- Ignoring prime edge cases: Treating 0 or 1 as prime, or forgetting that 2 is the only even prime.
- Sieve starting point: Forgetting that composite marking for prime $p$ can start at $p \times p$, leading to redundant operations.

### Real-world applications

- Cryptography: RSA and Diffie-Hellman key exchanges depend entirely on fast modular exponentiation and prime factorization hardness.
- Hashing & Distributed Systems: Consistent hashing rings, hash table bucket indexing, and rolling hashes (Rabin-Karp) use modular arithmetic.
- Game Engines & Graphics: Cycle generators, deterministic pseudo-random number generation (Linear Congruential Generators), and coordinate wrapping.

## Example

Computing $3^{13} \pmod{1000}$ using Binary Exponentiation:\n- $13$ in binary is $1101_2$ ($13 = 8 + 4 + 1$).\n- Initialize `result = 1`, `base = 3`.\n- Bit 0 is 1: `result = (1 * 3) % 1000 = 3`; `base = (3 * 3) % 1000 = 9`.\n- Bit 1 is 0: `result` unchanged; `base = (9 * 9) % 1000 = 81`.\n- Bit 2 is 1: `result = (3 * 81) % 1000 = 243`; `base = (81 * 81) % 1000 = 6561 % 1000 = 561`.\n- Bit 3 is 1: `result = (243 * 561) % 1000 = 136323 % 1000 = 323$.\nResult is $323$ in just 4 iterations instead of 13 multiplications.

## Visual Explanation

```text
Binary Exponentiation of base=a, exp=13 (binary: 1101):

Bit 0 (LSB = 1): result = (1 * a)       | base = a^2
Bit 1 (bit = 0): result unchanged       | base = (a^2)^2 = a^4
Bit 2 (bit = 1): result = result * a^4  | base = (a^4)^2 = a^8
Bit 3 (MSB = 1): result = result * a^8  | Done!

Euclidean Algorithm: gcd(48, 18)
  48 % 18 = 12  ==> gcd(18, 12)
  18 % 12 =  6  ==> gcd(12, 6)
  12 %  6 =  0  ==> return 6
```

## Complexity

- **Time Complexity:** GCD: O(log(min(a, b))) via Euclidean algorithm; Fast Power: O(log exp); Sieve of Eratosthenes: O(N log log N).
- **Space Complexity:** GCD: O(1) iterative; Fast Power: O(1) iterative; Sieve: O(N) boolean array.

Fast exponentiation reduces operations from linear to logarithmic in exponent size. Sieve allows O(1) primality queries after O(N log log N) preprocessing.

## Interview Perspective

1. **How do you compute (a / b) % MOD when MOD is a prime number?**
   <details><summary>What a strong answer covers</summary>

   By Fermat's Little Theorem, if MOD is prime and gcd(b, MOD) = 1, then b^(MOD - 1) ≡ 1 (mod MOD), which implies b^(MOD - 2) ≡ b^(-1) (mod MOD). Compute b^(MOD - 2) % MOD using fast exponentiation and multiply by a % MOD.

   </details>
2. **Why does the inner loop of the Sieve of Eratosthenes start at p * p instead of 2 * p?**
   <details><summary>What a strong answer covers</summary>

   Any composite number k * p with k < p has already been marked by a smaller prime factor of k during an earlier iteration of the outer loop.

   </details>
3. **How can you count the total number of trailing zeroes in n! without computing n!?**
   <details><summary>What a strong answer covers</summary>

   Trailing zeroes are produced by factors of 10 = 2 * 5. Since factors of 2 are always more frequent than factors of 5, count multiples of 5: floor(n/5) + floor(n/25) + floor(n/125) + ... until floor(n / 5^k) = 0.

   </details>
4. **What is the difference in handling negative dividends in Python vs C++/Java with the modulo operator?**
   <details><summary>What a strong answer covers</summary>

   In Python, modulo follows floored division (the sign matches the divisor, so -7 % 3 = 2). In C++ and Java, modulo follows truncated division (the sign matches the dividend, so -7 % 3 = -1). To ensure non-negative results uniformly: (val % mod + mod) % mod.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Subarray Sum Divisibility Counter](exercises/problem-01.md) | Easy/Medium | Modular Arithmetic with Hash Map Prefix Sums | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Kth Digit of a Geometric Product](exercises/problem-02.md) | Medium | Fast Modular Exponentiation and Logarithmic Math | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Coprime Component Groups](exercises/problem-03.md) | Medium/Hard | GCD & Prime Factorization Graph Reduction | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Prime Digit Circular Shifts](exercises/problem-04.md) | Medium/Hard | Sieve of Eratosthenes & Digit Manipulation | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Modular Combination Sequence Queries](exercises/problem-05.md) | Hard | Modular Arithmetic, Factorial Precomputation & Fermat's Inverse | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-020
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Euclidean GCD, LCM, Binary Exponentiation, Sieve of Eratosthenes, Modular Arithmetic & Inverses, Digit Manipulation*
