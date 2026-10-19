# Solution 1: Valid Parentheses and Brackets

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Bracket matching using LIFO stack invariant

## Approach

Use a Last-In, First-Out (LIFO) stack to track unmatched opening brackets. Whenever a closing bracket is encountered, verify that the stack is non-empty and that the most recently opened bracket matches the incoming closing bracket; otherwise, push opening brackets onto the stack. At the end, the string is valid if and only if the stack is completely empty.

## Thought Process

A naive approach might repeatedly find and remove adjacent matching pairs like `()`, `[]`, or `{}` using string replacement until no pairs can be removed. However, finding and slicing strings repeatedly takes $O(n^2)$ time in the worst case (e.g., deeply nested brackets `((((...))))`), which is too slow for $n = 10^5$.

Notice the core invariant: the most recently opened bracket must be the first one closed. This matches the LIFO property of a stack. When we iterate through the string character by character:
- If we see an opening bracket (`(`, `[`, `{`), we push it onto the stack.
- If we see a closing bracket (`)`, `]`, `}`), the matching opener must be sitting at the very top of the stack. If the stack is empty, or the top does not match, the string is invalid immediately.
- After iterating through the entire string, if any unclosed brackets remain in the stack, the string is invalid.

## Algorithm

1. Define a lookup table mapping each closing bracket to its corresponding opening bracket.
2. Initialize an empty list `stack`.
3. Iterate through each character `char` in the string `s`.
4. If `char` is in the lookup table (i.e. it is a closing bracket): check if `stack` is non-empty and `stack[-1]` equals `lookup[char]`. If so, pop from `stack`; otherwise, return `False`.
5. If `char` is an opening bracket: append `char` to `stack`.
6. After the loop finishes, return `True` if `stack` is empty, else `False`.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the length of `s`, since we process each character exactly once and push/pop operations take $O(1)$ amortized time.
- **Space:** $O(n)$ auxiliary space in the worst case where all characters are opening brackets, stored in the stack.

## Edge Cases

- Empty string (`""`): Vacuously valid; loop never executes, stack is empty, returns `True`.
- Odd length string: Can be optionally pre-checked (`len(s) % 2 != 0` immediately returns `False`), but handled correctly by loop regardless.
- Single opening bracket or single closing bracket: Stack either ends non-empty or pops on empty stack; correctly returns `False`.
- Closing bracket before any opening bracket: Stack is empty when closing bracket arrives; returns `False`.
- Interleaved mismatched brackets like `([)]`: Top of stack does not match `)`; returns `False`.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def is_valid_brackets(s: str) -> bool:
    """Determine if the string has balanced brackets."""
    if len(s) % 2 != 0:
        return False

    matching_open = {")": "(", "}": "{", "]": "["}
    stack: list[str] = []

    for char in s:
        if char in matching_open:
            if not stack or stack[-1] != matching_open[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0
```
