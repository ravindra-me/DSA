class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


def insertion_sort_list(head: ListNode | None) -> ListNode | None:
    """Sorts a singly-linked list using insertion sort."""
    if head is None or head.next is None:
        return head

    dummy = ListNode(0, head)
    last_sorted = head
    curr = head.next

    while curr is not None:
        if last_sorted.val <= curr.val:
            last_sorted = curr
        else:
            prev = dummy
            while prev.next is not None and prev.next.val <= curr.val:
                prev = prev.next

            last_sorted.next = curr.next
            curr.next = prev.next
            prev.next = curr

        curr = last_sorted.next

    return dummy.next
