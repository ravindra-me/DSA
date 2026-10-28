# Solution 1: Valid Anagram Parity

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** frequency counting and balance comparison

## Approach

Two strings are anagrams if and only if they have the same length and identical character frequencies. We can verify this in $O(n)$ time by first checking length equality, then tallying character counts using a fixed-size frequency array of size 26 (or hash map) incrementing for characters in $s$ and decrementing for characters in $t$.

## Thought Process

A naive approach is to generate all permutations of string $s$ and check if $t$ matches any of them, which takes $O(n! \cdot n)$ time—infeasible for $n \le 5 \cdot 10^4$. Another common approach is sorting both strings, yielding $O(n \log n)$ time and $O(n)$ auxiliary space depending on the sorting implementation.

Since the problem specifies that the strings consist only of lowercase English letters, the alphabet size is bounded by $\Sigma = 26$. This makes frequency counting ideal: an anagram must have an exact 1-to-1 matching of character frequencies. We can either build two hash tables / frequency arrays and compare them, or maintain a single frequency balance by incrementing counts for characters in $s$ and decrementing for characters in $t$. If all balances reach zero, the strings are anagrams.

## Algorithm

1. Check if len(s) != len(t). If true, return False immediately.
2. Initialize an array `counts` of size 26 with all zeros.
3. Iterate through index `i` from 0 to `len(s) - 1`:
4. Increment counts[ord(s[i]) - ord('a')].
5. Decrement counts[ord(t[i]) - ord('a')].
6. Return True if all entries in `counts` are 0, otherwise False.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the length of the strings. We traverse each string once and inspect a fixed-size array of 26 integers.
- **Space:** $O(1)$ auxiliary space because the alphabet size is bounded to 26 lowercase English letters.

## Edge Cases

- Length mismatch: handled immediately by the initial `len(s) != len(t)` check.
- Single character strings: correctly compares identical or differing single characters.
- Identical strings: naturally balances all character counts to zero.
- Strings with identical character sets but differing multiplicities: non-zero counts will remain, returning False.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def is_anagram(s: str, t: str) -> bool:
    """Return True if t is an anagram of s, otherwise False."""
    if len(s) != len(t):
        return False

    counts = [0] * 26
    offset = ord('a')
    for char_s, char_t in zip(s, t):
        counts[ord(char_s) - offset] += 1
        counts[ord(char_t) - offset] -= 1

    return all(count == 0 for count in counts)
```
