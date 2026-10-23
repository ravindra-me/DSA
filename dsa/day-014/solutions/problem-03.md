# Solution 3: Find All Anagrams in a String

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium/Hard | **Concept:** Fixed sliding window with character frequency signature

## Approach

Use a fixed-size sliding window of length `len(p)` over string `s` while maintaining character frequency counts. By comparing a count of matched distinct characters (or directly comparing 26-element frequency arrays), we can determine whether the current window is an anagram in $O(1)$ time per slide.

## Thought Process

A brute-force solution would examine every substring of `s` of length $k = len(p)$, sort it or build a full frequency map, and compare it to `p`. With $n = len(s)$, there are $n - k + 1$ windows, each taking $O(k \log k)$ or $O(k)$ to process, resulting in an overall time of $O(n \cdot k)$. Given $n, k \le 3 \times 10^4$, $n \cdot k$ can reach $9 \times 10^8$ operations, which easily times out.

Notice that as the window slides one character to the right, only two characters change: the character leaving the left boundary and the character entering the right boundary. The remaining $k - 2$ characters remain unchanged. We can maintain character frequencies using fixed-size arrays of length 26 (since the alphabet is restricted to lowercase English letters) or track the number of matching frequencies between the window and `p`. Maintaining fixed 26-element arrays makes comparing frequency signatures an $O(26) = O(1)$ operation, reducing the total time complexity to $O(n)$.

## Algorithm

1. If len(s) < len(p), return an empty list immediately.
2. Initialize two frequency lists of size 26 (for lowercase English letters), `p_counts` and `window_counts`, filled with zeros.
3. Populate `p_counts` with the character frequencies of `p`, and populate `window_counts` with the first `len(p)` characters of `s`.
4. Initialize an empty result list `result`.
5. Check if `window_counts == p_counts`; if so, append index 0 to `result`.
6. Iterate an index `i` from `len(p)` to `len(s) - 1`:
  a. Add the new incoming character `s[i]` to `window_counts`.
  b. Remove the outgoing character `s[i - len(p)]` from `window_counts`.
  c. If `window_counts == p_counts`, append `i - len(p) + 1` to `result`.
7. Return `result`.

## Complexity Analysis

- **Time:** O(n + k) where n is len(s) and k is len(p). Initializing the frequency arrays takes O(k) time, and sliding across s takes n - k steps, each performing an O(26) = O(1) comparison.
- **Space:** O(1) auxiliary space beyond the output list, as the frequency arrays each have a fixed size of 26 regardless of the input length.

## Edge Cases

- len(s) < len(p): No valid anagram window can exist, so the function returns [] immediately.
- len(s) == len(p): The loop over sliding steps does not execute; only the initial window check at index 0 is evaluated.
- All characters identical (e.g., s = 'aaaa', p = 'aa'): Multiple overlapping matches are correctly detected at consecutive indices [0, 1, 2].
- No matching anagrams: The function completes its traversal and returns an empty list [].

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def find_all_anagrams(s: str, p: str) -> list[int]:
    """Find all start indices in s that form anagrams of p."""
    n, k = len(s), len(p)
    if n < k:
        return []

    p_counts = [0] * 26
    window_counts = [0] * 26
    base = ord('a')

    for char in p:
        p_counts[ord(char) - base] += 1

    for i in range(k):
        window_counts[ord(s[i]) - base] += 1

    result: list[int] = []
    if window_counts == p_counts:
        result.append(0)

    for i in range(k, n):
        window_counts[ord(s[i]) - base] += 1
        window_counts[ord(s[i - k]) - base] -= 1
        if window_counts == p_counts:
            result.append(i - k + 1)

    return result
```
