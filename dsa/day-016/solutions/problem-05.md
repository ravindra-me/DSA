# Solution 5: Design a Chained Hash Map with Dynamic Rehashing

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Internal hash map architecture: buckets, collisions, load factor, rehashing

## Approach

A fixed-size array of buckets holds head pointers to singly linked lists (`MapNode`). Keys are mapped to buckets via `hash_code % capacity`. Dynamic resizing doubles the bucket array and redistributes all existing nodes whenever `size / capacity > load_factor_threshold` after an insertion.

## Thought Process

A hash map provides $O(1)$ expected time dictionary operations by mapping integer keys to bucket indices. Without relying on built-in dictionaries, separate chaining handles hash collisions gracefully using singly linked list chains.

To ensure constant amortized operation time, the average bucket chain length must be kept bounded by a constant factor $\alpha$ (the load factor threshold). When inserting a new key, we traverse the target bucket's chain. If the key exists, we update its value in-place without altering `size`. If the key is new, we prepend or append a new node and increment `size`. Next, if `size / capacity > threshold`, we allocate a new bucket table of size `2 * capacity` and rehash every node into the new table. Deletions traverse the chain with a predecessor pointer to unlink nodes.

## Algorithm

1. Initialize `_capacity`, `_threshold`, `_size = 0`, and `_buckets` as a list of `None` of length `_capacity`.
2. Hash function: compute `index = key % self._capacity`.
3. put(key, value): locate bucket `index`. Traverse list: if `curr.key == key`, update `curr.value = value` and return. Else, prepend `MapNode(key, value, next=self._buckets[index])` to the bucket and increment `_size`. If `self._size / self._capacity > self._threshold`, trigger `_rehash()`.
4. _rehash(): store old buckets, double `self._capacity`, allocate a new bucket array of `None`s of new capacity. For every node in old buckets, compute `new_index = node.key % self._capacity`, unlink and insert into `new_index` bucket.
5. get(key): locate bucket `index = key % self._capacity`. Traverse list; return `node.value` if found, else `-1`.
6. remove(key): locate bucket `index`. Traverse list keeping track of `prev`. If node found, adjust `prev.next = curr.next` (or head if `prev` is `None`), decrement `_size`, and return `True`. If not found, return `False`.
7. size() and capacity(): return `_size` and `_capacity` respectively.

## Complexity Analysis

- **Time:** Average $O(1)$ amortized for `put`, and average $O(1)$ worst-case per operation for `get` and `remove`. Rehashing takes $O(N + C)$ time when triggered, which amortizes to $O(1)$ per insertion.
- **Space:** $O(N + C)$ auxiliary space where $N$ is the number of elements and $C$ is bucket capacity.

## Edge Cases

- Zero key: `0 % capacity == 0`, works naturally with modulo arithmetic.
- Updating existing key: does not increment size and must not trigger rehashing.
- Load factor threshold boundary: rehashing triggers strictly when `size / capacity > threshold`.
- Removing the head of a bucket list vs removing an interior/tail node.
- Multiple collisions hashing to the exact same bucket.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
from typing import Optional


class MapNode:
    def __init__(self, key: int, value: int, next_node: Optional['MapNode'] = None):
        self.key: int = key
        self.value: int = value
        self.next: Optional['MapNode'] = next_node


class MyHashMap:
    def __init__(self, initial_capacity: int = 8, load_factor_threshold: float = 0.75) -> None:
        """Initialize hash map with initial bucket capacity and threshold."""
        self._capacity: int = max(2, initial_capacity)
        self._threshold: float = load_factor_threshold
        self._size: int = 0
        self._buckets: list[Optional[MapNode]] = [None] * self._capacity

    def _hash(self, key: int) -> int:
        return key % self._capacity

    def _rehash(self) -> None:
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [None] * self._capacity

        for head in old_buckets:
            curr = head
            while curr is not None:
                next_node = curr.next
                new_index = self._hash(curr.key)
                curr.next = self._buckets[new_index]
                self._buckets[new_index] = curr
                curr = next_node

    def put(self, key: int, value: int) -> None:
        """Insert or update (key, value). Rehash if load factor threshold exceeded."""
        index = self._hash(key)
        curr = self._buckets[index]
        while curr is not None:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        new_node = MapNode(key, value, self._buckets[index])
        self._buckets[index] = new_node
        self._size += 1

        if (self._size / self._capacity) > self._threshold:
            self._rehash()

    def get(self, key: int) -> int:
        """Return value for key, or -1 if not found."""
        index = self._hash(key)
        curr = self._buckets[index]
        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> bool:
        """Remove key; return True if removed, False if not present."""
        index = self._hash(key)
        curr = self._buckets[index]
        prev: Optional[MapNode] = None

        while curr is not None:
            if curr.key == key:
                if prev is None:
                    self._buckets[index] = curr.next
                else:
                    prev.next = curr.next
                self._size -= 1
                return True
            prev = curr
            curr = curr.next
        return False

    def size(self) -> int:
        """Return total number of key-value pairs stored."""
        return self._size

    def capacity(self) -> int:
        """Return the number of buckets."""
        return self._capacity
```
