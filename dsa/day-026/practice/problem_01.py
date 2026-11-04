class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


def partition_list(head: ListNode | None, x: int) -> ListNode | None:
    """Partition list such that nodes < x precede nodes >= x stably."""
    raise NotImplementedError
