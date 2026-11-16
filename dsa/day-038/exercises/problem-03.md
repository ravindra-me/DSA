# Problem 3: Circular Buffer with Overwrite and Range Read

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Fixed-capacity circular buffer with overwrite eviction and historical reading | [Day 38: Queue](../README.md) |

## Problem Statement

Design a bounded ring buffer `OverwriteBuffer` with fixed capacity $k$ that stores integers. When an element is added to a full buffer, it automatically overwrites the oldest element in the buffer.

Implement the following methods:
- `__init__(capacity: int)`: Initializes the buffer with maximum capacity `capacity`.
- `push(val: int) -> None`: Inserts `val` at the rear. If full, the oldest element is evicted.
- `pop_oldest() -> int`: Removes and returns the oldest element. If the buffer is empty, return `-1`.
- `get_last_k(m: int) -> list[int]`: Returns up to `m` most recently added elements in chronological order (oldest to newest among those $m$). If the buffer holds fewer than `m` elements, return all existing elements in chronological order.

## Input

Method parameters as typed in the signature.

## Output

`pop_oldest` returns `int`. `get_last_k` returns `list[int]`.

## Constraints

- 1 <= capacity <= 2000
- 0 <= val <= 10^9
- 1 <= m <= capacity
- At most 10^4 total method calls.

## Examples

**Example 1**

```text
Input:  buf = OverwriteBuffer(3)
buf.push(1)
buf.push(2)
buf.push(3)
buf.push(4)  # Overwrites 1
buf.get_last_k(2)  # [3, 4]
buf.pop_oldest()  # returns 2
buf.get_last_k(2)  # [3, 4]
Output: [3, 4], 2, [3, 4]
```

Buffer maintains at most 3 items. Pushing 4 drops 1. pop_oldest removes 2.

**Example 2**

```text
Input:  buf = OverwriteBuffer(2)
buf.pop_oldest()
Output: -1
```

Empty buffer returns -1 on pop_oldest.

## Function Signature

```python
class OverwriteBuffer:
    def __init__(self, capacity: int) -> None:
        """Initialize the overwrite ring buffer with a fixed capacity."""
        pass

    def push(self, val: int) -> None:
        """Push val, overwriting the oldest item if full."""
        pass

    def pop_oldest(self) -> int:
        """Pop and return the oldest item, or -1 if empty."""
        pass

    def get_last_k(self, m: int) -> list[int]:
        """Return up to m newest elements in chronological order."""
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a circular array with explicit head pointer and current size. Compute modular offsets for both oldest and newest sub-ranges in O(m) time without shifting elements.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
