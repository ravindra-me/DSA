# Problem 5: Design a Chained Hash Map with Dynamic Rehashing

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Internal hash map architecture: buckets, collisions, load factor, rehashing | [Day 16: HashMap](../README.md) |

## Problem Statement

Implement a simplified integer-to-integer hash map from scratch (`MyHashMap`) using separate chaining with singly linked lists (or raw nodes) and an explicit array of buckets.

You must implement:
- `__init__(initial_capacity: int = 8, load_factor_threshold: float = 0.75)`: Initializes the hash map with a fixed initial capacity (number of buckets) and load factor threshold.
- `put(key: int, value: int) -> None`: Inserts or updates the key-value pair. If the ratio `size / capacity > load_factor_threshold` after insertion, double the bucket capacity and rehash all keys.
- `get(key: int) -> int`: Returns the value mapped to `key`, or `-1` if not found.
- `remove(key: int) -> bool`: Removes `key` and returns `True` if it was present, `False` otherwise.
- `size() -> int`: Returns the total number of key-value pairs.
- `capacity() -> int`: Returns the current number of buckets.

*Constraint*: You may NOT use Python's built-in `dict` or `set` in your implementation.

## Input

Method calls on `MyHashMap` instances.

## Output

Corresponding return values for `get`, `remove`, `size`, and `capacity`.

## Constraints

- 0 <= key, value <= 10^6
- initial_capacity >= 2
- 0.1 <= load_factor_threshold <= 0.9
- At most 2 * 10^4 total method calls.

## Examples

**Example 1**

```text
Input:  hm = MyHashMap(2, 0.75)
hm.put(1, 10)
hm.capacity()
hm.put(2, 20)
hm.capacity()
hm.get(1)
hm.remove(1)
hm.get(1)
Output: hm.capacity() -> 2
hm.capacity() -> 4 (size 2/2 = 1.0 > 0.75, doubled)
hm.get(1) -> 10
hm.remove(1) -> True
hm.get(1) -> -1
```

Illustrates insertion, load factor trigger, resizing, and deletion.

**Example 2**

```text
Input:  hm = MyHashMap(4, 0.75)
hm.get(99)
Output: -1
```

Lookup of a non-existent key returns -1.

## Function Signature

```python
class MapNode:
    def __init__(self, key: int, value: int, next_node: 'MapNode | None' = None):
        self.key = key
        self.value = value
        self.next = next_node

class MyHashMap:
    def __init__(self, initial_capacity: int = 8, load_factor_threshold: float = 0.75) -> None:
        """Initialize hash map with initial bucket capacity and threshold."""
        pass

    def put(self, key: int, value: int) -> None:
        """Insert or update (key, value). Rehash if load factor threshold exceeded."""
        pass

    def get(self, key: int) -> int:
        """Return value for key, or -1 if not found."""
        pass

    def remove(self, key: int) -> bool:
        """Remove key; return True if removed, False if not present."""
        pass

    def size(self) -> int:
        """Return total number of key-value pairs stored."""
        pass

    def capacity(self) -> int:
        """Return the number of buckets."""
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use an internal list of bucket heads representing linked list nodes. Hash keys via `abs(hash_func(key)) % capacity`. Track element count, and when `count / capacity > threshold`, allocate a new array of $2 \times \text{capacity}$ and re-insert all nodes.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
