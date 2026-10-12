# Day 3: Strings: Character Sequences, Immutability, and Core Patterns

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 3 | 2026-10-12 | Fundamentals | New topic | progressive | Python 3.12 |

Strings are ordered sequences of characters that appear in almost every programming domain, from web requests to genome sequencing. In Python and many modern languages, strings are immutable, meaning modifications create new strings rather than updating existing ones in place. Mastering string manipulation requires understanding indexing, frequency counting, two-pointer traversals, and efficient string construction.

## Topic

**Strings**: immutability, character manipulation, palindromes, anagrams, string building

## Learning Objectives

By the end of this lesson you should be able to:

- Understand string immutability in Python and avoid accidental $O(N^2)$ concatenation antipatterns.
- Manipulate characters efficiently using ASCII/Unicode mappings and frequency counting.
- Apply inward-moving two-pointer techniques to palindrome detection and filtering.
- Determine anagram relationships using frequency arrays and hash maps.
- Construct and transform complex strings in optimal $O(N)$ time using list-based buffering.

## Concept Explanation

### What it is

A string is fundamentally an indexed sequence of characters. Conceptually, it is very similar to an array of bytes or Unicode code points. However, in Python, strings (`str`) are *immutable*: once allocated in memory, their contents cannot be altered. If you want to change a character in a string, you must allocate and build an entirely new string.

### Why it exists

Immutability exists for safety, thread-safety, and performance optimization (such as hash caching and string interning). Because strings cannot change, Python can safely use them as dictionary keys and set elements without worrying that their hash value will mutate. The trade-off is algorithmic: naive string concatenation inside a loop repeatedly allocates new memory, degrading linear operations into quadratic bottlenecks.

### When to use it

Use string-specific techniques whenever dealing with text, pattern matching, format conversion, lexical comparisons, or sequence symmetry. When a problem asks to verify properties like palindrome structure or anagram rearrangement, character-level indexed operations and frequency tables are the primary tools.

### When NOT to use it

Do not treat strings as mutable arrays. If an algorithm requires frequent in-place character swaps, appends, or deletions at arbitrary indices, convert the string into a list of characters (`list(s)`), mutate the list, and then join it back (`"".join(chars)`). For raw binary processing, use `bytes` or `bytearray` instead.

### How it works internally

Strings support random access in $O(1)$ time via zero-based indexing (`s[i]`). Python stores strings using internal representations (Latin-1, UCS-2, or UCS-4) depending on the widest character, ensuring each character takes equal byte width for $O(1)$ indexing. 

Two core algorithmic patterns govern strings:
1. **Two Pointers**: Used for symmetry (e.g., palindromes) where one pointer starts at index `0` and another at `len(s) - 1`, advancing toward each other.
2. **Frequency Buckets**: Because the alphabet size $K$ is typically small and fixed (e.g., 26 lowercase English letters or 128 ASCII symbols), character counts can be tracked in an array of size $K$ or a hash map, enabling $O(N)$ anagram and permutation checks.

### Common mistakes

- Accumulating strings using `s += char` inside an $N$-iteration loop. Each addition creates a new string of increasing length, producing an accidental $O(N^2)$ runtime instead of $O(N)$.
- Confusing string length with byte length when dealing with multi-byte Unicode characters (e.g., emojis or accented glyphs).
- Forgetting case sensitivity or non-alphanumeric characters in interview problems (e.g., ignoring whether 'A' equals 'a' or if punctuation should be stripped).
- Index out-of-range errors when slicing or comparing adjacent characters (`s[i] == s[i + 1]`) at the string boundary.

### Real-world applications

- URL parsing, routing, and parameter sanitization in web frameworks.
- Bioinformatics algorithms finding DNA sequences, reverse complements, and mutations (A, C, G, T).
- Data serialization formats such as JSON, CSV, and protocol parsers.
- Search engine tokenization, text normalization, and inverted index construction.

## Example

### Tracing Palindrome Validation
Consider verifying whether the string `"racecar"` is a palindrome.

1. Initialize left pointer `l = 0` ('r') and right pointer `r = 6` ('r').
2. Compare `s[l]` and `s[r]`. Both are `'r'`, so increment `l` to 1, decrement `r` to 5.
3. Compare `s[l]` ('a') and `s[r]` ('a'). Equal. Advance: `l = 2`, `r = 4`.
4. Compare `s[l]` ('c') and `s[r]` ('c'). Equal. Advance: `l = 3`, `r = 3`.
5. Pointers meet (`l >= r`). Loop terminates.

