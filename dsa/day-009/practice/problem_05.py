class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def reorder_list(head: ListNode | None) -> ListNode | None:
    """Reorder the list in-place to L0 -> Ln -> L1 -> Ln-1 -> ..."""
    raise NotImplementedError
