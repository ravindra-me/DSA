# Day 6: Day 6: Bit Manipulation Fundamentals

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 6 | 2026-10-15 | Fundamentals | New topic | progressive | Python 3.12 |

Computers store and process everything as sequences of binary digits (bits: 0 and 1). Bit manipulation involves operating directly on these bits using low-level boolean logic and shift operators. Mastering bit operations allows you to execute arithmetic, state tracking, and set operations in $O(1)$ time with negligible memory overhead.

## Topic

**Bit Manipulation**: bitwise operators, masks, XOR tricks, counting set bits, power of two checks

## Learning Objectives

By the end of this lesson you should be able to:

- Understand the six fundamental bitwise operators (&, |, ^, ~, <<, >>) and truth tables.
- Isolate, set, clear, and toggle specific bits using bitmasks.
- Apply Brian Kernighan's algorithm to count set bits in time proportional to the set bits.
- Leverage the algebraic properties of XOR (identity, self-inverse, commutativity) to solve uniqueness problems.
- Detect powers of two and isolate lowest set bits using two's complement arithmetic.

## Concept Explanation

### What it is

At its heart, bit manipulation treats integers not as abstract continuous numbers, but as fixed-width arrays of boolean flags indexed from right ($0$) to left. Instead of using standard arithmetic loops or boolean arrays, we evaluate and transform multiple bits in parallel using hardware-level boolean logic gates.

### Why it exists

Operating on numbers digit-by-digit or using data structures like hash sets and boolean arrays introduces computational and memory overhead. Bit manipulation solves this by executing multiple boolean operations simultaneously in a single CPU instruction, achieving true $O(1)$ time and $O(1)$ space.

### When to use it

Look for clues such as: finding missing or duplicate numbers, powers of two, tracking subsets or combinations of up to 30-60 elements, parity checks, or when constraints strictly require $O(1)$ auxiliary space.

### When NOT to use it

Do not use bit manipulation when representing states larger than word sizes (e.g., beyond 64 bits without BigInt), when standard collections like hash sets improve code clarity without violating constraints, or when floating-point precision is required.

### How it works internally

1. `&` (AND): Result is 1 only if both bits are 1. Used to check or clear bits.
2. `|` (OR): Result is 1 if either bit is 1. Used to set bits.
3. `^` (XOR): Result is 1 if bits differ. Crucial properties: `x ^ 0 = x`, `x ^ x = 0`, and it is commutative and associative.
4. `~` (NOT): Inverts all bits. In two's complement, `~x = -(x + 1)`.
5. `<<` (Left Shift): `x << k` multiplies $x$ by $2^k$.
6. `>>` (Right Shift): `x >> k` divides integer $x$ by $2^k$.
7. Isolating lowest set bit: `x & (-x)`.
8. Clearing lowest set bit: `x & (x - 1)`.

### Common mistakes

- Operator precedence: bitwise operators have lower precedence than comparison operators (`==`, `!=`, `<`, `>`). Always wrap bitwise expressions in parentheses: `(n & 1) == 0` instead of `n & 1 == 0`.
- Python's arbitrary-precision integers: unlike C++/Java 32-bit signed ints, Python integers do not overflow, and negative numbers have infinite leading ones. Use `& 0xFFFFFFFF` when 32-bit behavior is required.
- Assuming `1 << k` handles negative shifts or large shifts greater than system bounds without precision costs.

### Real-world applications

- Operating systems: managing file permissions (chmod rwx) and page allocation flags.
- Networking: subnet masking (IPv4/IPv6 address routing and filtering).
- Graphics & Game Development: packing RGB/RGBA colors into 32-bit integers and tracking state masks.

## Example

Suppose we want to determine if an integer $n = 12$ is a power of two, and count its set bits.

Binary representation of $12$ is `1100` (8 + 4).
1. Check Power of Two: A power of two in binary has exactly one set bit (e.g., `1`, `10`, `100`, `1000`).
   - Formula: `n > 0 and (n & (n - 1)) == 0`
   - $n = 12$ (`1100`)
   - $n - 1 = 11$ (`1011`)
   - $12 \,\&\, 11 = 1100_2 \,\&\, 1011_2 = 1000_2 = 8 \neq 0$.
   - Hence, 12 is not a power of two.

