# Solution 4: Design Min-Stack with Constant Time Minimum

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Auxiliary stack invariant for auxiliary queries

## Approach

Maintain two parallel stacks: a primary stack holding all pushed values, and an auxiliary `min_stack` where the top element always represents the minimum value currently in the primary stack. When pushing a value `val`, push `val` onto the primary stack and `min(val, min_stack[-1])` onto the auxiliary stack. When popping, pop from both stacks. This guarantees $O(1)$ access to the current minimum at all times.

## Thought Process

A naive approach simply uses a single stack (list) for push and pop in $O(1)$ time, but scans the entire stack to find the minimum in $O(N)$ time on each `get_min()` call. If we have $30,000$ operations alternating between `push` and `get_min`, scanning takes $O(N^2)$ overall, which is too slow.

To achieve $O(1)$ for `get_min`, we need to track the minimum as elements are added and removed. Notice that stacks adhere to strict Last-In, First-Out (LIFO) semantics: elements are only removed in the exact reverse order of how they were added. Therefore, the minimum of the stack at depth $k$ is completely determined by the elements at depths $0 \dots k$ and never changes until depth $k$ is popped.

By tracking the running minimum alongside each element (or using a parallel `min_stack`), every stack prefix's minimum is stored and accessible in $O(1)$ time at the top of `min_stack`.

## Algorithm

1. Initialize two empty lists: `self._stack` to hold values and `self._min_stack` to hold prefix minimums.
2. For `push(val)`: append `val` to `self._stack`. If `self._min_stack` is empty, push `val` onto `self._min_stack`. Otherwise, push `min(val, self._min_stack[-1])` onto `self._min_stack`.
3. For `pop()`: pop the top item from both `self._stack` and `self._min_stack`.
4. For `top()`: return the last element of `self._stack` (`self._stack[-1]`).
5. For `get_min()`: return the last element of `self._min_stack` (`self._min_stack[-1]`).

## Complexity Analysis

- **Time:** $O(1)$ for all operations (`push`, `pop`, `top`, `get_min`). Each operation performs constant number of list appends, pops, or index accesses.
- **Space:** $O(N)$ where $N$ is the maximum number of elements in the stack at any time. We store at most $2N$ elements across both stacks.

## Edge Cases

- Single element: both stacks hold 1 element, `top()` and `get_min()` both return that element.
- Duplicate minimums: pushing the same minimum multiple times correctly replicates that minimum on `min_stack`, ensuring popping one copy preserves the minimum for the remaining elements.
- Decreasing / strictly increasing sequences: handled correctly as prefix minimum either updates or remains constant.
- Extreme 32-bit integer values ($-2^{31}$ to $2^{31} - 1$): standard Python arbitrary-precision integers handle boundary values without overflow.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
class MinStack:
    def __init__(self) -> None:
        """Initialize the stack and auxiliary minimum tracking stack."""
        self._stack: list[int] = []
        self._min_stack: list[int] = []

    def push(self, val: int) -> None:
        """Push element val onto stack and record current minimum."""
        self._stack.append(val)
        if not self._min_stack or val < self._min_stack[-1]:
            self._min_stack.append(val)
        else:
            self._min_stack.append(self._min_stack[-1])

    def pop(self) -> None:
        """Remove the top element from both stacks."""
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        """Return the top element of the primary stack."""
        return self._stack[-1]

    def get_min(self) -> int:
        """Retrieve the minimum element in constant time."""
        return self._min_stack[-1]
```
