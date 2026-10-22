# Solution 2: Implement Queue using Stacks

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Emulating FIFO behavior using two LIFO stacks

## Approach

Maintain two stacks: `in_stack` to accept incoming elements and `out_stack` to serve outgoing elements. When popping or peeking, if `out_stack` is empty, transfer all elements from `in_stack` to `out_stack`, reversing their order to achieve FIFO behavior in amortized $O(1)$ time.

## Thought Process

A stack is Last-In-First-Out (LIFO), whereas a queue is First-In-First-Out (FIFO). Reversing a sequence twice yields the original sequence.

A naive approach might move all elements from one stack to another on every single `push` or every single `pop`, resulting in $O(N)$ operations for each queue operation. However, we can be lazy with transfers:
1. Incoming elements are pushed directly onto `in_stack` in $O(1)$.
2. When a `pop` or `peek` is requested, we need the oldest element. If `out_stack` already contains elements, its top is already the oldest element in the queue, requiring $O(1)$ time.
3. Only when `out_stack` is empty do we dump all elements from `in_stack` into `out_stack`. This reverses the order of elements in `in_stack` so that the oldest element lands at the top of `out_stack`.

Each element enters `in_stack` once and `out_stack` once, giving an amortized time complexity of $O(1)$ per operation.

## Algorithm

1. Initialize two empty lists `in_stack` and `out_stack`.
2. For `push(x)`: append `x` to `in_stack`.
3. Create a helper `_shift_stacks()`: if `out_stack` is empty, while `in_stack` has elements, pop from `in_stack` and append to `out_stack`.
4. For `peek()`: call `_shift_stacks()`, then return the top element of `out_stack` (`self.out_stack[-1]`).
5. For `pop()`: call `peek()`, then pop and return the top element from `out_stack`.
6. For `empty()`: return `True` if both `in_stack` and `out_stack` are empty, else `False`.

## Complexity Analysis

- **Time:** Amortized $O(1)$ for `push`, `pop`, `peek`, and `empty`. While a single `pop` or `peek` can take $O(N)$ when shifting, each element is moved at most once from `in_stack` to `out_stack`, bounding total work over $N$ operations to $O(N)$.
- **Space:** $O(N)$ total space where $N$ is the number of elements currently in the queue, distributed across `in_stack` and `out_stack`.

## Edge Cases

- Single element: push and immediately pop or peek; works correctly as `_shift_stacks` moves the single item.
- Interleaved push and pop: elements pushed after a shift remain in `in_stack` until `out_stack` is completely exhausted, preserving FIFO ordering.
- Checking `empty()` when elements exist in either stack: must check both stacks are empty, not just one.
- Consecutive peeks: `_shift_stacks` only shifts once when `out_stack` is empty; subsequent peeks are $O(1)$ reads from `out_stack`.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
class StackQueue:
    """FIFO queue implemented using two LIFO stacks."""

    def __init__(self) -> None:
        """Initialize data structures."""
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []

    def push(self, x: int) -> None:
        """Push element x to the back of the queue."""
        self.in_stack.append(x)

    def _shift_stacks(self) -> None:
        """Move elements from in_stack to out_stack if out_stack is empty."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        """Remove and return the element from front of queue."""
        self._shift_stacks()
        return self.out_stack.pop()

    def peek(self) -> int:
        """Get the front element."""
        self._shift_stacks()
        return self.out_stack[-1]

    def empty(self) -> bool:
        """Return whether the queue is empty."""
        return not self.in_stack and not self.out_stack
```