2. Count Set Bits (Kernighan's Algorithm):
   - Step 1: `count = 0`
   - Step 2: `n = n & (n - 1) = 12 & 11 = 8` (`1000`), `count = 1`
   - Step 3: `n = n & (n - 1) = 8 & 7 = 1000_2 & 0111_2 = 0`, `count = 2`
   - Stop since $n = 0$. Total set bits: 2.

## Visual Explanation

```text
Checking and clearing lowest set bit:

   n     = 12 ->  1 1 0 0
   n - 1 = 11 ->  1 0 1 1
   ----------------------
   n & (n - 1) -> 1 0 0 0   (Cleared rightmost 1-bit!)

Isolating the lowest set bit:

   n     = 12 ->  0 0 0 0 1 1 0 0
  -n     =        1 1 1 1 0 1 0 0   (Two's complement: ~n + 1)
   ------------------------------
   n & (-n)   ->  0 0 0 0 0 1 0 0   (= 4, isolated lowest set bit)
```

## Complexity

- **Time Complexity:** O(1) for all primitive bit operations (&, |, ^, ~, <<, >>); O(k) for Kernighan's bit count where k is the number of set bits (at most 32 or 64).
- **Space Complexity:** O(1) auxiliary space as operations act in-place within register-sized integers.

In Python, integers have arbitrary precision. Operations on very large integers scale as O(B) where B is the bit length.

## Interview Perspective

1. **How does `n & (n - 1)` clear the lowest set bit?**
   <details><summary>What a strong answer covers</summary>

   Subtracting 1 flips all bits after the lowest set bit (which are all 0s) to 1s, and turns the lowest set bit itself to 0. All higher bits remain unchanged. ANDing this with the original number zeroes out that specific bit while preserving higher bits.

   </details>
2. **How do you swap two variables without using temporary memory?**
   <details><summary>What a strong answer covers</summary>

   Using XOR: `a = a ^ b`, `b = a ^ b`, `a = a ^ b`. Explain how `(a ^ b) ^ b = a` due to self-inverse and associativity, while noting that in production code this is less readable and modern compilers optimize standard swaps anyway.

   </details>
3. **What is two's complement and why does `x & (-x)` yield the lowest set bit?**
   <details><summary>What a strong answer covers</summary>

   In two's complement, `-x = ~x + 1`. Inverting `x` flips all bits. Adding 1 cascades carries up to the lowest set bit position, leaving all lower bits 0, the lowest set bit 1, and inverting all higher bits. Thus `x & (-x)` preserves only that single bit.

   </details>
4. **How would you determine if an integer is a power of 4 using bit manipulation?**
   <details><summary>What a strong answer covers</summary>

   First verify it is a power of two (`n > 0 and (n & (n - 1)) == 0`). Second, verify that its single set bit resides at an even bit index (0, 2, 4, ...). This can be checked with mask `0x55555555`: `(n & 0x55555555) != 0`.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Power of Two and Hamming Weight](exercises/problem-01.md) | Easy | Power of two checking and bit counting using bitwise operations | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Single Number from Pairs](exercises/problem-02.md) | Easy/Medium | XOR cancellation property | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Reverse Bits of a 32-bit Integer](exercises/problem-03.md) | Medium | Bit extraction and bit assembly with shift operators | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Single Number III (Two Unique Elements)](exercises/problem-04.md) | Medium/Hard | Partitioning elements by distinguishing bit using lowest set bit | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Maximum XOR of Two Numbers in an Array](exercises/problem-05.md) | Hard | Bitwise prefix matching and greedy evaluation with masks | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-006
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Bitwise AND, OR, XOR, NOT, Shifts, Bitmasking (set, get, clear, toggle), Brian Kernighan's Algorithm, Power of Two detection, Two's complement and `n & (-n)`*
