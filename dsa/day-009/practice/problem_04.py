from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def merge_two_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted linked lists by splicing nodes in-place."""
    raise NotImplementedError
