from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverses nodes of list k at a time in O(1) auxiliary memory."""
    raise NotImplementedError
