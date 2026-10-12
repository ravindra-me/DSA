# Problem 1: Valid Palindrome with Alphanumeric Filtering

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Two Pointers with Character Filtering | [Day 3: Strings](../README.md) |

## Problem Statement

Given a string `s`, determine if it is a palindrome after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters.

An alphanumeric character is defined as a letter (`a-z`, `A-Z`) or digit (`0-9`). An empty string or a string with no alphanumeric characters is considered a valid palindrome.

## Input

`s: str` — the input string.

## Output

`bool` — `True` if `s` is a palindrome under the given rules, `False` otherwise.

## Constraints

- 1 <= len(s) <= 2 * 10^5
- `s` consists only of printable ASCII characters.

## Examples

**Example 1**

```text
Input:  s = "A man, a plan, a canal: Panama"
Output: True
```

After filtering and lowercasing, the string becomes "amanaplanacanalpanama", which reads the same forwards and backwards.

**Example 2**

```text
Input:  s = "race a car"
Output: False
```

After filtering and lowercasing, the string becomes "raceacar", which is not a palindrome.

**Example 3**

```text
Input:  s = "   .,:;!?   "
Output: True
```

Edge case: After filtering out non-alphanumeric characters, the string is empty, which is a valid palindrome.

## Function Signature

```python
def is_palindrome(s: str) -> bool:
    """Determine if string is a palindrome considering only alphanumeric characters."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use two pointers starting at opposite ends of the string. Skip non-alphanumeric characters on both sides without creating an intermediate filtered string, achieving $O(N)$ time and $O(1)$ auxiliary space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
