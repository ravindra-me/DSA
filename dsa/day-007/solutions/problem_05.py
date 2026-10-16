from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or k == 1:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    curr = head

    def get_list_length(node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    remaining_len = get_list_length(head)

    while remaining_len >= k:
        group_start = prev_group_end.next
        curr = group_start
        
        # Reverse k nodes
        prev = None
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Connect reversed group
        next_group_start = curr
        prev_group_end.next = prev
        group_start.next = next_group_start
        
        # Prepare for next iteration
        prev_group_end = group_start
        remaining_len -= k

    return dummy.next
