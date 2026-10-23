# Problem 1: Valid Palindrome II

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Two-pointer symmetry check with single tolerance branch | [Day 14: Strings](../README.md) |

## Problem Statement

Given a string `s`, return `True` if `s` can be made a palindrome after deleting **at most one** character from it, or `False` otherwise.

## Input

A single string `s` consisting only of lowercase English letters.

## Output

A boolean (`True` or `False`).

## Constraints

- 1 <= len(s) <= 10^5
- `s` consists only of lowercase English letters.

## Examples

**Example 1**

```text
Input:  s = "aba"
Output: True
```

"aba" is already a palindrome.

**Example 2**

```text
Input:  s = "abca"
Output: True
```

You could delete the character 'c' to get "aba", which is a palindrome.

**Example 3**

```text
Input:  s = "abc"
Output: False
```

Deleting any single character leaves a non-palindrome.

## Function Signature

```python
def valid_palindrome_after_one_removal(s: str) -> bool:
    """Return True if s can become a palindrome by removing at most one character."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use two pointers starting at both ends. When the first mismatch is encountered, check if either the substring skipping the left character or the substring skipping the right character forms a valid palindrome.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
