from typing import Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """Partition list such that nodes < x appear before nodes >= x preserving relative order."""
    raise NotImplementedError("Implement partition")
