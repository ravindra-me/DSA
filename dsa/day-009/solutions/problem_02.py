class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def remove_kth_from_end(head: ListNode | None, k: int) -> ListNode | None:
    """Remove the k-th node from the end and return the head of the modified list."""
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Move fast k + 1 steps ahead so the gap between fast and slow is k + 1
    for _ in range(k + 1):
        if fast is None:
            break
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast is not None:
        fast = fast.next
        slow = slow.next

    # slow.next is the node to delete
    if slow.next is not None:
        slow.next = slow.next.next

    return dummy.next
