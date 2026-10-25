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
