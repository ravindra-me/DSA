from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """Recursively swap every two adjacent nodes in a linked list and return the new head."""
    if head is None or head.next is None:
        return head

    first = head
    second = head.next

    # Recurse on the remaining list and connect to first
    first.next = swap_pairs(second.next)
    # Put second before first
    second.next = first

    return second
