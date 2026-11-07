from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """Swaps adjacent nodes in pairs in-place."""
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next is not None and prev.next.next is not None:
        first = prev.next
        second = prev.next.next

        # Rewire pointers to swap first and second
        prev.next = second
        first.next = second.next
        second.next = first

        # Move prev to the end of the swapped pair
        prev = first

    return dummy.next
