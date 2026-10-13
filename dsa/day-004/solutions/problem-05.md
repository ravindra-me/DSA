# Solution 5: Generate Parentheses

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Backtracking / Combinatorial recursion

## Approach

Use backtracking to build the string character by character, maintaining counts of open and closed parentheses placed so far. A combination is valid only if, at any point, the number of closed parentheses does not exceed the number of open ones, and we stop once we have placed `n` of each.

## Thought Process

A naive approach might generate all 2^(2n) possible parenthesis strings and filter them, which is incredibly inefficient. Instead, we can construct the string incrementally. We have two choices at each step: add an '(' if we have not used all `n` openers, or add a ')' if we have more open than closed parentheses. This pruning ensures we only explore paths that could possibly lead to a valid string, effectively solving the problem using the Catalan number property, which relates to the number of valid parenthesis combinations.

## Algorithm

1. 1. Define a recursive helper function that takes the current string state and counts of open and closed parentheses.
2. 2. If the current string length is 2 * n, it is complete; add it to the results list.
3. 3. If 'open' count is less than n, we can always add an '(' and recurse.
4. 4. If 'closed' count is less than 'open', we can add a ')' and recurse.
5. 5. Initialize the process with an empty string and 0 counts for both.
6. 6. Return the collected list of valid strings.

## Complexity Analysis

- **Time:** O(4^n / sqrt(n)). The number of valid parentheses combinations is given by the n-th Catalan number, which is asymptotic to 4^n / (n * sqrt(n)). In our backtracking approach, we perform constant work at each step of the recursion tree.
- **Space:** O(n) for the recursion stack depth, excluding the space required to store the output.

## Edge Cases

- n=1: Base case, should return ['()'].
- n=8: Maximum constraint, ensures recursion depth is handled (recursion limit is usually 1000, 16 is fine).

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
from typing import List

def generate_parentheses(n: int) -> List[str]:
    """Generates all combinations of well-formed parentheses for n pairs."""
    if n <= 0:
        return []
    
    results = []
    
    def backtrack(current: str, open_count: int, closed_count: int) -> None:
        if len(current) == 2 * n:
            results.append(current)
            return
        
        if open_count < n:
            backtrack(current + "(", open_count + 1, closed_count)
            
        if closed_count < open_count:
            backtrack(current + ")", open_count, closed_count + 1)
            
    backtrack("", 0, 0)
    return results
```
