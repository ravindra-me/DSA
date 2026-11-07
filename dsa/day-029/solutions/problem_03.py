from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def _split_list(head: ListNode) -> tuple[ListNode, ListNode]:
    """Splits a list into two halves using fast and slow pointers."""
    slow: ListNode = head
    fast: Optional[ListNode] = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    return head, mid  # type: ignore[return-value]


def _merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Merges two sorted linked lists into one sorted list."""
    dummy = ListNode(0)
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
    """Sorts linked list in O(n log n) time using merge sort."""
    if head is None or head.next is None:
        return head
    left, right = _split_list(head)
    sorted_left = sort_list(left)
    sorted_right = sort_list(right)
    return _merge(sorted_left, sorted_right)
