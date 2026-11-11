from typing import Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def _merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Merges two sorted linked lists into one sorted linked list."""
    dummy = ListNode()
    tail = dummy

    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 is not None else l2
    return dummy.next


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Sorts a singly linked list in O(n log n) time using merge sort."""
    if head is None or head.next is None:
        return head

    # Split list into two halves using slow and fast pointers
    slow: ListNode = head
    fast: Optional[ListNode] = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sort_list(head)
    right = sort_list(mid)

    return _merge(left, right)
