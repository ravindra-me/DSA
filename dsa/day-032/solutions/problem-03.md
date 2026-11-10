# Solution 3: Remove All Adjacent Duplicates in String II

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium/Hard | **Concept:** State compression using dynamic dynamic frequency stacks

## Approach

We maintain a stack of `[char, count]` pairs. As we iterate through string `s`, if the current character matches the character at the top of the stack, we increment its count. When a character's count reaches `k`, we pop it from the stack. Otherwise, we push a new `[char, 1]` pair onto the stack. Finally, we reconstruct the result string by expanding the character-count pairs remaining on the stack.

## Thought Process

A naive simulation repeatedly scans the string for `k` identical adjacent characters, deletes them, and restarts or backtracks. Deleting from a string takes $O(N)$ time and can be repeated up to $O(N/k)$ times, leading to an $O(N^2 / k)$ total time complexity, which will time out for $N = 10^5$.

By using a stack to keep track of characters along with their consecutive frequencies (state compression), we eliminate the need to re-scan the string after a deletion. Each character is pushed onto the stack once and popped at most once, reducing the time complexity to $O(N)$ time and $O(N)$ space.

## Algorithm

1. Initialize an empty stack `stack` to store lists of `[char, count]`.
2. Iterate through each character `char` in string `s`.
3. If `stack` is not empty and `stack[-1][0] == char`, increment `stack[-1][1]` by 1.
4. Else, append `[char, 1]` to `stack`.
5. Check if `stack[-1][1] == k`. If true, pop the top element from `stack`.
6. After iterating through all characters, reconstruct the final string by joining `char * count` for each `[char, count]` in `stack`.

## Complexity Analysis

- **Time:** $O(N)$ where $N$ is the length of string `s`. Each character is processed once during iteration and popping takes $O(1)$ time.
- **Space:** $O(N)$ to store the stack elements in the worst case (when no deletions occur).

## Edge Cases

- No duplicates equal to `k`: The stack retains all elements, returning the original string.
- Entire string gets removed: Stack becomes empty, returning an empty string `""`.
- Cascading removals: Removals reveal previous identical characters that form a group of `k`, correctly handled by incrementing the count of the now-top element.
- Large input length ($10^5$): Handled efficiently in $O(N)$ without triggering recursion limit or memory limits.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def remove_k_duplicates(s: str, k: int) -> str:
    """Remove all k-adjacent duplicates from string s repeatedly."""
    stack = []  # Element structure: [char, count]
    
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([char, 1])
            
    return "".join(char * count for char, count in stack)
```
