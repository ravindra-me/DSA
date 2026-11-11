from typing import Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Sorts a singly linked list in O(n log n) time using merge sort."""
    raise NotImplementedError
