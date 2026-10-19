# Problem 5: Decode String with Nested Multipliers

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Nested context resolution with dual stacks | [Day 10: Stack](../README.md) |

## Problem Statement

Given an encoded string `s`, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid: there are no extra white spaces, square brackets are well-formed, and digits are only used for repeat numbers `k`. Furthermore, brackets may be nested.

## Input

A string `s` containing lowercase English letters, digits, and brackets `'['`, `']'`.

## Output

`str`: The fully decoded string.

## Constraints

- 1 <= len(s) <= 100
- s consists of digits, lowercase English letters, and brackets '[' and ']'
- All the integers in s are in the range [1, 300]

## Examples

**Example 1**

```text
Input:  s = "3[a]2[bc]"
Output: "aaabcbc"
```

"a" repeated 3 times is "aaa"; "bc" repeated 2 times is "bcbc".

**Example 2**

```text
Input:  s = "3[a2[c]]"
Output: "accaccacc"
```

Innermost "2[c]" -> "cc". Outer "3[a + cc]" -> "accaccacc".

**Example 3**

```text
Input:  s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

Trailing unbracketed characters are preserved.

## Function Signature

```python
def decode_string(s: str) -> str:
    """Decode the nested encoded string."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a stack to store previous string contexts and repetition counts k when encountering '['. On encountering ']', pop the count and previous string, build the repeated segment, and attach it to the restored context. Target O(length of decoded output).

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
