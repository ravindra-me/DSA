class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


def find_cycle_entrance_value(head: ListNode | None) -> int | None:
    """Return the value of the cycle's entrance node, or None if acyclic."""
    if head is None or head.next is None:
        return None

    slow: ListNode | None = head
    fast: ListNode | None = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None

    slow = head
    while slow is not fast:
        assert slow is not None and fast is not None
        slow = slow.next
        fast = fast.next

    return slow.val
