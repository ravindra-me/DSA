from typing import Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """Partition list such that nodes < x appear before nodes >= x preserving relative order."""
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)

    less_tail = less_dummy
    greater_tail = greater_dummy

    curr = head
    while curr:
        if curr.val < x:
            less_tail.next = curr
            less_tail = less_tail.next
        else:
            greater_tail.next = curr
            greater_tail = greater_tail.next
        curr = curr.next

    greater_tail.next = None
    less_tail.next = greater_dummy.next

    return less_dummy.next
