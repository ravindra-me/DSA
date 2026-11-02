# Solution 4: Longest Repeating Character Replacement

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** window invariants with character frequency

## Approach

We use a variable-length sliding window `[left, right]` and keep track of character frequencies within the window. The core invariant is that a window of length `L` is valid if `L - max_freq <= k`, where `max_freq` is the frequency of the most common character in the window. We expand `right` step-by-step and increment `left` whenever the invariant is violated.

## Thought Process

A naive brute-force approach checks all $O(N^2)$ substrings, counts character frequencies in $O(N)$ for each, and checks if `length - max_freq <= k`. This results in $O(N^3)$ time complexity, or $O(N^2)$ if frequencies are updated dynamically. To optimize to $O(N)$, we observe that as the right end of the window advances, the required number of replacements only increases. If a window becomes invalid (`length - max_freq > k`), shrinking the window from the left by 1 element ensures we maintain an optimal candidate window size. Notably, `max_freq` only needs to track the maximum frequency seen in any window so far, because a smaller `max_freq` can never yield a longer valid window than our current maximum.

## Algorithm

1. Initialize `counts` array/hashmap of size 26 for character frequencies.
2. Initialize `left = 0`, `max_freq = 0`, and `max_len = 0`.
3. Iterate `right` from `0` to `len(s) - 1`.
4. Increment the count of `s[right]` in `counts` and update `max_freq = max(max_freq, counts[s[right]])`.
5. If the current window size `(right - left + 1) - max_freq > k`, decrement `counts[s[left]]` and increment `left`.
6. Update `max_len = max(max_len, right - left + 1)`.
7. Return `max_len` after processing all characters.

## Complexity Analysis

- **Time:** $O(N)$ where $N$ is the length of string `s`. Each character is added and removed from the sliding window at most once.
- **Space:** $O(1)$ auxiliary space since the character frequency map stores at most 26 uppercase English letters.

## Edge Cases

- k is larger than or equal to string length: any substitution is allowed, answer is len(s).
- k = 0: no substitutions allowed, return length of longest contiguous identical substring.
- Single character string: window size is 1, answer is 1.
- All characters identical: no replacements needed, answer is len(s).

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
from collections import Counter

def character_replacement(s: str, k: int) -> int:
    """Calculates maximum length of repeating character substring after at most k replacements."""
    counts = Counter()
    left = 0
    max_freq = 0
    max_len = 0
    
    for right in range(len(s)):
        counts[s[right]] += 1
        max_freq = max(max_freq, counts[s[right]])
        
        # Current window size is right - left + 1.
        # Number of replacements needed is window size - max_freq.
        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len
```
