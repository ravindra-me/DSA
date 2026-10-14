# Day 5: Basic Mathematics for DSA: Number Theory, Modular Arithmetic, and Fast Operations

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 5 | 2026-10-14 | Fundamentals | New topic | progressive | Python 3.12 |

Every competitive programmer and backend engineer eventually encounters problems that require working with numbers beyond brute-force iteration. Whether counting divisors, handling huge quantities without numeric overflow, or finding primes up to billions, core mathematical primitives allow us to turn $O(N)$ operations into logarithmic or sublinear solutions. Today we build the mathematical toolbox that serves as the foundation for hashing, cryptography, dynamic programming, and combinatorics.

## Topic

**Basic Mathematics for DSA**: GCD/LCM, primes & sieve, modular arithmetic, fast exponentiation, digit manipulation

## Learning Objectives

By the end of this lesson you should be able to:

- Manipulate digits mathematically using division and modulo without resorting to slow string conversions.
- Compute the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) in logarithmic time using the Euclidean Algorithm.
- Perform modular arithmetic safely without integer overflow or negative remainder bugs.
- Compute large powers in $O(\log N)$ time using binary exponentiation.
- Generate prime numbers up to $N$ in $O(N \log \log N)$ using the Sieve of Eratosthenes.

## Concept Explanation

### What it is

Basic Mathematics for DSA covers fundamental computational number theory: extracting digits via base-10 arithmetic, finding common factors (GCD/LCM), testing and generating prime numbers efficiently, handling cyclic arithmetic (modulo), and exponentiating numbers rapidly by halving powers. Rather than simulating processes step-by-step, these algorithms exploit algebraic properties of integers to skip vast amounts of computation.

### Why it exists

Computers have physical constraints on time and space. A brute-force check to determine if $N = 10^{14}$ is prime by checking every number up to $N$ would take days. Similarly, calculating $2^{10^9}$ by multiplying 2 iteratively takes a billion operations and produces a number too large to fit in physical RAM. Basic mathematical principles provide mathematical shortcuts: testing primes only up to $\sqrt{N}$, halving exponents in binary exponentiation to finish in 30 steps, and wrapping large numbers around a modulo (like $10^9 + 7$) so intermediate results fit in standard register sizes.

### When to use it

Use these tools when a problem mentions primes, factors, divisibility, or coprimality; when an answer must be returned modulo $10^9 + 7$ or another prime; when exponents are large ($N \ge 10^5$); or when problems require digit reversal, palindrome number verification, or finding cycles.

### When NOT to use it

