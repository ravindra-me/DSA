from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverses nodes in groups of k in-place, leaving remainders untouched."""
    raise NotImplementedError
