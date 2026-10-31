# Solution 1: Valid Palindrome with Alphanumeric Filtering

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Opposite-direction pointers with conditional filtering

## Approach

Use two pointers starting at opposite ends of the string (`left = 0`, `right = len(s) - 1`). Advance the pointers inward past any non-alphanumeric characters, and compare characters case-insensitively. If any mismatch occurs, the string is not a valid palindrome; if the pointers cross, it is.

## Thought Process

A naive approach filters out non-alphanumeric characters and converts remaining characters to lowercase into a new string or list, then checks if it equals its reverse. While this is $O(N)$ time, it requires $O(N)$ auxiliary memory.

We can improve the auxiliary space complexity to $O(1)$ by using the two-pointer technique directly on the original string in place. By maintaining a left pointer moving forward and a right pointer moving backward, we skip non-alphanumeric characters on the fly using `str.isalnum()`. Whenever both pointers point to alphanumeric characters, we compare their lowercase versions. If they ever differ, we can return `False` immediately.

## Algorithm

1. Initialize `left = 0` and `right = len(s) - 1`.
2. While `left < right`:
3. If `s[left]` is not alphanumeric, increment `left` and continue.
4. If `s[right]` is not alphanumeric, decrement `right` and continue.
5. Compare `s[left].lower()` and `s[right].lower()`. If they do not match, return `False`.
6. If they match, increment `left` and decrement `right`.
7. If the loop finishes without mismatches, return `True`.

## Complexity Analysis

- **Time:** O(N) where N is the length of `s`. Each character is visited at most a constant number of times as the two pointers converge.
- **Space:** O(1) auxiliary space because pointers are updated in place without allocating new strings or collections.

## Edge Cases

- Single character string: trivially returns True.
- String with no alphanumeric characters (e.g. "   " or ",.?!"): pointers pass each other without mismatches, correctly returning True.
- Even vs. odd length valid palindromes: pointers either meet on the middle element or cross cleanly.
- Mixed alphanumeric characters (letters and digits, e.g. "0P"): '0' and 'P' are both alphanumeric but not equal, correctly returning False.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def is_valid_palindrome(s: str) -> bool:
    """Return True if s is a palindrome considering only alphanumeric chars, case-insensitively."""
    left: int = 0
    right: int = len(s) - 1

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
