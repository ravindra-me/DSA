# Solution 4: Remove Duplicate Letters to Form Smallest Subsequence

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Monotonic stack with character frequency and seen tracking

## Approach

We build the result greedily using a monotonic stack. As we iterate through each character, if it is not already in the stack and is smaller than the stack's top, we can pop the top character provided that the top character appears again later in the string.

## Thought Process

A naive brute-force approach would generate all possible subsequences containing every unique character exactly once, sort them lexicographically, and return the minimum. However, there can be up to $2^N$ subsequences, which is intractable for $N = 10^4$.

To optimize, observe that a character earlier in the string has a much higher impact on lexicographical order than characters later on. If we see a character `c` that is smaller than the current last character in our result, we prefer putting `c` earlier. But we can only discard the previous character if we know it will appear again later in `s` (so we do not permanently lose it).

This leads naturally to a greedy monotonic stack approach:
1. Precompute the last index where each character appears in `s`.
2. Iterate through `s` character by character.
3. If a character is already present in our stack, we skip it because keeping its earliest valid position is always optimal given our greedy popping rule.
4. Otherwise, while the stack is non-empty, the current character is smaller than `stack[-1]`, and `stack[-1]` occurs again later (i.e. `last_occurrence[stack[-1]] > current_index`), pop `stack[-1]` and mark it as no longer in the stack.
5. Push the current character onto the stack and mark it as seen.
6. Finally, join the stack into the resulting string.

## Algorithm

1. Scan `s` to record the last index of each character in a hash map `last_occurrence`.
2. Initialize an empty stack `stack` and a set/boolean array `in_stack` to track characters currently included in `stack`.
3. Iterate through each character `char` with its index `idx` in `s`.
4. If `char` is already in `in_stack`, continue to the next character.
5. While `stack` is not empty, `char < stack[-1]`, and `last_occurrence[stack[-1]] > idx`, pop from `stack` and remove the popped character from `in_stack`.
6. Append `char` to `stack` and add `char` to `in_stack`.
7. After the loop finishes, return the characters in `stack` joined as a string.

## Complexity Analysis

- **Time:** O(N) where N is the length of `s`. Each character is pushed and popped at most once, and alphabet size is bounded by 26.
- **Space:** O(1) auxiliary space beyond the output string, as the stack, hash map, and set contain at most 26 lowercase English letters.

## Edge Cases

- Single character string: the loop runs once and returns the character directly.
- Already sorted unique characters (e.g., 'abc'): no characters are popped, stack remains 'abc'.
- Reverse sorted characters with duplicates (e.g., 'cba'): characters cannot be dropped if they don't appear later, so relative order is preserved.
- All identical characters (e.g., 'aaaa'): only the first character is pushed, duplicates are skipped.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def remove_duplicate_letters(s: str) -> str:
    """Return the lexicographically smallest subsequence containing every unique letter once."""
    last_occurrence = {char: idx for idx, char in enumerate(s)}
    stack: list[str] = []
    seen: set[str] = set()

    for idx, char in enumerate(s):
        if char in seen:
            continue

        while stack and char < stack[-1] and last_occurrence[stack[-1]] > idx:
            removed = stack.pop()
            seen.remove(removed)

        stack.append(char)
        seen.add(char)

    return "".join(stack)
```
