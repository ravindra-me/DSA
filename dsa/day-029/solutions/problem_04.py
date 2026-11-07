from typing import Optional
import heapq


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """Merges k sorted linked lists into one sorted linked list."""
    heap: list[tuple[int, int, ListNode]] = []
    counter = 0

    for node in lists:
        if node is not None:
            heapq.heappush(heap, (node.val, counter, node))
            counter += 1

    dummy = ListNode(0)
    tail = dummy

    while heap:
        _, _, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next

        if node.next is not None:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1

    tail.next = None
    return dummy.next
