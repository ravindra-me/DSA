from typing import Optional


class ListNode:
    """Node in a singly linked list."""

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverses a singly linked list in-place and returns the new head."""
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev
