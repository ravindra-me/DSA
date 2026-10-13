# Problem 3: Reverse String

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Recursive manipulation of sequences | [Day 4: Recursion](../README.md) |

## Problem Statement

Given a string, return the reversed string using only recursion. Do not use string slicing `[::-1]` or built-in reversal methods.

## Input

A string s.

## Output

The reversed string.

## Constraints

- 0 <= len(s) <= 1000

## Examples

**Example 1**

```text
Input:  'hello'
Output: 'olleh'
```

**Example 2**

```text
Input:  ''
Output: ''
```

## Function Signature

```python
def reverse_string(s: str) -> str:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Base case: if string is empty or length 1, return string. Recursive case: take the last character + recursive call on the substring without the last character.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
