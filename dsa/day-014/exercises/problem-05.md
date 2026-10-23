# Problem 5: Shortest Palindrome via Prefix Prepending

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Finding the longest palindromic prefix using rolling hash or prefix-suffix matching | [Day 14: Strings](../README.md) |

## Problem Statement

You are given a string `s`. You can convert `s` to a palindrome by adding characters **in front of it**.

Find and return the shortest palindrome you can find by performing this transformation.

## Input

A single string `s` consisting of lowercase English letters.

## Output

The shortest palindrome string formed by prepending characters to `s`.

## Constraints

- 0 <= len(s) <= 5 * 10^4
- `s` consists of lowercase English letters.

## Examples

**Example 1**

```text
Input:  s = "aacecaaa"
Output: "aaacecaaa"
```

The longest palindromic prefix is "aacecaa". Prepending the reverse of the remaining suffix "a" yields "aaacecaaa".

**Example 2**

```text
Input:  s = "abcd"
Output: "dcbabcd"
```

The longest palindromic prefix is "a". Prepending the reverse of "bcd" yields "dcbabcd".

**Example 3**

```text
Input:  s = ""
Output: ""
```

An empty string is already a palindrome.

## Function Signature

```python
def shortest_palindrome(s: str) -> str:
    """Find the shortest palindrome by prepending characters to s."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

The problem reduces to finding the longest palindromic prefix of s. Once identified, reverse the suffix following this prefix and prepend it to s. Use a linear-time rolling hash (Rabin-Karp) or KMP prefix function on `s + '#' + reverse(s)`.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
