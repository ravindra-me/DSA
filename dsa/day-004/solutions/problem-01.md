# Solution 1: Sum of Array

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Base recursion on linear structures

## Approach

The sum of a list can be defined recursively: the sum of an empty list is 0, and the sum of a non-empty list is its first element plus the sum of the remaining list elements. We use Python slicing to reduce the problem size at each step.

## Thought Process

The problem asks for a summation of a linear data structure. A standard iterative approach uses a loop accumulator. To solve this recursively, we observe the optimal substructure: `sum([x, y, z])` is `x + sum([y, z])`. By breaking the list into a head (first element) and a tail (rest of the list), we reduce the problem to a smaller subproblem of the same type, converging toward the base case of an empty list.

## Algorithm

1. 1. Define the base case: If the input list is empty, return 0.
2. 2. Define the recursive step: Return the sum of the first element plus the result of recursively calling the function on the slice of the list from the second element onwards.
3. 3. Because Python recursion limit is typically 1000, ensure the solution handles constraints up to 1000 safely.

## Complexity Analysis

- **Time:** O(N) where N is the number of elements in the array, as each element is processed exactly once.
- **Space:** O(N) due to the recursive call stack depth, which grows linearly with the size of the input list.

## Edge Cases

- Empty list: Handled by the base case, returns 0.
- Single element: The recursive call gets an empty list, returns 0 + element.
- Negative numbers: Addition works correctly regardless of sign.
- Maximum size (1000): Python's default recursion limit is usually 1000. 1000 elements should fit safely.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
import sys

# Increase recursion depth to handle constraints up to 1000 safely.
sys.setrecursionlimit(2000)

def recursive_sum(arr: list[int]) -> int:
    """Calculates the sum of a list recursively using an index helper."""
    def _helper(index: int) -> int:
        if index == len(arr):
            return 0
        return arr[index] + _helper(index + 1)

    return _helper(0)
```
