# Solution 3: Amortized Queue via Stacks

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Amortized time complexity analysis

## Approach

Maintain two stacks (`_in_stack` and `_out_stack`). Incoming elements are pushed onto `_in_stack`. When `pop()` or `peek()` needs an element, if `_out_stack` is empty, all elements are moved one-by-one from `_in_stack` to `_out_stack`, reversing their order and placing the oldest element at the top.

## Thought Process

A single stack only supports LIFO (last-in, first-out) order. Reversing the order of elements requires popping them all into a second stack. A naive implementation might transfer elements to the second stack on every single `push` or every single `pop` and immediately transfer them back, resulting in $O(n)$ time for every operation and $O(n^2)$ total runtime for $n$ operations. 

Instead, we adopt a lazy transfer strategy: keep elements in `_in_stack` until an extraction (`pop` or `peek`) specifically needs them. When `_out_stack` runs empty, we dump the entire contents of `_in_stack` into `_out_stack`. Because each element is pushed to `_in_stack` once, popped from `_in_stack` once, pushed to `_out_stack` once, and popped from `_out_stack` once, each element incurs at most 4 stack operations across its entire lifecycle in the queue. Thus, $n$ queue operations take at most $O(n)$ total work, which is $O(1)$ amortized per operation.

## Algorithm

1. Initialize two internal lists `_in_stack` and `_out_stack` as empty lists.
2. For `push(x)`: Append `x` directly to `_in_stack` in $O(1)$ time.
3. Define a helper `_shift()`: If `_out_stack` is empty, repeatedly pop the top element from `_in_stack` and append it to `_out_stack` until `_in_stack` is exhausted.
4. For `peek()`: Call `_shift()`, then inspect and return the last element of `_out_stack`.
5. For `pop()`: Call `_shift()`, then pop and return the last element of `_out_stack`.
6. For `empty()`: Return `True` if both `_in_stack` and `_out_stack` are empty, else `False`.

## Complexity Analysis

- **Time:** $O(1)$ amortized for `push`, `pop`, `peek`, and `empty`. While a single `pop` or `peek` can take $O(n)$ worst-case time when `_out_stack` is empty, any sequence of $m$ operations requires at most $4m$ underlying stack actions, yielding $O(1)$ amortized time per operation.
- **Space:** $O(n)$ auxiliary space to store $n$ elements distributed between `_in_stack` and `_out_stack`.

## Edge Cases

- Empty queue check at the start: Both stacks are empty, returning `True`.
- Single element lifecycle: Pushing one element and popping it immediately transfers that single element and leaves the queue empty.
- Interleaved push and pop: `_out_stack` is partially consumed while new elements arrive in `_in_stack`; `_shift()` must not overwrite or reorder `_out_stack` until it is completely drained.
- Multiple consecutive peek calls: `_shift()` moves elements once, and subsequent `peek()` calls take $O(1)$ worst-case without redundant transfers.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
class AmortizedQueue:
    """FIFO queue implemented using two LIFO stacks with amortized O(1) operations."""

    def __init__(self) -> None:
        self._in_stack: list[int] = []
        self._out_stack: list[int] = []

    def _shift(self) -> None:
        """Transfer elements from in_stack to out_stack if out_stack is empty."""
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())

    def push(self, x: int) -> None:
        """Push element x to the back of the queue."""
        self._in_stack.append(x)

    def pop(self) -> int:
        """Remove and return the element at the front of the queue."""
        self._shift()
        return self._out_stack.pop()

    def peek(self) -> int:
        """Return the element at the front of the queue without removing it."""
        self._shift()
        return self._out_stack[-1]

    def empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        return not self._in_stack and not self._out_stack
```
