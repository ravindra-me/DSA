# Solution 4: Longest Palindromic Substring

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Center Expansion Technique

## Approach

A palindrome mirrors around its center. A string of length $n$ has $2n - 1$ possible centers (each individual character for odd lengths, and each adjacent pair for even lengths). For each center, we expand outwards symmetrically as long as the boundary characters match. We track the longest palindrome found, keeping the earliest one in case of ties.

## Thought Process

A brute-force solution checks all $O(n^2)$ substrings, verifying each in $O(n)$ time for a total of $O(n^3)$ time, which is too slow for $n = 1000$.

Instead of checking substrings from the outside in, we can build them from the inside out using the center expansion technique. Palindromes grow symmetrically around a center. Since an odd-length palindrome centers on an index `i` and an even-length palindrome centers between indices `i` and `i + 1`, there are exactly $n + (n - 1) = 2n - 1$ possible centers. Expanding from each center takes at most $O(n)$ steps, reducing the overall time complexity to $O(n^2)$ and space complexity to $O(1)$ auxiliary space. Because we iterate through centers from left to right and only update our record when a strictly longer palindrome is found, we naturally preserve the earliest appearance rule for ties.

## Algorithm

1. Handle the base case: if `len(s) <= 1`, return `s`.
2. Initialize `start = 0` and `max_len = 1` to track the bounds of the longest palindrome found.
3. Define a helper function `expand(left: int, right: int) -> tuple[int, int]` that decrements `left` and increments `right` while characters at both indices match and are within bounds.
4. Iterate through each index `i` from `0` to `len(s) - 1`.
5. For odd-length palindromes, call `expand(i, i)`.
6. For even-length palindromes, call `expand(i, i + 1)`.
7. For each expansion, if the resulting length `curr_len = right - left + 1` is strictly greater than `max_len`, update `start = left` and `max_len = curr_len`.
8. Return the substring slice `s[start : start + max_len]`.

## Complexity Analysis

- **Time:** $O(n^2)$ where $n$ is the length of `s`. There are $2n - 1$ centers, and expanding from any center takes at most $O(n)$ time.
- **Space:** $O(1)$ auxiliary space as we only maintain pointers and indices without allocating extra data structures.

## Edge Cases

- Single character string: trivially returns `s` without expansion.
- Entire string is identical characters (e.g., 'aaaa'): expands fully across the entire string and returns the whole string.
- No multi-character palindrome exists: returns the first single character in the string.
- Ties in length: only strictly greater lengths update the recorded start position, ensuring the earliest occurrence is returned.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def longest_palindrome(s: str) -> str:
    """Find the longest palindromic substring by expanding around centers."""
    if len(s) <= 1:
        return s

    start = 0
    max_len = 1
    n = len(s)

    def expand(left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        # Loop terminates when s[left] != s[right] or out of bounds
        return left + 1, right - 1

    for i in range(n):
        # Odd-length palindrome centered at i
        l1, r1 = expand(i, i)
        len1 = r1 - l1 + 1
        if len1 > max_len:
            start = l1
            max_len = len1

        # Even-length palindrome centered between i and i + 1
        l2, r2 = expand(i, i + 1)
        len2 = r2 - l2 + 1
        if len2 > max_len:
            start = l2
            max_len = len2

    return s[start:start + max_len]
```
