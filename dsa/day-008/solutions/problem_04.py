class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None) -> None:
        self.val = val
        self.next = next


def partition_list(head: ListNode | None, x: int) -> ListNode | None:
    """Partition a linked list around pivot x preserving relative order in O(N) time and O(1) space."""
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)
    less_tail = less_dummy
    greater_tail = greater_dummy

    curr = head
    while curr is not None:
        if curr.val < x:
            less_tail.next = curr
            less_tail = curr
        else:
            greater_tail.next = curr
            greater_tail = curr
        curr = curr.next

    greater_tail.next = None
    less_tail.next = greater_dummy.next
    return less_dummy.next
