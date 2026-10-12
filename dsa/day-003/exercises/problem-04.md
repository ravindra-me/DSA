# Problem 4: Longest Palindromic Substring

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Center Expansion Technique | [Day 3: Strings](../README.md) |

## Problem Statement

Given a string `s`, return the longest substring of `s` that is a palindrome.

A **substring** is a contiguous non-empty sequence of characters within a string. If multiple palindromic substrings have the same maximum length, return the one that appears first.

## Input

`s: str` — the input string.

## Output

`str` — the longest palindromic substring.

## Constraints

- 1 <= len(s) <= 1000
- `s` consists of only lowercase and/or uppercase English letters.

## Examples

**Example 1**

```text
Input:  s = "babad"
Output: "bab"
```

"aba" is also valid in length, but "bab" appears first.

**Example 2**

```text
Input:  s = "cbbd"
Output: "bb"
```

The longest palindromic substring is "bb".

**Example 3**

```text
Input:  s = "a"
Output: "a"
```

Edge case: a single character is trivially a palindrome of length 1.

## Function Signature

```python
def longest_palindrome(s: str) -> str:
    """Find the longest palindromic substring by expanding around centers."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Expand outward from each potential center. Remember there are $2N - 1$ possible centers (odd-length centers at each character and even-length centers between characters). Aim for $O(N^2)$ time and $O(1)$ auxiliary space.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
