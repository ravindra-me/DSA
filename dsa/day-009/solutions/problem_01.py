class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


def find_middle_value(head: ListNode) -> int:
    """Return the value of the middle node (second middle if even)."""
    slow: ListNode | None = head
    fast: ListNode | None = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.val
