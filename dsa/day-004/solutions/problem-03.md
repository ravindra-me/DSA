# Solution 3: Reverse String

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Recursive manipulation of sequences

## Approach

The recursive strategy is based on the observation that the reverse of a string `s` is equal to the reverse of the tail of `s` (everything after the first character) concatenated with the first character itself. We define a base case for strings of length 0 or 1, and for longer strings, we reduce the problem size by one character in each recursive call.

## Thought Process

A brute-force approach would be to create a new list or string and append characters in reverse order. In recursion, we can think of the stack as our storage. By moving the first character to the end of the result of the recursive call on the remainder, we naturally build the string in reverse. While slicing `s[1:]` in Python creates a new string object, making the naive recursive approach O(N^2) due to copying, it is the idiomatic way to demonstrate recursion on sequences. To make this O(N) in space and time, one would typically use two pointers; however, since the prompt mandates recursion for the reversal logic, the stack-based decomposition is the intended recursive solution.

## Algorithm

1. 1. Define a base case: if the string length is <= 1, return the string as is.
2. 2. For a string of length > 1, extract the first character `head` and the rest of the string `tail`.
3. 3. Recursively call the function on `tail` to get the reversed tail.
4. 4. Return the result of the reversed tail concatenated with `head`.

## Complexity Analysis

- **Time:** O(N^2) in this specific Python implementation because string slicing `s[1:]` creates a copy at each recursive step, leading to N + (N-1) + ... + 1 operations.
- **Space:** O(N^2) due to the call stack depth of N and the creation of N intermediate string objects of decreasing size.

## Edge Cases

- Empty string: The base case len(s) <= 1 handles this by returning '' immediately.
- Single character string: The base case returns the string immediately.
- Large string (up to 1000): The default recursion limit is usually 1000, which covers the constraint perfectly without needing `sys.setrecursionlimit`.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def reverse_string(s: str) -> str:
    """Reverses a string using recursion."""
    if len(s) <= 1:
        return s
    
    return reverse_string(s[1:]) + s[0]
```
