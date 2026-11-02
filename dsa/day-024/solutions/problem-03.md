# Solution 3: Longest Substring Without Repeating Characters

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** variable-size window (longest subarray with hash set/map)

## Approach

We maintain a sliding window `[left, right]` containing only unique characters. Using a hash map to store the most recent index of each character, when a duplicate character is encountered at `right`, we instantly shrink the window by moving `left` to `max(left, last_seen[char] + 1)`.

## Thought Process

A brute-force approach checks every possible substring, checking for duplicates in $O(N)$ time per substring, leading to an overall time complexity of $O(N^3)$ (or $O(N^2)$ with an incremental set). We can optimize this by noticing that if a substring `s[left:right+1]` contains duplicate characters, expanding further right will not fix the duplicates. Instead of resetting the left pointer to `left + 1`, we can jump `left` directly past the previous occurrence of the duplicate character. Storing character indices in a map allows $O(1)$ lookups and updates, giving a single pass $O(N)$ solution.

## Algorithm

1. Initialize `max_len = 0`, `left = 0`, and an empty dictionary `last_seen` to track the last index of each character.
2. Iterate through the string with index `right` and character `ch`.
3. If `ch` is in `last_seen` and `last_seen[ch] >= left`, update `left = last_seen[ch] + 1` to exclude the previous instance of `ch` from the window.
4. Update `last_seen[ch] = right`.
5. Update `max_len = max(max_len, right - left + 1)`.
6. Return `max_len`.

## Complexity Analysis

- **Time:** $O(N)$ where $N$ is the length of the string `s`. Each character is processed once by the `right` pointer, and the `left` pointer only moves forward.
- **Space:** $O(	ext{min}(N, \Sigma))$ where $\Sigma$ is the size of the character set (e.g., ASCII/Unicode subset). The hash map stores at most as many entries as distinct characters present in `s`.

## Edge Cases

- Empty string `""`: handled naturally as the loop doesn't execute and returns `0`.
- Single character `"a"`: window size is 1, returns `1`.
- All identical characters `"bbbbb"`: `left` moves forward at every step, max length remains `1`.
- All unique characters `"abcdef"`: window never shrinks, returns full string length `6`.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def length_of_longest_substring(s: str) -> int:
    """Returns the length of the longest substring without repeating characters."""
    last_seen = {}
    max_len = 0
    left = 0
    
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len
```
