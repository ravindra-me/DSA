from typing import Optional


class MapNode:
    def __init__(self, key: int, value: int, next_node: Optional['MapNode'] = None):
        self.key: int = key
        self.value: int = value
        self.next: Optional['MapNode'] = next_node


class MyHashMap:
    def __init__(self, initial_capacity: int = 8, load_factor_threshold: float = 0.75) -> None:
        """Initialize hash map with initial bucket capacity and threshold."""
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        """Insert or update (key, value). Rehash if load factor threshold exceeded."""
        raise NotImplementedError

    def get(self, key: int) -> int:
        """Return value for key, or -1 if not found."""
        raise NotImplementedError

    def remove(self, key: int) -> bool:
        """Remove key; return True if removed, False if not present."""
        raise NotImplementedError

    def size(self) -> int:
        """Return total number of key-value pairs stored."""
        raise NotImplementedError

    def capacity(self) -> int:
        """Return the number of buckets."""
        raise NotImplementedError
