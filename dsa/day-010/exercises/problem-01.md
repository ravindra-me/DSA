# Problem 1: Valid Parentheses and Brackets

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Bracket matching using LIFO stack invariant | [Day 10: Stack](../README.md) |

## Problem Statement

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

An input string is valid if and only if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Input

A string `s` of length between 0 and $10^5$.

## Output

`bool`: `True` if valid, `False` otherwise.

## Constraints

- 0 <= len(s) <= 10^5
- s consists of parentheses only: '()[]{}'

## Examples

**Example 1**

```text
Input:  s = "()[]{}"
Output: True
```

Every opening bracket is immediately closed by its matching closing bracket.

**Example 2**

```text
Input:  s = "(]"
Output: False
```

')' does not match '['.

**Example 3**

```text
Input:  s = "([)]"
Output: False
```

The closing bracket ')' arrives before '[' is closed.

**Example 4**

```text
Input:  s = ""
Output: True
```

An empty string is vacuously valid.

## Function Signature

```python
def is_valid_brackets(s: str) -> bool:
    """Determine if the string has balanced brackets."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Iterate through characters, pushing opening brackets onto a stack. When encountering a closing bracket, verify that the stack is non-empty and the top matches; pop if valid, otherwise return False. At the end, check that the stack is empty. Aim for O(n) time and O(n) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
