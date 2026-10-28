# Solution 5: Minimum Window Anagram Substring

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** dynamic frequency matching over sliding windows

## Approach

Maintain a fixed-size sliding window of length `len(p)` over string `s` using character frequency counts. Compare the character frequencies inside the window with `p`'s frequencies in $O(1)$ time by tracking the number of matched character counts across the alphabet.

## Thought Process

A naive approach checks every substring of length $k = len(p)$ in `s` and counts its characters (or sorts it), taking $O((n - k + 1) \cdot k)$ time, which for $n, k \le 3 \times 10^4$ requires roughly $10^8$ operations and times out.

Since an anagram requires an exact multiset match, every candidate substring in `s` must have length exactly equal to `len(p)`. When shifting a window of fixed length $k$ by one position to the right, only two characters change: one character leaves the left edge, and one character enters the right edge.

Instead of recomputing or re-comparing the full 26-character frequency arrays at every step (which is $O(26) = O(1)$ per step, but still can be optimized), we can maintain a variable `matches` that tracks how many of the 26 lowercase English letters currently have identical counts in both the window and `p`. When `matches == 26`, the current window is an anagram. Updating counts and `matches` takes $O(1)$ operations per character slide.

## Algorithm

1. If len(s) < len(p), return an empty list immediately.
2. Initialize frequency arrays `p_count` and `window_count` of size 26 with zeros.
3. Populate `p_count` with the counts of each character in `p`.
4. Populate `window_count` with the counts of the first `len(p)` characters of `s`.
5. Count how many characters (0 to 25) have `window_count[i] == p_count[i]`, and store this in `matches`.
6. If `matches == 26`, record index 0 in `result`.
7. Iterate through `s` with index `i` from `len(p)` to `len(s) - 1`.
8. For the incoming character `s[i]`: if its count previously matched `p_count`, decrement `matches`; increment its count in `window_count`; if its count now matches `p_count`, increment `matches`.
9. For the outgoing character `s[i - len(p)]`: if its count previously matched `p_count`, decrement `matches`; decrement its count in `window_count`; if its count now matches `p_count`, increment `matches`.
10. If `matches == 26`, append `i - len(p) + 1` to `result`.
11. Return `result`.

## Complexity Analysis

- **Time:** $O(n)$ where $n = len(s)$, because building the initial window takes $O(k)$ where $k = len(p) \le n$, and each slide of the window processes one incoming and one outgoing character in $O(1)$ operations.
- **Space:** $O(1)$ auxiliary space beyond the output list, as frequency counts require fixed arrays of size 26 for lowercase English letters.

## Edge Cases

- len(p) > len(s): Immediately returns empty list since no substring of `s` can be as long as `p`.
- len(p) == len(s): Evaluates only the single window of length `len(s)` and returns `[0]` if they are anagrams, `[]` otherwise.
- All identical characters: Correctly handles strings like `s = "aaaa"` and `p = "aa"`, sliding count updates properly without underflowing or overcounting.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def find_anagrams(s: str, p: str) -> list[int]:
    """Return start indices of all anagrams of p in s."""
    n, k = len(s), len(p)
    if n < k:
        return []

    p_count = [0] * 26
    window_count = [0] * 26
    ord_a = ord('a')

    for char in p:
        p_count[ord(char) - ord_a] += 1

    for i in range(k):
        window_count[ord(s[i]) - ord_a] += 1

    matches = sum(1 for i in range(26) if window_count[i] == p_count[i])
    result: list[int] = []

    if matches == 26:
        result.append(0)

    for i in range(k, n):
        in_idx = ord(s[i]) - ord_a
        out_idx = ord(s[i - k]) - ord_a

        if in_idx == out_idx:
            if matches == 26:
                result.append(i - k + 1)
            continue

        # Add incoming character
        if window_count[in_idx] == p_count[in_idx]:
            matches -= 1
        window_count[in_idx] += 1
        if window_count[in_idx] == p_count[in_idx]:
            matches += 1

        # Remove outgoing character
        if window_count[out_idx] == p_count[out_idx]:
            matches -= 1
        window_count[out_idx] -= 1
        if window_count[out_idx] == p_count[out_idx]:
            matches += 1

        if matches == 26:
            result.append(i - k + 1)

    return result
```
