class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def split_list_to_parts(head: ListNode | None, k: int) -> list[ListNode | None]:
    """Splits linked list into k consecutive balanced parts."""
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    
    width, remainder = divmod(length, k)
    
    result: list[ListNode | None] = []
    curr = head
    
    for i in range(k):
        part_head = curr
        part_size = width + (1 if i < remainder else 0)
        
        if part_size > 0:
            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
        
        result.append(part_head)
        
    return result
