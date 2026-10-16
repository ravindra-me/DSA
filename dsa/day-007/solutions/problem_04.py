from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Dummy node handles edge cases where head is removed
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy
    
    # Create a gap of n between fast and slow
    for _ in range(n + 1):
        fast = fast.next
        
    # Advance both until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next
        
    # Slow is now just before the target node
    slow.next = slow.next.next
    
    return dummy.next
