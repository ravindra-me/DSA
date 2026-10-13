# Solution 4: Nested List Sum

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Tree traversal

## Approach

We solve this by recursively traversing the list structure. The key is to treat the problem as a tree traversal where each element is a leaf (integer) or a branch (another list).

## Thought Process

The problem structure is recursive by definition: a nested list contains either integers or other nested lists. Iterative solutions require managing an explicit stack, whereas recursion leverages the implicit call stack to handle arbitrary nesting depths cleanly. The brute force approach here is essentially the same as the optimal recursive approach since we must visit every single integer exactly once.

## Algorithm

1. Initialize a sum variable to 0.
2. Iterate through each item in the input list.
3. If the item is an integer, add it to the sum.
4. If the item is a list, recursively call the function on that item and add the result to the sum.
5. Return the total sum accumulated.

## Complexity Analysis

- **Time:** O(N) where N is the total number of elements (integers and lists) in the structure, as we must visit each node once.
- **Space:** O(D) where D is the maximum depth of the nesting, due to the call stack.

## Edge Cases

- Empty lists: The function naturally returns 0 as the loop will not execute.
- Negative integers: The logic uses addition, which naturally handles negative values correctly.
- Deeply nested lists: The solution uses standard recursion. For extremely deep structures, one might need `sys.setrecursionlimit`.
- Single element list: Handled by the iteration logic correctly.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
import sys

def nested_sum(nested_list: list) -> int:
    """Calculates sum of all integers in a nested list structure."""
    # Increase recursion depth for deep nesting scenarios
    sys.setrecursionlimit(2000)
    
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            total += nested_sum(element)
        else:
            total += element
    return total
```
