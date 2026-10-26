# Problem 3: Decode String with Nested Multipliers

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Recursive descent parsing with call-stack index tracking | [Day 17: Recursion](../README.md) |

## Problem Statement

Given an encoded string `s`, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, and digits are only used for repeat numbers `k`.

Implement this using a recursive descent approach where each bracket nesting level is parsed by a new recursive activation record.

## Input

`s`: A string representing the encoded message.

## Output

A string representing the fully decoded message.

## Constraints

- 1 <= len(s) <= 60
- `s` consists of lowercase English letters, digits, and square brackets `'['` and `']'`.
- All integers `k` are in the range [1, 300].
- The decoded output length will not exceed 10^5.

## Examples

**Example 1**

```text
Input:  s = "3[a]2[bc]"
Output: "aaabcbc"
```

"a" is repeated 3 times, followed by "bc" repeated 2 times.

**Example 2**

```text
Input:  s = "3[a2[c]]"
Output: "accaccacc"
```

"c" is repeated twice inside the bracket yielding "acc", which is then repeated 3 times.

**Example 3**

```text
Input:  s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

Multiple separate chunks concatenated.

## Function Signature

```python
def decode_string(s: str) -> str:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a parsing index and recursively decode characters. When encountering `'['`, recurse to decode the bracketed content; when encountering `']'`, return the constructed substring and the updated index.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
