# Problem 1: Validate Deque Palindrome

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Double-ended queue operations | [Day 15: Deque & Monotonic Queue](../README.md) |

## Problem Statement

Determine whether a given string `s` is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

You must explicitly use a double-ended queue (`collections.deque`) to simulate the verification process by popping characters from both ends simultaneously.

## Input

`s: str` - the input string.

## Output

`bool` - `True` if `s` is a palindrome under the rules, `False` otherwise.

## Constraints

- 1 <= len(s) <= 2 * 10^5
- s consists only of printable ASCII characters.

## Examples

**Example 1**

```text
Input:  s = "A man, a plan, a canal: Panama"
Output: True
```

After cleaning: "amanaplanacanalpanama", which reads the same forwards and backwards.

**Example 2**

```text
Input:  s = "race a car"
Output: False
```

After cleaning: "raceacar", which is not a palindrome.

**Example 3**

```text
Input:  s = ".,"
Output: True
```

After removing non-alphanumeric characters, the string becomes empty "", which is trivially a palindrome.

## Function Signature

```python
def is_deque_palindrome(s: str) -> bool:
    """Return True if s is a palindrome using a deque for matching."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Filter alphanumeric characters into a `collections.deque` in lowercase. While the deque has length > 1, pop from left and right and compare.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
