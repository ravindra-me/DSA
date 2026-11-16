# Solution 3: Circular Buffer with Overwrite and Range Read

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium/Hard | **Concept:** Fixed-capacity circular buffer with overwrite eviction and historical reading

## Approach

We maintain a fixed-size array of length `capacity`, along with `head` (index of the oldest element) and `size` (number of active elements). Pushing appends at `(head + size) % capacity`; if the buffer is already full, `head` advances by 1 to discard the oldest element. `pop_oldest` increments `head` and decrements `size`. `get_last_k(m)` computes how many items to return ($c = \min(m, \text{size})$) and reads $c$ items starting from logical offset $\text{size} - c$ via modular indexing.

## Thought Process

A naive list-based approach might append elements and `pop(0)` when capacity is exceeded. However, `pop(0)` on a standard Python list takes $O(n)$ time due to shifting elements, which becomes inefficient under frequent insertions when full.

Using a circular array (ring buffer) allows $O(1)$ amortized and worst-case time for insertions and deletions. By tracking `head` and current `size`, we can easily:
1. Determine emptiness (`size == 0`) and fullness (`size == capacity`).
2. Calculate the rear index as `(head + size) % capacity` when inserting.
3. Advance `head = (head + 1) % capacity` when an overwrite occurs or on `pop_oldest`.
4. Access any relative offset $i$ from oldest to newest as `(head + i) % capacity` in $O(1)$ time per element.

## Algorithm

1. Initialize an array `buffer` of length `capacity` with 0, `head = 0`, and `size = 0`.
2. For `push(val)`: if `size == capacity`, advance `head = (head + 1) % capacity` and write `val` at `(head + capacity - 1) % capacity`. Otherwise, write `val` at `(head + size) % capacity` and increment `size`.
3. For `pop_oldest()`: if `size == 0`, return -1. Otherwise, fetch `val = buffer[head]`, update `head = (head + 1) % capacity`, decrement `size`, and return `val`.
4. For `get_last_k(m)`: set count $c = \min(m, \text{size})$. Calculate start offset `start = size - c`. Iterate $i$ from 0 to $c - 1$, collecting `buffer[(head + start + i) % capacity]` into a list, and return it.

## Complexity Analysis

- **Time:** `push` is $O(1)$, `pop_oldest` is $O(1)$, and `get_last_k(m)` is $O(\min(m, \text{size}))$.
- **Space:** $O(k)$ where $k$ is `capacity` to store the fixed array.

## Edge Cases

- `capacity == 1`: overwriting replaces the single element, `pop_oldest` empties it immediately.
- `pop_oldest` when empty: correctly returns -1.
- `m > size`: returns all `size` elements currently stored without crashing.
- `val == 0`: 0 is a valid value and should not be confused with empty slots.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
class OverwriteBuffer:
    def __init__(self, capacity: int) -> None:
        """Initialize the overwrite ring buffer with a fixed capacity."""
        self._capacity = capacity
        self._buffer: list[int] = [0] * capacity
        self._head = 0
        self._size = 0

    def push(self, val: int) -> None:
        """Push val, overwriting the oldest item if full."""
        if self._size == self._capacity:
            # Overwrite oldest element: write at current head and advance head
            self._buffer[self._head] = val
            self._head = (self._head + 1) % self._capacity
        else:
            idx = (self._head + self._size) % self._capacity
            self._buffer[idx] = val
            self._size += 1

    def pop_oldest(self) -> int:
        """Pop and return the oldest item, or -1 if empty."""
        if self._size == 0:
            return -1
        val = self._buffer[self._head]
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return val

    def get_last_k(self, m: int) -> list[int]:
        """Return up to m newest elements in chronological order."""
        count = min(m, self._size)
        start_offset = self._size - count
        result: list[int] = []
        for i in range(count):
            idx = (self._head + start_offset + i) % self._capacity
            result.append(self._buffer[idx])
        return result
```
