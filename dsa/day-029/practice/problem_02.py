from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """Swaps adjacent nodes in pairs in-place."""
    raise NotImplementedError
