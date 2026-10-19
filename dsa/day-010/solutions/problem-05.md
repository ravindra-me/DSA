# Solution 5: Decode String with Nested Multipliers

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Nested context resolution with dual stacks

## Approach

We maintain a running current string and current repeat count. When encountering an open bracket `'['`, we push the accumulated string and count onto a stack and reset both. When encountering a closing bracket `']'`, we pop the previous string and repeat count from the stack, replicate the current string by the count, and prepend the popped string to it.

## Thought Process

Nested brackets create hierarchical contexts: an inner encoded string must be resolved before the outer string can be fully expanded. This Last-In-First-Out behavior maps naturally to a stack.

A naive recursive approach could parse matching brackets by scanning for matching pairs, but that requires repeated substrings and string slicing, leading to quadratic overhead. By processing linearly with an explicit stack, we track context switches in $O(1)$ stack operations.

At any point, we track:
1. `curr_str`: characters collected in the current scope.
2. `curr_k`: the multiplier being parsed digit by digit (handling multi-digit numbers like `10[a]`).

When we see `'['`, a new scope begins: we push `(curr_str, curr_k)` to the stack and reset both. When we see `']'`, the current scope closes: we pop `(prev_str, k)` and update `curr_str = prev_str + k * curr_str`. Plain characters are simply appended to `curr_str`.

## Algorithm

1. Initialize an empty stack `stack`, an empty string `curr_str = ""`, and `curr_k = 0`.
2. Iterate through each character `char` in the input string `s`.
3. If `char` is a digit: update `curr_k = curr_k * 10 + int(char)` to accumulate multi-digit numbers.
4. If `char` is `'['`: push `(curr_str, curr_k)` onto `stack`, then reset `curr_str = ""` and `curr_k = 0`.
5. If `char` is `']'`: pop `(prev_str, repeat_count)` from `stack`, then update `curr_str = prev_str + (curr_str * repeat_count)`.
6. If `char` is an alphabetic character: append `char` to `curr_str`.
7. After iterating through all characters, return `curr_str`.

## Complexity Analysis

- **Time:** O(N + L) where N is the length of the encoded string `s` and L is the length of the decoded string. Each character of `s` is examined once, and constructing the output takes time proportional to the length of the generated string.
- **Space:** O(D + L) where D is the maximum nesting depth of the brackets (bounded by N) for the stack, and L is the storage required for constructing intermediate strings and the final decoded output.

## Edge Cases

- No brackets present: the string consists solely of plain characters, which are appended directly to `curr_str`.
- Multi-digit multipliers: numbers like `100[a]` are parsed correctly via `curr_k = curr_k * 10 + int(char)`.
- Deeply nested brackets: multiple levels of nested contexts (e.g. `2[a2[b2[c]]]`) are maintained in the stack without stack overflow.
- Consecutive sibling bracketed groups: state is reset between adjacent encoded blocks (e.g. `2[a]3[b]`).

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def decode_string(s: str) -> str:
    """Decode the nested encoded string."""
    stack: list[tuple[str, int]] = []
    curr_str = ""
    curr_k = 0

    for char in s:
        if char.isdigit():
            curr_k = curr_k * 10 + int(char)
        elif char == "[":
            stack.append((curr_str, curr_k))
            curr_str = ""
            curr_k = 0
        elif char == "]":
            prev_str, repeat_count = stack.pop()
            curr_str = prev_str + (curr_str * repeat_count)
        else:
            curr_str += char

    return curr_str
```
