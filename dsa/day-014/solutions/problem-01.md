# Solution 1: Valid Palindrome II

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy/Medium | **Concept:** Two-pointer symmetry check with single tolerance branch

## Approach

Use a two-pointer approach comparing characters from both ends inward. As long as characters match, advance both pointers. Upon encountering the first mismatch, test whether deleting either the left character or the right character produces a valid palindrome by checking the remaining substrings.

## Thought Process

A standard palindrome check runs in $O(N)$ time with two pointers `left` and `right`. If `s[left] == s[right]`, those characters match and must be retained because deleting either would leave the opposite character unmatched without any benefit.

A brute-force approach would try removing each of the $N$ characters one by one and checking if the remaining string is a palindrome, requiring $O(N^2)$ time. Given $N \le 10^5$, an $O(N^2)$ approach will timeout.

However, we only need to tolerate at most one deletion. When the first mismatch `s[left] != s[right]` occurs, one of these two characters MUST be the deleted character if a palindrome can be formed. We branch into two independent checks: check whether `s[left+1:right+1]` is a palindrome or whether `s[left:right]` is a palindrome. If either is, we can form a palindrome with one removal; otherwise, it is impossible.

## Algorithm

1. Initialize two pointers: `left = 0` and `right = len(s) - 1`.
2. Define a helper function `is_palindrome_range(l, r)` that checks if the substring `s[l..r]` is a palindrome using standard inward two pointers.
3. While `left < right`: if `s[left] == s[right]`, increment `left` and decrement `right`.
4. If `s[left] != s[right]`, return `is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)`.
5. If the loop finishes without finding any mismatch, the string is already a palindrome; return `True`.

## Complexity Analysis

- **Time:** O(N), where N is the length of `s`. We scan inward until the first mismatch, and then perform at most two standard palindrome checks over a substring of length at most N.
- **Space:** O(1) auxiliary space when using pointer indices for the palindrome checks, avoiding substring allocations.

## Edge Cases

- Single character string: trivially a palindrome without any deletions, returns `True`.
- Two character string: always returns `True` because removing either character leaves a 1-character palindrome.
- Already a palindrome: loop terminates without any mismatch, returns `True`.
- Mismatch at the very ends or in the exact middle: handled uniformly by the two pointers.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def valid_palindrome_after_one_removal(s: str) -> bool:
    """Return True if s can become a palindrome by removing at most one character."""
    def is_palindrome_range(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        left += 1
        right -= 1
    return True
```
