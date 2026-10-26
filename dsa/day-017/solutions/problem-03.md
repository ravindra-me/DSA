# Solution 3: Decode String with Nested Multipliers

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium/Hard | **Concept:** Recursive descent parsing with call-stack index tracking

## Approach

We parse the encoded string using recursive descent, tracking the current character index. Each time an opening bracket `[` is encountered, a new recursive call decodes the nested substring until the matching `]`, returning both the decoded content and the updated parser index to the caller.

## Thought Process

A bracket-matching problem can naturally be modeled either with an explicit stack or with the call stack via recursion. Because the problem explicitly asks for recursive descent where each nesting level corresponds to a recursive activation record, we maintain a parsing index `i`.

While scanning through the string at the current nesting level:
1. If we see a letter, we append it directly to the current level's accumulator.
2. If we see a digit, we accumulate it to form the multiplier `k` (which may span multiple digits, e.g., `300`).
3. When we hit `[`, we recursively call `parse(i + 1)` to evaluate the subproblem inside the brackets. That call returns the decoded inner string and the index pointing right after the matching `]`. We append `k * inner_str` to our current accumulator, reset `k = 0`, and resume parsing from the returned index.
4. When we hit `]`, we know the current level's bracketed section has ended, so we return the accumulated string and the current index + 1.
5. If we reach the end of the string, we return the accumulated string.

## Algorithm

1. Define a helper function `parse(index: int) -> tuple[str, int]` that processes the string starting at `index`.
2. Initialize an empty list `result` for the current nesting level, and an integer `k = 0`.
3. Loop while `index < len(s)`:
4. If `s[index]` is a digit, update `k = k * 10 + int(s[index])` and increment `index`.
5. If `s[index] == '['`, recursively call `sub_result, index = parse(index + 1)`. Append `sub_result * k` to `result`, and reset `k = 0`.
6. If `s[index] == ']'`, return `''.join(result)` and `index + 1` (advancing past the closing bracket).
7. Otherwise (`s[index]` is a letter), append `s[index]` to `result` and increment `index`.
8. After the loop finishes, return `''.join(result)` and `index`.
9. In the main function, call `parse(0)` and return the decoded string.

## Complexity Analysis

- **Time:** O(N + L) where N is the length of the encoded string `s` and L is the length of the decoded string. Each character of `s` is processed by the parser, and building the final output string takes time proportional to the total decoded length L <= 10^5.
- **Space:** O(D + L) where D is the maximum nesting depth of the brackets (call stack depth, at most 30 given len(s) <= 60) and L is the memory needed to construct and return the decoded string segments.

## Edge Cases

- Multi-digit multipliers (e.g. `100[a]`): properly accumulated via `k * 10 + digit`.
- Strings with no brackets or numbers (e.g. `"abc"`): parsed sequentially without recursion.
- Deeply nested brackets (e.g. `2[a2[b2[c]]]`): handled correctly by nested recursive activation records.
- Multiple adjacent bracket expressions (e.g. `3[a]2[bc]`): parsed sequentially within the same activation record.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def decode_string(s: str) -> str:
    """Decodes an encoded string using recursive descent parsing."""
    def parse(index: int) -> tuple[str, int]:
        result: list[str] = []
        k = 0
        
        while index < len(s):
            char = s[index]
            if char.isdigit():
                k = k * 10 + int(char)
                index += 1
            elif char == '[':
                sub_str, index = parse(index + 1)
                result.append(sub_str * k)
                k = 0
            elif char == ']':
                return "".join(result), index + 1
            else:
                result.append(char)
                index += 1
                
        return "".join(result), index

    decoded, _ = parse(0)
    return decoded
```
