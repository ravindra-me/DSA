class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


def partition_list(head: ListNode | None, x: int) -> ListNode | None:
    """Partition list such that nodes < x precede nodes >= x stably."""
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)
    
    less = less_dummy
    greater = greater_dummy
    curr = head
    
    while curr is not None:
        if curr.val < x:
            less.next = curr
            less = less.next
        else:
            greater.next = curr
            greater = greater.next
        curr = curr.next
    
    greater.next = None
    less.next = greater_dummy.next
    
    return less_dummy.next
