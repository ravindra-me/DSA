# Solution 1: Valid Palindrome with Alphanumeric Filtering

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Two Pointers with Character Filtering

## Approach

Use two converging pointers from the start and end of the string. Skip non-alphanumeric characters on both ends, and compare lowercase versions of the alphanumeric characters as they meet.

## Thought Process

A straightforward brute-force approach is to filter the entire string into a new list or string of lowercase alphanumeric characters, and then compare that string to its reverse. While this is $O(N)$ time, it requires $O(N)$ extra space to store the filtered string.

To optimize space to $O(1)$ auxiliary memory, we can use the two-pointer technique directly on the input string. By initializing one pointer `left = 0` and another `right = len(s) - 1`, we can advance `left` forward whenever `s[left]` is not alphanumeric, and move `right` backward whenever `s[right]` is not alphanumeric. When both point to valid alphanumeric characters, we compare their lowercase values. If they differ, the string cannot be a palindrome. If they match, we move both inward and repeat until the pointers cross.

## Algorithm

1. Initialize two pointers: `left = 0` and `right = len(s) - 1`.
2. While `left < right`:
3. Advance `left` while `left < right` and `s[left]` is not alphanumeric.
4. Decrement `right` while `left < right` and `s[right]` is not alphanumeric.
5. Compare `s[left].lower()` with `s[right].lower()`. If they do not match, return `False`.
6. Increment `left` by 1 and decrement `right` by 1.
7. If the loop finishes without mismatches, return `True`.

## Complexity Analysis

- **Time:** O(N) where N is the length of `s`, because each pointer advances at most N steps across the string.
- **Space:** O(1) auxiliary space, as no extra strings or lists are created; comparisons are made in-place.

## Edge Cases

- Strings containing only non-alphanumeric characters: both pointers skip past each other without finding mismatches and return True.
- Single-character strings: pointers never cross with differing values and trivially return True.
- Strings with digits and letters: digits should only match identical digits and never match letters (e.g., '0P' is False).

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def is_palindrome(s: str) -> bool:
    """Determine if string is a palindrome considering only alphanumeric characters."""
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```