Do not use heavy number-theoretic machinery if $N$ is tiny (e.g., $N \le 10$) where simple iteration is easier to read and maintain. Avoid modular division unless you are certain the modulus is prime (which permits Fermat's Little Theorem) or numbers are coprime (which permits the Extended Euclidean Algorithm). Avoid precomputing primes via a sieve if you only query a single large number—use trial division up to $\sqrt{N}$ instead.

### How it works internally

1. **Digit Extraction**: Any integer $N$ in base $b$ can yield its least significant digit with `N % b` and be shifted right with `N // b`. Repeating until $N = 0$ inspects all digits in $O(\log_{10} N)$ time.

2. **Euclidean Algorithm for GCD**: Based on the invariant $\gcd(a, b) = \gcd(b, a \pmod b)$. At each step, the larger number is reduced by at least half every two steps, running in $O(\log(\min(a, b)))$. $\text{lcm}(a, b) = (a \cdot b) / \gcd(a, b)$.

3. **Modular Arithmetic**: Addition, subtraction, and multiplication preserve equivalence modulo $M$:
- $(a + b) \pmod M = ((a \pmod M) + (b \pmod M)) \pmod M$
- $(a - b) \pmod M = ((a \pmod M) - (b \pmod M) + M) \pmod M$
- $(a \times b) \pmod M = ((a \pmod M) \times (b \pmod M)) \pmod M$

4. **Binary Exponentiation**: To compute $a^b$, express $b$ in binary. If $b$ is even, $a^b = (a^2)^{b/2}$. If $b$ is odd, $a^b = a \times a^{b-1}$. This reduces multiplications from $O(b)$ to $O(\log b)$.

5. **Sieve of Eratosthenes**: To find all primes up to $N$, allocate a boolean array of size $N+1$. Mark 0 and 1 as non-prime. Iterate $p$ from 2 up to $\sqrt{N}$. If $p$ is prime, mark all multiples $p^2, p^2+p, p^2+2p, \dots$ as composite. Multiple marking starts at $p^2$ because smaller multiples have already been marked by smaller prime factors.

### Common mistakes

- Negative Modulo in Python vs Other Languages: In Python, `-1 % 5` is `4`, whereas in C++/Java `-1 % 5` is `-1`. When writing cross-language modular arithmetic, always use `(a % m + m) % m` to ensure non-negative outputs.
- Integer Overflow in LCM: Computing `(a * b) // gcd(a, b)` can cause intermediate integer overflow in fixed-width integer languages. Always divide first: `(a // gcd(a, b)) * b`.
- Sieve Memory Limit: Allocating an array of booleans for $N > 10^8$ will exceed the standard 256MB memory limit. Recognize when $N$ requires a segmented sieve or direct $\sqrt{N}$ trial division.
- Modulo Division Fallacy: Assuming $(a / b) \pmod M = ((a \pmod M) / (b \pmod M)) \pmod M$. Division under modulo requires calculating the modular multiplicative inverse via Fermat's Little Theorem or the Extended Euclidean Algorithm.
- String Conversion for Digit Math: Converting integers to strings (e.g. `str(n)`) introduces memory allocations and has $O(D^2)$ hidden costs in languages with arbitrary precision when numbers grow very large.

### Real-world applications

- Public-Key Cryptography (RSA & Diffie-Hellman): Relies heavily on fast modular exponentiation, large prime generation, and finding modular inverses.
- Hash Functions and Hash Maps: Hash buckets wrap arbitrary object hashes into table bounds using modulo $M$ where $M$ is typically chosen as a prime to minimize collisions.
- Random Number Generators: Linear Congruential Generators (LCGs) generate pseudorandom sequences using the recurrence $X_{n+1} = (aX_n + c) \pmod m$.
- Aspect Ratio & Screen Scaling: Video encoders and window managers compute the GCD of display dimensions (e.g., 1920x1080 -> GCD 120 -> 16:9) to maintain proportions.

## Example

Let's trace **Binary Exponentiation** to compute $3^{13} \pmod{1000}$:
1. Target exponent: $13$, which is binary `1101` ($8 + 4 + 1$).
2. Maintain `result = 1`, `base = 3`, `power = 13`.
- Step 1: `power = 13` (odd).
  `result = (result * base) % 1000 = (1 * 3) % 1000 = 3`.
  `base = (base * base) % 1000 = (3 * 3) % 1000 = 9`.
  `power = 13 // 2 = 6`.
- Step 2: `power = 6` (even).
  `base = (base * base) % 1000 = (9 * 9) % 1000 = 81`.
  `power = 6 // 2 = 3`.
- Step 3: `power = 3` (odd).
  `result = (result * base) % 1000 = (3 * 81) % 1000 = 243`.
  `base = (base * base) % 1000 = (81 * 81) % 1000 = 6561 % 1000 = 561`.
  `power = 3 // 2 = 1`.
- Step 4: `power = 1` (odd).
  `result = (result * base) % 1000 = (243 * 561) % 1000 = 136323 % 1000 = 323`.
  `base = (561 * 561) % 1000 = 721`.
  `power = 1 // 2 = 0`.
3. Loop terminates. Final result is `323` in just 4 iterations instead of 13 multiplications.

## Visual Explanation

```text
EUCLIDEAN GCD ALGORITHM: gcd(48, 18)
  Step 1: 48 % 18 = 12   -->  gcd(18, 12)
  Step 2: 18 % 12 = 6    -->  gcd(12, 6)
  Step 3: 12 % 6  = 0    -->  gcd(6, 0)
  Base case reached (b == 0): Answer is 6.

SIEVE OF ERATOSTHENES (N = 16):
Initial: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
p = 2:   Cross out 4, 6, 8, 10, 12, 14, 16 (multiples starting from 2^2=4)
p = 3:   Cross out 9, 15 (multiples starting from 3^2=9; 6, 12 already crossed)
p = 4 > sqrt(16)=4: Stop.
Primes remaining: [2, 3, 5, 7, 11, 13]
```

## Complexity

- **Time Complexity:** Digit Extraction: O(log_10 N) - one iteration per decimal digit; Euclidean GCD: O(log(min(a, b))) - numbers reduce by at least factor of 2 every two iterations; Binary Exponentiation: O(log exponent) - exponent is halved at each step; Sieve of Eratosthenes: O(N log log N) - harmonic sum over primes.
- **Space Complexity:** Euclidean GCD & Binary Exponentiation: O(1) iterative space; Sieve of Eratosthenes: O(N) space to store the boolean primality array.

The Sieve of Eratosthenes runs in $O(N \log \log N)$, which in practice is virtually linear because $\log \log N \le 5$ for any $N$ fitting in typical memory ($N < 10^9$). Trial division up to $\sqrt{N}$ takes $O(\sqrt{N})$ time and $O(1)$ space, making it preferable if you only need to check primality for a single number.

## Interview Perspective

1. **Why does the inner loop of the Sieve of Eratosthenes start at p * p instead of 2 * p?**
   <details><summary>What a strong answer covers</summary>

   Any multiple $k \times p$ where $k < p$ must have a prime factor strictly smaller than $p$. Therefore, that multiple would have already been marked composite when that smaller prime factor was processed earlier.

   </details>
2. **How do you compute (A / B) % M when working with modular arithmetic?**
   <details><summary>What a strong answer covers</summary>

   You cannot simply divide. You must multiply $A$ by the modular multiplicative inverse of $B$ modulo $M$. If $M$ is prime, by Fermat's Little Theorem, $B^{-1} \equiv B^{M-2} \pmod M$. Compute $B^{M-2} \pmod M$ using fast exponentiation, then multiply by $A$ modulo $M$.

   </details>
3. **Why is the time complexity of the Euclidean algorithm O(log(min(a, b)))?**
   <details><summary>What a strong answer covers</summary>

   For any two integers $a \ge b$, $a \pmod b < a / 2$. This guarantees that after at most every two reduction steps, the larger number is at least halved, bounding the maximum recursion depth or iterations to $2 \log_2(\min(a, b))$.

   </details>
4. **How would you handle negative inputs when implementing a digit-reversal or palindrome-checking algorithm?**
   <details><summary>What a strong answer covers</summary>

   Clarify requirements with the interviewer: negative numbers often cannot be palindromes due to the leading negative sign (e.g. `-121` reversed is `121-`). For digit reversal, preserve the sign, process the absolute value, and reapply the sign, checking for integer overflow limits if working under 32-bit limits.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Reverse Integer with Overflow Guard](exercises/problem-01.md) | Easy | Digit extraction and arithmetic overflow handling | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Pairwise Array Reduction](exercises/problem-02.md) | Easy/Medium | Euclidean GCD and LCM across multiple values | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Prime Factor Counting Queries](exercises/problem-03.md) | Medium | Sieve of Eratosthenes with precomputed Smallest Prime Factor (SPF) | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Modular Exponentiation Matrix Series](exercises/problem-04.md) | Medium/Hard | Fast binary exponentiation and modular arithmetic properties | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Prime Counting in Ranges (Segmented Sieve)](exercises/problem-05.md) | Hard | Segmented Sieve of Eratosthenes | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-005
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Digit Extraction and Reversal, Euclidean GCD and LCM, Modular Arithmetic Invariants, Binary Exponentiation, Sieve of Eratosthenes*
