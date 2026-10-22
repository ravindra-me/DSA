# Problem 1: Design Circular Queue

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Fixed-capacity circular buffer with modular arithmetic | [Day 13: Queue](../README.md) |

## Problem Statement

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called 'Ring Buffer'.

Implement the `CircularQueue` class:
- `CircularQueue(k: int)`: Initializes the object with the size of the queue to be `k`.
- `enqueue(value: int) -> bool`: Inserts an element into the circular queue. Return `True` if the operation is successful, or `False` if the queue is full.
- `dequeue() -> bool`: Deletes an element from the circular queue. Return `True` if the operation is successful, or `False` if the queue is empty.
- `front() -> int`: Gets the front item from the queue. If the queue is empty, return `-1`.
- `rear() -> int`: Gets the last item from the queue. If the queue is empty, return `-1`.
- `is_empty() -> bool`: Checks whether the circular queue is empty or not.
- `is_full() -> bool`: Checks whether the circular queue is full or not.

You must not use Python's built-in `collections.deque` or dynamic resizing `list.pop(0)`.

## Input

Class method invocations with integer values and capacities.

## Output

Booleans for status checks and enqueue/dequeue operations; integers for front/rear inspections.

## Constraints

- 1 <= k <= 1000
- 0 <= value <= 1000
- At most 3000 calls will be made to enqueue, dequeue, front, rear, is_empty, and is_full.

## Examples

**Example 1**

```text
Input:  q = CircularQueue(3)
q.enqueue(1) -> True
q.enqueue(2) -> True
q.enqueue(3) -> True
q.enqueue(4) -> False
q.rear() -> 3
q.is_full() -> True
q.dequeue() -> True
q.enqueue(4) -> True
q.rear() -> 4
Output: True, True, True, False, 3, True, True, True, 4
```

After dequeuing 1, slot 0 opens up, allowing 4 to be successfully enqueued at the wrapped index.

**Example 2**

```text
Input:  q = CircularQueue(1)
q.is_empty() -> True
q.front() -> -1
q.dequeue() -> False
Output: True, -1, False
```

An empty queue returns -1 for front/rear and False for dequeue.

## Function Signature

```python
class CircularQueue:
    def __init__(self, k: int) -> None:
        """Initialize the queue with capacity k."""
        pass

    def enqueue(self, value: int) -> bool:
        """Insert value. Return True if successful, False if full."""
        pass

    def dequeue(self) -> bool:
        """Delete front value. Return True if successful, False if empty."""
        pass

    def front(self) -> int:
        """Return front value, or -1 if empty."""
        pass

    def rear(self) -> int:
        """Return rear value, or -1 if empty."""
        pass

    def is_empty() -> bool:
        """Check whether queue is empty."""
        pass

    def is_full() -> bool:
        """Check whether queue is full."""
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a fixed-size list of capacity k, tracking `head`, `count`, and capacity `k`. Compute the rear index using `(head + count - 1) % k`.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
