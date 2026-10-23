# Day 14: Day 14: Strings (Revision & Advanced Synthesis)

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 14 | 2026-10-23 | Fundamentals | Revision (stage 1) | progressive | Python 3.12 |

> **Revision day.** You first studied this topic earlier; today recaps the essentials and gives you brand-new problems. (spaced revision due on day 10 of 'strings' (learned on day 3))

In this revision lesson, we revisit strings with an emphasis on performance invariants, memory representation, and multi-concept synthesis. We examine how string immutability in Python affects time complexity and how to combine string manipulations with stacks, queues, and two-pointer invariants. By mastering linear-time transformations and state-driven parsing, you will solve complex, interview-grade string problems cleanly and efficiently.

## Topic

**Strings**: immutability, character manipulation, palindromes, anagrams, string building

## Learning Objectives

By the end of this lesson you should be able to:

- Analyze the hidden $O(N)$ cost of Python string concatenations and systematically apply $O(N)$ string-building patterns.
- Formulate two-pointer invariants to evaluate palindrome transformations and substrings without redundant allocations.
- Utilize frequency arrays, bitmasks, and sliding counters to verify anagrams and permutation properties.
- Integrate auxiliary data structures such as monotonic stacks and queues to parse and transform structured string inputs in linear time.

## Concept Explanation

### What it is

A string is an immutable sequence of characters laid out contiguously in memory. In Python 3, strings (`str`) are encoded internally using the most compact representation necessary (Latin-1, UCS-2, or UCS-4 depending on the maximum code point via PEP 393). Because strings are immutable, modifying a character or appending characters with naive `+=` in a loop typically allocates a completely new string, copying all preceding characters and turning an intended $O(N)$ process into an $O(N^2)$ bottleneck.

### Why it exists

Immutability provides critical advantages: thread safety, hash stability (enabling strings to serve as dictionary keys and set elements), and memory optimization through interning. However, algorithm design requires managing this immutability explicitly. We build buffers via mutable lists (`list[str]`) or integer arrays, deferring the creation of the final string until the entire process is complete.

### When to use it

Apply specialized string patterns when problems require evaluating symmetry (palindromes), structural permutations (anagrams), nested/hierarchical formatting (stack-based parsing), or order-sensitive compression and deduplication.

### When NOT to use it

Do not treat strings as arbitrary mutable buffers. When a problem requires frequent in-place character updates or insertions, convert the string into a `list[str]` or `bytearray` first. Furthermore, avoid full string slices (`s[i:j]`) inside tight loops if a simple two-pointer index comparison or rolling hash can verify equivalence in $O(1)$ space.

### How it works internally

Most non-trivial string problems rely on three primary paradigms:
1. **List-as-Buffer**: Accumulate fragments or individual characters into a Python list and assemble the result at the end using `''.join(buffer)` in $O(N)$ time.
2. **Two-Pointer Invariants**: For palindrome checks or partition problems, place pointers at boundaries (or around centers) and move inward/outward step-by-step, comparing characters without allocating substrings.
3. **Frequency Signatures**: Check anagram or permutation properties using fixed-size frequency tables (e.g., `[0] * 26` for ASCII lowercase) or bitmasks when counting parity (odd/even frequencies), ensuring $O(1)$ auxiliary memory per window or state.

### Common mistakes

- Using repeated string concatenation `s += ch` inside a loop, leading to hidden $O(N^2)$ execution time.
- Creating unnecessary slices like `s[i:j] == s[i:j][::-1]` inside nested loops, causing massive memory allocations and quadratic overhead.
- Assuming ASCII encoding when inputs may contain arbitrary Unicode characters, leading to index-out-of-range errors on fixed-size `[0]*26` arrays without prior validation.
- Off-by-one errors in sliding window boundaries when adjusting dynamic character frequencies.

### Real-world applications

- Text processing engines, markdown parsers, and template renderers that stream and assemble structured text.
- Bioinformatics algorithms analyzing DNA/RNA sequences (k-mer counting, palindromic sequence recognition).
- Network protocol parsers and serializers (HTTP header parsers, JSON tokenizers) tracking delimiters and escape characters.

## Example

