class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


def find_cycle_entrance_value(head: ListNode | None) -> int | None:
    """Return the value of the cycle's entrance node, or None if acyclic."""
    raise NotImplementedError
