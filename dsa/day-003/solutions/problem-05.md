# Solution 5: Minimum Window Substring

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Sliding Window with Character Multi-Sets

## Approach

We use a sliding window with two pointers, `left` and `right`, expanding the window by moving `right` to include characters until the window satisfies all character counts from `t`. Once valid, we contract the window by moving `left` to find the smallest possible valid substring, updating our result whenever we find a shorter valid window.

## Thought Process

A brute-force approach would check every possible substring, leading to O(N^3) time complexity. The sliding window pattern is ideal here because we need a contiguous sequence, and adding/removing characters only incrementally changes the window's validity. By maintaining a frequency map of `t` and a running count of 'matched' characters, we can expand and contract efficiently in a single pass over `s` (O(N) time).

## Algorithm

1. 1. Create a frequency map (or array) `target_counts` for string `t`.
2. 2. Initialize `left = 0`, `right = 0`, `formed = 0` (number of unique characters fully satisfied), and `required = len(target_counts)`.
3. 3. Use a dictionary `window_counts` to track characters in the current `[left, right]` window.
4. 4. Expand `right` from 0 to `len(s) - 1`. For each char, increment its `window_counts` and check if it matches the `target_counts` threshold.
5. 5. When `formed == required`, start contracting from `left`. Update the minimum window if the current one is smaller.
6. 6. Increment `left` and update `formed` if a character count drops below the requirement.
7. 7. Return the smallest substring found, or "" if no valid window was ever formed.

## Complexity Analysis

- **Time:** O(S + T), where S is the length of s and T is the length of t. We traverse s at most twice (once with right, once with left).
- **Space:** O(1) because the character set is restricted to English letters (max 52) or standard ASCII (constant 128), making the frequency map size fixed.

## Edge Cases

- s is shorter than t: The loop will finish without setting the result, correctly returning "".
- t contains characters not in s: The `formed` variable will never reach `required`, correctly returning "".
- Empty strings: Handled implicitly by range loops or explicit checks.
- Duplicates in t: The frequency map handles these correctly by only marking a character 'satisfied' when the window count meets or exceeds the required count.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""

    target_counts = Counter(t)
    required = len(target_counts)
    
    window_counts = {}
    formed = 0
    
    # (length, left_index, right_index)
    ans = float("inf"), None, None
    
    l, r = 0, 0
    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1
        
        while l <= r and formed == required:
            char = s[l]
            
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            
            window_counts[char] -= 1
            if char in target_counts and window_counts[char] < target_counts[char]:
                formed -= 1
            
            l += 1
            
        r += 1
        
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
```