All symmetric characters matched; return `True` in $O(N)$ time and $O(1)$ extra space.

## Visual Explanation

```text
Two-Pointer Palindrome Check on 'racecar':

  Index:  0   1   2   3   4   5   6
  Char:   r   a   c   e   c   a   r
          ^                       ^
        left                    right    s[0] == s[6] ('r' == 'r') -> Advance

  Index:  0   1   2   3   4   5   6
  Char:   r   a   c   e   c   a   r
              ^               ^
            left            right        s[1] == s[5] ('a' == 'a') -> Advance

  Index:  0   1   2   3   4   5   6
  Char:   r   a   c   e   c   a   r
                  ^       ^
                left    right            s[2] == s[4] ('c' == 'c') -> Advance

  Index:  0   1   2   3   4   5   6
  Char:   r   a   c   e   c   a   r
                      ^
                  left, right            left >= right -> Valid Palindrome
```

## Complexity

- **Time Complexity:** Character indexing `s[i]`: $O(1)$. Length check `len(s)`: $O(1)$. Slicing `s[i:j]`: $O(j - i)$ because a new string copy is created. Joining a list of $N$ characters `"".join(arr)`: $O(N)$. Naive repeated concatenation of $N$ characters in a loop: $O(N^2)$.
- **Space Complexity:** $O(N)$ auxiliary space whenever allocating a modified copy of the string or accumulating characters in a list before joining.

Python optimizes certain string operations with C-level implementations. However, relying on implementation-specific optimizations (like CPython's in-place append optimization when reference count is 1) is fragile. Always design algorithms assuming string concatenation is $O(L)$ where $L$ is current length.

## Interview Perspective

1. **Why does string concatenation inside a loop lead to $O(N^2)$ time in Python?**
   <details><summary>What a strong answer covers</summary>

   Strings are immutable. Adding a character of length 1 to a string of length $k$ requires allocating memory for $k + 1$ characters and copying all existing $k$ characters. Summing from $1$ to $N$ yields $1 + 2 + \dots + N = O(N^2)$ work. The optimal approach collects items in a list and calls `"".join()`, which pre-allocates the exact memory needed in a single $O(N)$ pass.

   </details>
2. **How do you check if two strings are anagrams without sorting?**
   <details><summary>What a strong answer covers</summary>

   Sorting takes $O(N \log N)$ time. Anagrams can be verified in $O(N)$ time using frequency counts. Count frequencies of each character in both strings using either a fixed-size array of 26 integers (for lowercase English) or a hash map / `collections.Counter`, and verify that all character counts match.

   </details>
3. **What is the difference between Unicode code points and byte representations?**
   <details><summary>What a strong answer covers</summary>

   A Unicode code point is an abstract integer representing a unique character (e.g., U+0041 for 'A'). Byte representations (like UTF-8, UTF-16) encode these code points into sequences of bytes. In Python 3, `str` operates at the code point level, while `bytes` represents raw binary data.

   </details>
4. **How do you reverse the words in a sentence without using built-in split or reverse methods?**
   <details><summary>What a strong answer covers</summary>

   Convert the string to a mutable character list. First, reverse the entire character array. Then, traverse the array and reverse each individual word in place using two pointers. Finally, clean up redundant whitespace. This demonstrates deep understanding of in-place two-pointer manipulation.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Valid Palindrome with Alphanumeric Filtering](exercises/problem-01.md) | Easy | Two Pointers with Character Filtering | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Group Anagrams](exercises/problem-02.md) | Easy/Medium | Character Frequency Signatures and Hashing | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [String Compression (Run-Length Encoding)](exercises/problem-03.md) | Medium | String Building & In-Place Pointer Compacting | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Longest Palindromic Substring](exercises/problem-04.md) | Medium/Hard | Center Expansion Technique | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Minimum Window Substring](exercises/problem-05.md) | Hard | Sliding Window with Character Multi-Sets | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-003
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: String Immutability, String Slicing & Indexing, Two-Pointer Technique, Frequency Counting & Anagrams, Efficient String Building*
