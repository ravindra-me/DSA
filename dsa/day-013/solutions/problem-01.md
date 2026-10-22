# Solution 1: Design Circular Queue

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Fixed-capacity circular buffer with modular arithmetic

## Approach

Maintain a fixed-size array of capacity $k$ alongside a `head` index pointing to the first element and an explicit `size` counter. Modular arithmetic handles index wrapping when advancing `head` or computing the tail index `(head + size - 1) % capacity`.

## Thought Process

A naive implementation using a standard list with `pop(0)` takes $O(N)$ time per dequeue because all remaining elements shift left. To achieve $O(1)$ operations, we allocate a fixed-size buffer of capacity $k$.

Instead of shifting elements, we move two pointer-like indices: `head` and `tail`. Tracking the current `size` explicitly eliminates the classic ambiguity where `head == tail` could mean either completely empty or completely full. Any operation that moves forward simply takes `(index + 1) % capacity`.

## Algorithm

1. Initialize an internal array `buffer` of length $k$ filled with a sentinel (e.g., None), `head = 0`, `size = 0`, and `capacity = k`.
2. is_empty: return `size == 0`.
3. is_full: return `size == capacity`.
4. enqueue(value): if full, return `False`. Calculate tail position via `(head + size) % capacity`. Write `buffer[tail] = value`, increment `size` by 1, and return `True`.
5. dequeue(): if empty, return `False`. Advance `head = (head + 1) % capacity`, decrement `size` by 1, and return `True`.
6. front(): if empty, return `-1`. Otherwise, return `buffer[head]`.
7. rear(): if empty, return `-1`. Otherwise, compute `tail = (head + size - 1) % capacity` and return `buffer[tail]`.

## Complexity Analysis

- **Time:** O(1) for all methods: enqueue, dequeue, front, rear, is_empty, and is_full perform constant number of arithmetic operations and array index accesses.
- **Space:** O(k) where k is the capacity of the queue, required to store up to k elements in a pre-allocated fixed-size buffer.

## Edge Cases

- Capacity k = 1: the queue can alternate between empty and full immediately with single enqueue and dequeue calls.
- Queue full on enqueue: must reject with False without modifying queue state.
- Queue empty on dequeue, front, rear: dequeue returns False; front and rear return -1.
- Continuous wrap-around: repeatedly enqueuing and dequeuing advances indices past capacity multiple times without off-by-one errors.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
class CircularQueue:
    def __init__(self, k: int) -> None:
        """Initialize the queue with capacity k."""
        self._capacity: int = k
        self._buffer: list[int] = [0] * k
        self._head: int = 0
        self._size: int = 0

    def enqueue(self, value: int) -> bool:
        """Insert value. Return True if successful, False if full."""
        if self.is_full():
            return False
        tail_index = (self._head + self._size) % self._capacity
        self._buffer[tail_index] = value
        self._size += 1
        return True

    def dequeue(self) -> bool:
        """Delete front value. Return True if successful, False if empty."""
        if self.is_empty():
            return False
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return True

    def front(self) -> int:
        """Return front value, or -1 if empty."""
        if self.is_empty():
            return -1
        return self._buffer[self._head]

    def rear(self) -> int:
        """Return rear value, or -1 if empty."""
        if self.is_empty():
            return -1
        tail_index = (self._head + self._size - 1) % self._capacity
        return self._buffer[tail_index]

    def is_empty(self) -> bool:
        """Check whether queue is empty."""
        return self._size == 0

    def is_full(self) -> bool:
        """Check whether queue is full."""
        return self._size == self._capacity
```
