# Problem 2: Implement Queue using Stacks

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Emulating FIFO behavior using two LIFO stacks | [Day 13: Queue](../README.md) |

## Problem Statement

Implement a First In First Out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `pop`, `peek`, and `empty`).

Implement the `StackQueue` class:
- `push(x: int) -> None`: Pushes element `x` to the back of the queue.
- `pop() -> int`: Removes the element from the front of the queue and returns it.
- `peek() -> int`: Returns the element at the front of the queue without removing it.
- `empty() -> bool`: Returns `True` if the queue is empty, `False` otherwise.

Notes:
- You must use only standard stack operations: push to top, peek/pop from top, size, and check if empty.
- Python `list` may be used, but you should only use `append()` and `pop()` from the end.

## Input

Method calls on `StackQueue`.

## Output

Return values for `pop`, `peek`, and `empty`.

## Constraints

- 1 <= x <= 10^9
- At most 1000 calls will be made to push, pop, peek, and empty.
- All calls to pop and peek are valid (queue is non-empty).

## Examples

**Example 1**

```text
Input:  q = StackQueue()
q.push(1)
q.push(2)
q.peek() -> 1
q.pop() -> 1
q.empty() -> False
Output: 1, 1, False
```

1 was pushed first, so it is peeked and popped first.

**Example 2**

```text
Input:  q = StackQueue()
q.push(10)
q.pop() -> 10
q.empty() -> True
Output: 10, True
```

Popping the single inserted element empties the queue.

## Function Signature

```python
class StackQueue:
    def __init__(self) -> None:
        """Initialize data structures."""
        pass

    def push(self, x: int) -> None:
        """Push element x to the back of the queue."""
        pass

    def pop(self) -> int:
        """Remove and return the element from front of queue."""
        pass

    def peek() -> int:
        """Get the front element."""
        pass

    def empty() -> bool:
        """Return whether the queue is empty."""
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain two stacks `in_stack` and `out_stack`. Push to `in_stack`. For peek/pop, transfer all elements from `in_stack` to `out_stack` only when `out_stack` is empty.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
