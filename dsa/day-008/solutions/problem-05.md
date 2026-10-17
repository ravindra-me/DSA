# Solution 5: Minimum Window Subsequence

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Multi-variable dynamic programming / two-pointer complexity analysis

## Approach

We can achieve $O(|s1| \cdot |s2|)$ time and $O(1)$ auxiliary space using a two-pointer sliding window technique with reverse-scanning contraction. We scan forward through `s1` to match characters of `s2` greedily. Once the full sequence of `s2` is matched at some index `r` in `s1`, we walk backward from `r` matching `s2` in reverse order to find the latest possible start index `l` that completes `s2` ending at `r`. This maximizes `l` (minimizing window length `r - l + 1`). We then update our best result and resume the forward search from `l + 1`.

## Thought Process

A naive brute-force approach checks every possible substring `s1[i:j]`, checking if `s2` is a subsequence. There are $O(|s1|^2)$ substrings, and checking takes $O(|s1|)$, giving $O(|s1|^3)$ overall time, which is far too slow for $|s1| = 2 \times 10^4$.

A standard dynamic programming table `dp[i][j]` (the start index in `s1` of the shortest subsequence ending at `s1[i]` matching `s2[:j]`) requires $O(|s1| \cdot |s2|)$ time and $O(|s1| \cdot |s2|)$ space (or $O(|s1|)$ space if optimized), but the constraint specifically asks for $O(1)$ auxiliary space.

Notice that if we fix the end index of a valid window where `s2` is completed, the optimal (shortest) window ending at that exact index is obtained by scanning backwards greedily matching `s2` from right to left. Because matching greedily to the left preserves subsequence validity and pushes the start index as far right as possible, it guarantees the minimum window ending at that position.

After recording the window `s1[l:r + 1]`, the next potential window could not start at or before `l`, so we restart the forward search from `l + 1`. Since each character in `s1` is visited at most $|s2|$ times during reverse scans and once during forward scans, the total time is bounded by $O(|s1| \cdot |s2|)$, with only a few index variables used ($O(1)$ auxiliary space).

## Algorithm

1. Initialize two pointers: `i = 0` (for `s1`) and `j = 0` (for `s2`). Track `min_len = infinity` and `start_idx = -1`.
2. Advance `i` through `s1`. Whenever `s1[i] == s2[j]`, increment `j`.
3. When `j == len(s2)`, we have matched all of `s2`. Let `end = i`.
4. Move backward to optimize the window: decrement `j` to `len(s2) - 1`. While `j >= 0`, decrement `i` until `s1[i] == s2[j]`, then decrement `j`.
5. Now `i` is at the rightmost valid start position `l` for a window ending at `end`. Calculate the window length `end - i + 1`.
6. If this length is strictly less than `min_len`, update `min_len = end - i + 1` and `start_idx = i`.
7. Reset `j = 0` and advance `i = i + 1` to search for subsequent matching windows in `s1`.
8. Continue until `i` reaches the end of `s1`. Return `s1[start_idx : start_idx + min_len]` if `start_idx != -1`, else return `""`.

## Complexity Analysis

- **Time:** $O(|s1| \cdot |s2|)$ because the forward pointer traverses `s1` linearly, and each time a match of `s2` is found, the backward scan takes at most $O(|s2|)$ steps before advancing the forward search by at least 1 index.
- **Space:** $O(1)$ auxiliary space as we only maintain integer indices and pointers (`i`, `j`, `start_idx`, `min_len`, `end`).

## Edge Cases

- `len(s2) > len(s1)`: Handled immediately as `j` will never reach `len(s2)`, correctly returning `""`.
- No window exists (characters from `s2` missing): `start_idx` remains `-1`, returning `""`.
- Single character strings `s1` and `s2`: Properly evaluated in a single step.
- Ties in window length: The algorithm strictly requires `length < min_len` to update `start_idx`, preserving the earliest start index.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def min_window_subsequence(s1: str, s2: str) -> str:
    """Find the shortest contiguous substring of s1 containing s2 as a subsequence."""
    n1, n2 = len(s1), len(s2)
    if n2 > n1:
        return ""

    i = 0
    j = 0
    min_len = float("inf")
    best_start = -1

    while i < n1:
        if s1[i] == s2[j]:
            j += 1
            if j == n2:
                # Full match found ending at i
                end = i
                j -= 1
                # Scan backwards to find the latest valid start for this window
                while j >= 0:
                    if s1[i] == s2[j]:
                        j -= 1
                    i -= 1
                i += 1  # i is now the start index of the window

                window_len = end - i + 1
                if window_len < min_len:
                    min_len = window_len
                    best_start = i

                # Restart search from next character
                j = 0
        i += 1

    if best_start == -1:
        return ""
    return s1[best_start : best_start + int(min_len)]
```
