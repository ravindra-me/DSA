# Solution 2: Remove Duplicate Letters Lexicographically

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Medium | **Concept:** Monotonic Stack with Hash Map / Frequency Count

## Approach

We use a monotonic stack combined with a character frequency count (or last-seen index map) and a `visited` set. As we iterate through string `s`, we decrement the character's remaining frequency count. If the character is already in our stack (`visited`), we skip it. Otherwise, while the stack top is lexicographically larger than the current character and the stack top character appears again later in `s`, we pop it from the stack and remove it from `visited`. Finally, we push the current character and mark it as visited.

## Thought Process

To get the lexicographically smallest string, we prefer smaller characters as early as possible. This naturally suggests a monotonic increasing stack. However, we can only remove a larger character from the top of the stack if we are guaranteed to see it again later in the string (checked via remaining frequency count or last index). A set `visited` ensures each character appears exactly once in the final result. This greedy stack approach runs in linear time $O(N)$, improving over an exponential brute-force search over all valid subsequences.

## Algorithm

1. Count the total occurrences of each character in `s` using a frequency map or array.
2. Initialize an empty stack and an empty `visited` set.
3. Iterate through each character `char` in `s`:
4. Decrement the remaining count of `char` in the frequency map.
5. If `char` is already in `visited`, continue to the next character.
6. While stack is not empty, `stack[-1] > char`, and frequency map of `stack[-1]` is greater than 0:
7. Pop the top character from `stack` and remove it from `visited`.
8. Push `char` onto `stack` and add `char` to `visited`.
9. Return the joined characters in `stack` as a string.

## Complexity Analysis

- **Time:** O(N) where N is the length of string `s`. Each character is pushed and popped from the stack at most once, and frequency table lookup/update takes O(1) time.
- **Space:** O(1) auxiliary space (or O(K) where K <= 26 is the alphabet size), since the stack, set, and frequency map store at most 26 distinct lowercase English letters.

## Edge Cases

- Single character string `s`: Stack processes 1 element and returns it directly.
- Already sorted or reverse sorted strings: Monotonic stack correctly pops elements when future occurrences exist or keeps them when no future occurrences remain.
- All identical characters (e.g., "aaaaa"): Reduces to a single character output "a".

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
from collections import Counter

def remove_duplicate_letters(s: str) -> str:
    """Remove duplicate letters to return lexicographically smallest result while preserving order."""
    count = Counter(s)
    stack = []
    visited = set()
    
    for char in s:
        count[char] -= 1
        if char in visited:
            continue
            
        while stack and stack[-1] > char and count[stack[-1]] > 0:
            removed = stack.pop()
            visited.remove(removed)
            
        stack.append(char)
        visited.add(char)
        
    return "".join(stack)
```