Consider checking if a string can become a palindrome by removing at most one character: `s = "abca"`.
1. Place left pointer $L = 0$ (`'a'`), right pointer $R = 3$ (`'a'`). They match, so increment $L \to 1$, decrement $R \to 2$.
2. Now $L = 1$ (`'b'`), $R = 2$ (`'c'`). A mismatch occurs.
3. We have two choices: delete character at $L$ (check if `s[2..2]` is a palindrome) or delete character at $R$ (check if `s[1..1]` is a palindrome).
4. Checking `s[2..2]` gives `"c"` (valid). Checking `s[1..1]` gives `"b"` (valid).
5. Either choice yields a valid palindrome, so the result is `True`. We examined each character at most twice, running in $O(N)$ time and $O(1)$ auxiliary space.

## Visual Explanation

```text
Two-Pointer Palindrome Invariant with at most one skip:

Step 1: Pointers match
  L                   R
  v                   v
[ a ,  b ,  c ,  a ]  --> s[L] == s[R] ('a' == 'a') -> advance both

Step 2: Mismatch detected
       L    R
       v    v
[ a ,  b ,  c ,  a ]  --> s[L] != s[R] ('b' != 'c')

Branch A: Skip L (test s[L+1..R])     Branch B: Skip R (test s[L..R-1])
            L,R                             L,R
             v                               v
       [ a , c , a ] -> Palindrome!     [ a , b , a ] -> Palindrome!

Conclusion: Both branches are valid palindromes. Output True.
```

## Complexity

- **Time Complexity:** String assembly via `''.join()`: $O(N)$ where $N$ is total length of joined fragments. Two-pointer traversal: $O(N)$. Fixed-alphabet anagram checks: $O(N)$ time to count frequencies.
- **Space Complexity:** $O(N)$ for auxiliary character lists and stack buffers. $O(1)$ auxiliary space when evaluating properties with pointer arithmetic and fixed-size frequency tables (e.g., 26 or 128 elements).

Always check whether input constraints permit an $O(N)$ time, $O(1)$ auxiliary space solution before allocating auxiliary strings or dictionaries.

## Interview Perspective

1. **Why is `str` immutable in Python, and how does CPython optimize certain string operations?**
   <details><summary>What a strong answer covers</summary>

   Explain thread safety, hash table security (strings as immutable dictionary keys), and interned string pools. Mention that while CPython has an optimization for `s += c` when the refcount of `s` is 1, relying on it in algorithmic interviews is risky because it is an implementation detail and fails if there are other references.

   </details>
2. **How do you check if two strings are anagrams of each other in $O(1)$ auxiliary space?**
   <details><summary>What a strong answer covers</summary>

   Mention that if the alphabet is bounded (e.g., ASCII or lowercase English), a fixed-size integer array of size 26 or 256 takes $O(1)$ space. For arbitrary Unicode, sorting uses $O(N \log N)$ time and $O(N)$ space in Python (Timsort), or a hash map uses $O(U)$ space where $U$ is the number of unique characters.

   </details>
3. **How can bit manipulation be used to check if any permutation of a string can form a palindrome?**
   <details><summary>What a strong answer covers</summary>

   A palindrome allows at most one character with an odd frequency. For lowercase letters 'a'-'z', maintain a 32-bit integer bitmask where the $k$-th bit is toggled for each occurrence of character $k$. The string can form a palindrome if and only if the bitmask has at most one bit set, checked via `mask & (mask - 1) == 0`.

   </details>
4. **When decoding or expanding encoded strings like `3[a2[c]]`, why is a stack preferred over recursion?**
   <details><summary>What a strong answer covers</summary>

   Both work conceptually, but an explicit stack keeps memory in heap space and avoids Python's recursion limit on deeply nested inputs. Furthermore, it cleanly maintains intermediate repeat counts and string builders across multiple nested scopes.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Valid Palindrome II](exercises/problem-01.md) | Easy/Medium | Two-pointer symmetry check with single tolerance branch | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Decode String](exercises/problem-02.md) | Medium | Stack-based nested string reconstruction | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Find All Anagrams in a String](exercises/problem-03.md) | Medium/Hard | Fixed sliding window with character frequency signature | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Remove Duplicate Letters to Form Smallest Subsequence](exercises/problem-04.md) | Medium/Hard | Monotonic stack with character frequency and seen tracking | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Shortest Palindrome via Prefix Prepending](exercises/problem-05.md) | Hard | Finding the longest palindromic prefix using rolling hash or prefix-suffix matching | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-014
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: String Immutability and Memory, Efficient String Building, Two-Pointer Symmetrical Traversals, Anagram and Frequency Signatures, Stack-Assisted String Parsing and Transformations*
