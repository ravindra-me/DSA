# Day 23: Day 23: Bit Manipulation Revision & Cross-Pattern Synthesis

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 23 | 2026-11-01 | Fundamentals | Revision (stage 1) | progressive | Python 3.12 |

> **Revision day.** You first studied this topic earlier; today recaps the essentials and gives you brand-new problems. (spaced revision due on day 13 of 'bit-manipulation' (learned on day 6))

Bit manipulation treats fixed-width integers as compact, highly efficient vectors of boolean flags. Revisiting this topic allows us to advance from isolated bit tricks to combining masks with prefix sums, monotonic passes, sliding windows, and hashing. By mastering low-level bit invariants, you can solve constraint-heavy interview problems in $O(1)$ auxiliary space and blazing $O(N)$ runtime.

## Topic

**Bit Manipulation**: bitwise operators, masks, XOR tricks, counting set bits, power of two checks

## Learning Objectives

By the end of this lesson you should be able to:

- Recall and apply fundamental bit identities: Brian Kernighan's algorithm (`n & (n - 1)`), lowest set bit extraction (`n & -n`), and power-of-two invariants.
- Formulate integer bitmasks to represent states, sets, and frequency parities (even/odd counts) in $O(1)$ space.
- Combine bit manipulation with prefix state tracking and hash maps to solve sub-array parity and match problems.
- Evaluate bit-by-bit contribution across arrays to avoid expensive nested pair/triplet comparisons.

## Concept Explanation

### What it is

At its core, bit manipulation leverages hardware-level binary operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to manipulate numeric representations directly. Instead of managing arrays of booleans or hash sets for small finite universes (like lowercase letters a-z), an integer's binary representation serves as an immutable, cache-friendly bitset.

### Why it exists

Traditional set and array operations introduce pointer dereferences, heap allocations, and constant factor overheads. A 32-bit or 64-bit word can perform up to 64 parallel boolean operations in a single CPU clock cycle. Furthermore, arithmetic and XOR invariants allow us to cancel matching elements, isolate lowest set bits, and check parity without branching.

### When to use it

Look for bit manipulation when: (1) Elements repeat in pairs/triples with an odd-one-out, (2) State needs to be represented for a small alphabet (e.g., lowercase letters, 0-9 digits), (3) Problems ask for XOR-sums, subsets, or combinations, (4) In-place, $O(1)$ auxiliary space is explicitly required.

### When NOT to use it

Do not use bit manipulation when the number of distinct states or the universe size exceeds the integer width of the platform (unless using arbitrary-precision integers, which negates single-cycle hardware efficiency), or when code readability and maintenance outweigh microseconds of latency in non-bottleneck routines.

### How it works internally

Key operational invariants:
- `n & (n - 1)` clears the least significant set bit (LSSB). Repeating this counts set bits in $O(k)$ steps where $k$ is the number of ones.
- `n & -n` isolates the least significant set bit using two's complement arithmetic (`-n = ~n + 1`).
- `x ^ x = 0` and `x ^ 0 = x`: XOR is associative and commutative; duplicate values cancel out regardless of order.
- `1 << k` creates a mask with only the $k$-th bit set. `mask | (1 << k)` sets bit $k$, `mask & ~(1 << k)` clears bit $k$, and `(mask >> k) & 1` checks bit $k$.

### Common mistakes

- Operator Precedence: Comparison (`==`, `<`, `!=`) and addition (`+`) have higher precedence in Python than bitwise operators (`&`, `^`, `|`). Always wrap bitwise operations in parentheses: `(n & 1) == 0`, not `n & 1 == 0`.
- Arbitrary-Precision Negation in Python: Python integers have arbitrary precision (no fixed 32-bit overflow). `~0` is `-1`, not `0xFFFFFFFF`. Mask explicitly with `& 0xFFFFFFFF` when emulating 32-bit registers.
- Zero Checks for Powers of Two: `n & (n - 1) == 0` is true for `n = 0`, but 0 is not a power of two. Always enforce `n > 0`.
- Off-by-one shifts: Shifting by $\ge 32$ or $\ge 64$ in fixed-width languages causes undefined behavior. In Python, it keeps growing, consuming unexpected memory.

### Real-world applications

- Network routing and subnetting (CIDR masks matching IP prefixes).
- Database Bloom filters and indexing bitmap indices for lightning-fast set membership.
- Cryptography (AES s-boxes, stream ciphers, and hash functions like SHA-256).
- Graphics rendering and game development (collision masks, state flags, pixel format unpacking).

