# Problem 2: Decode String

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Stack-based nested string reconstruction | [Day 14: Strings](../README.md) |

## Problem Statement

Given an encoded string `s`, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is repeated exactly `k` times. `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid: there are no extra white spaces, square brackets are well-formed, and digits are only used for repeat counts `k`.

## Input

A string `s` containing lowercase English letters, digits, and square brackets `[` and `]`.

## Output

The decoded string.

## Constraints

- 1 <= len(s) <= 1000
- `s` consists of lowercase English letters, digits, and square brackets '[]'.
- `s` is guaranteed to be a valid input.
- All integer multipliers `k` satisfy 1 <= k <= 300.
- The length of the output string will not exceed 10^5.

## Examples

**Example 1**

```text
Input:  s = "3[a]2[bc]"
Output: "aaabcbc"
```

'a' repeated 3 times is 'aaa', and 'bc' repeated 2 times is 'bcbc'.

**Example 2**

```text
Input:  s = "3[a2[c]]"
Output: "accaccacc"
```

The inner '2[c]' becomes 'cc'. The outer '3[a2[c]]' becomes '3[acc]' which is 'accaccacc'.

**Example 3**

```text
Input:  s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

Notice 'ef' is outside brackets and remains as is.

## Function Signature

```python
def decode_string(s: str) -> str:
    """Decode an encoded string formatted as k[encoded_string]."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Traverse the string using a stack to store previous string buffers and multipliers whenever an opening bracket is met. On a closing bracket, pop the multiplier and previous string, and assemble the newly repeated block.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
