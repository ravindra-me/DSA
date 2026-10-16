from typing import Optional


class ListNode:
    """Node in a singly linked list."""

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverses a singly linked list in-place."""
    raise NotImplementedError
