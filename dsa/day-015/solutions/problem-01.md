# Solution 1: Validate Deque Palindrome

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Double-ended queue operations

## Approach

Filter the string to keep only lowercase alphanumeric characters and insert them into a double-ended queue (`collections.deque`). Then repeatedly pop characters from both the left and right ends simultaneously, verifying that they match until fewer than two characters remain.

## Thought Process

A palindrome reads identically forwards and backwards. The traditional two-pointer approach checks characters from both ends moving inward. A double-ended queue (`deque`) naturally mirrors this two-pointer symmetry by supporting $O(1)$ operations at both ends (`popleft()` and `pop()`).

To satisfy the constraint of using a `deque`, we first sanitize the input string by filtering out non-alphanumeric characters and converting all letters to lowercase. We populate a `deque` with these cleaned characters. At each step, if the front character differs from the rear character, the string cannot be a palindrome. If all pairs match until the deque has 0 or 1 element, the string is a valid palindrome.

## Algorithm

1. Initialize an empty `collections.deque`.
2. Iterate through each character `char` in the input string `s`. If `char.isalnum()` is true, append `char.lower()` to the deque.
3. While the deque has 2 or more elements (`len(deque) > 1`), pop `left = deque.popleft()` and `right = deque.pop()`.
4. If `left != right`, return `False` immediately.
5. If the loop terminates with 0 or 1 character remaining, return `True`.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the length of `s`. We traverse `s` once to filter characters and then perform at most $n / 2$ pairs of $O(1)$ deque pop operations.
- **Space:** $O(n)$ to store the filtered alphanumeric characters inside the `collections.deque`.

## Edge Cases

- String containing no alphanumeric characters (e.g., '.,' or spaces only): cleans to an empty deque, loop doesn't run, correctly returns `True`.
- Single alphanumeric character (e.g., 'a' or ' :a! '): cleans to length 1, loop doesn't run, correctly returns `True`.
- Odd vs. even length palindromes: odd leaves 1 element, even leaves 0; both exit the loop cleanly and return `True`.
- Mismatches at the boundary ends or deep in the middle: correctly caught as soon as `left != right`.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
from collections import deque


def is_deque_palindrome(s: str) -> bool:
    """Return True if s is a palindrome using a deque for matching."""
    char_deque: deque[str] = deque(
        ch.lower() for ch in s if ch.isalnum()
    )

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True
```