## Example

Suppose we want to find the length of the longest substring with at most one character having an odd frequency (i.e., characters can be rearranged to form a palindrome).

String: `"a a b c c b"`
1. Represent character parity as a 26-bit mask where bit `i` is toggled whenever character `i` appears.
2. Maintain `first_seen[mask] = index`. Initialize `first_seen[0] = -1`.
3. Traverse:
   - `i = 0`, char `'a'`: mask becomes `001` (binary 1). `first_seen[1] = 0`.
   - `i = 1`, char `'a'`: mask becomes `000` (binary 0). `0` was seen at `-1` -> len = `1 - (-1) = 2`.
   - Check single bit flips (`mask ^ (1 << k)`): matching any previous mask with 1 bit difference allows 1 odd char.
4. This converts an $O(N^2)$ frequency table check into an $O(26 \cdot N) = O(N)$ single-pass solution.

## Visual Explanation

```text
Extracting the Lowest Set Bit (LSSB):

     n     =  12 (1100 in binary)
    ~n     =  ...11110011 (inversion)
-n = ~n+1  =  ...11110100 (two's complement)
----------------------------------------
  n & (-n) =  00000100 (4 in decimal - exactly the lowest set bit!)

Clearing the Lowest Set Bit:

     n     =  12 (1100)
   n - 1   =  11 (1011)
----------------------------------------
 n & (n-1) =  8  (1000) -> Lowest 1 has been flipped to 0.
```

## Complexity

- **Time Complexity:** Bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`): $O(1)$ per operation on fixed-width words. Kernighan's counting: $O(k)$ where $k$ is the number of set bits.
- **Space Complexity:** $O(1)$ auxiliary space for tracking bitmasks and state words.

Python automatically promotes integers to arbitrary precision if they exceed 64 bits. While convenient, operations on huge masks (e.g., thousands of bits) scale with $O(M)$ where $M$ is the number of bits.

## Interview Perspective

1. **How do you swap two variables without using a temporary variable, and what are its caveats?**
   <details><summary>What a strong answer covers</summary>

   Use XOR swap: `a ^= b; b ^= a; a ^= b`. Point out that modern compilers optimize standard swaps with register moves anyway, and if `a` and `b` reference the exact same memory location (aliases), XOR swap zeroes out the value.

   </details>
2. **Why does `n & (n - 1)` clear the lowest set bit?**
   <details><summary>What a strong answer covers</summary>

   Explain that subtracting 1 flips all bits after the rightmost 1 (from 0 to 1) and flips the rightmost 1 itself to 0. Performing bitwise AND with the original number leaves all higher bits intact while turning the rightmost 1 into 0.

   </details>
3. **How do you detect if an unsigned integer is a power of 4?**
   <details><summary>What a strong answer covers</summary>

   First verify it is a power of two: `n > 0 and (n & (n - 1)) == 0`. Then ensure the single set bit is in an odd position (0-indexed: 0, 2, 4, ...). In 32-bit integers, mask with `0x55555555` (`n & 0x55555555 != 0`). Alternatively, verify `(n - 1) % 3 == 0`.

   </details>
4. **How can you iterate through all submasks of a given mask in $O(3^N)$ instead of $O(4^N)$?**
   <details><summary>What a strong answer covers</summary>

   Explain the submask enumeration trick: `sub = mask; while sub > 0: sub = (sub - 1) & mask`. Show that by summing binomial coefficients $\sum \binom{n}{k} 2^k = (1 + 2)^n = 3^n$, traversing all submasks over all masks takes $O(3^n)$ time.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Subsets Generation via Bitmasks](exercises/problem-01.md) | Easy/Medium | Power set generation using binary integers as inclusion/exclusion masks | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Single Number II: Elements Appearing Three Times](exercises/problem-02.md) | Medium | Bit counting modulo 3 / finite-state machine with bitwise logic | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Sum of Hamming Distances of All Pairs](exercises/problem-03.md) | Medium/Hard | Bit-by-bit contribution counting across array elements | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Find Longest Awesome Substring](exercises/problem-04.md) | Medium/Hard | Prefix parity bitmask combined with hash map for palindrome eligibility | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Minimum XOR Sum of Two Arrays](exercises/problem-05.md) | Hard | Bitmask Dynamic Programming over permutations | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-023
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Bitwise operators (&, |, ^, ~, <<, >>), Brian Kernighan's bit-clearing invariant, Lowest set bit extraction (n & -n), Prefix bitmasks with hash tables, Bit-level aggregation and contribution counting*
