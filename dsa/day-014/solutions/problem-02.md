# Solution 2: Decode String

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Medium | **Concept:** Stack-based nested string reconstruction

## Approach

Use a stack to manage nested structures. Track the current repeating count `current_k` and accumulated string `current_str`. When encountering `[`, push `(current_str, current_k)` onto the stack and reset them. When encountering `]`, pop the previous state and append `popped_k * current_str` to `popped_str`.

## Thought Process

When decoding nested patterns like `3[a2[c]]`, the innermost brackets must be decoded before their enclosing brackets can be formed. This Last-In, First-Out (LIFO) relationship directly suggests a stack or recursion.

A naive approach might find matching bracket pairs iteratively, replace the innermost bracketed string with its repeated version, and repeat. However, repeated string searches and slicing result in quadratic or worse complexity due to intermediate string copies.

With a single pass and a stack, we process each character linearly:
1. If it's a digit, update `current_k` (handling multi-digit numbers via `current_k = current_k * 10 + digit`).
2. If it's `[`, we push the `current_str` context and `current_k` onto the stack and reset both.
3. If it's `]`, we pop the previous context string and repeat count `k`, setting `current_str = prev_str + k * current_str`.
4. If it's a letter, simply append it to `current_str`.

This ensures that every character is processed in a single pass, with string concatenations directly contributing to the final output string.

## Algorithm

1. Initialize `stack = []`, `current_str = []` (or empty string/list of chars), and `current_num = 0`.
2. Iterate through each character `char` in string `s`.
3. If `char` is a digit: update `current_num = current_num * 10 + int(char)`.
4. If `char == '['`: push the tuple `(''.join(current_str), current_num)` to `stack`, then reset `current_str = []` and `current_num = 0`.
5. If `char == ']'`: pop `prev_str, repeat_count` from `stack`. Set `current_str = [prev_str + repeat_count * ''.join(current_str)]`.
6. If `char` is an alphabetic character: append `char` to `current_str`.
7. After iterating through `s`, return `''.join(current_str)`.

## Complexity Analysis

- **Time:** O(N + M), where N is the length of `s` and M is the length of the decoded output string. Each character of `s` is examined once, and string repetitions copy characters proportionally to the final output size (bounded by 10^5).
- **Space:** O(N + M) to store the stack frames and intermediate/final decoded strings.

## Edge Cases

- String with no brackets (e.g., 'abcdef'): handled directly as letters accumulate in `current_str` without stack operations.
- Multi-digit repeat counts (e.g., '100[a]'): handled by accumulating digits via `current_num = current_num * 10 + int(char)`.
- Multiple nesting levels (e.g., '2[a3[b2[c]]]'): handled gracefully by the stack's LIFO order.
- Adjacent encoded blocks (e.g., '2[a]3[b]'): after finishing one block at `]`, the next block starts with a clean `current_num` and appends to existing decoded text.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def decode_string(s: str) -> str:
    """Decode an encoded string formatted as k[encoded_string]."""
    stack: list[tuple[str, int]] = []
    current_str: list[str] = []
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack.append(("".join(current_str), current_num))
            current_str = []
            current_num = 0
        elif char == "]":
            prev_str, repeat_count = stack.pop()
            decoded_chunk = prev_str + repeat_count * "".join(current_str)
            current_str = [decoded_chunk]
        else:
            current_str.append(char)

    return "".join(current_str)
```
