# Problem 1: Valid Palindrome with Alphanumeric Filtering

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Opposite-direction pointers with conditional filtering | [Day 22: Two Pointers](../README.md) |

## Problem Statement

Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

A string is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

## Input

`s: str` — an input string of ASCII characters.

## Output

`bool` — `True` if `s` is a palindrome under the conditions, `False` otherwise.

## Constraints

- 1 <= len(s) <= 2 * 10^5
- s consists only of printable ASCII characters.

## Examples

**Example 1**

```text
Input:  s = "A man, a plan, a canal: Panama"
Output: True
```

"amanaplanacanalpanama" is a palindrome.

**Example 2**

```text
Input:  s = "race a car"
Output: False
```

"raceacar" is not a palindrome.

**Example 3**

```text
Input:  s = " ., "
Output: True
```

After removing non-alphanumeric characters, the string is empty "", which is trivially a palindrome.

## Function Signature

```python
def is_valid_palindrome(s: str) -> bool:
    """Return True if s is a palindrome considering only alphanumeric chars, case-insensitively."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use opposite-direction pointers starting at the front and back. Increment/decrement to skip non-alphanumeric characters without allocating a new filtered string, achieving O(n) time and O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
