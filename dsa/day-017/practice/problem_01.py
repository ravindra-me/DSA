from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """Recursively swap every two adjacent nodes in a linked list and return the new head."""
    raise NotImplementedError
