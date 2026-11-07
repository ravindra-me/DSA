from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverses nodes in groups of k in-place, leaving remainders untouched."""
    if not head or k <= 1:
        return head

    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        # Check if there are at least k nodes remaining
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next

        group_next = kth.next

        # Reverse k nodes: [curr ... kth]
        # We can initialize prev to group_next so the new tail directly links to group_next
        prev = group_next
        curr = group_prev.next
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Connect the previous group's tail to the new head of this reversed group
        temp = group_prev.next
        group_prev.next = kth
        group_prev = temp
