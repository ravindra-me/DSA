class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def reorder_list(head: ListNode | None) -> ListNode | None:
    """Reorder the list in-place to L0 -> Ln -> L1 -> Ln-1 -> ..."""
    if head is None or head.next is None or head.next.next is None:
        return head

    # Step 1: Find the midpoint of the linked list
    slow: ListNode = head
    fast: ListNode | None = head
    while fast and fast.next and fast.next.next:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next

    # Split into two lists
    second: ListNode | None = slow.next
    slow.next = None

    # Step 2: Reverse the second half in-place
    prev: ListNode | None = None
    curr: ListNode | None = second
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Step 3: Interweave first half (head) and reversed second half (prev)
    first: ListNode | None = head
    second = prev
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

    return head
