class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def add_two_numbers_ii(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """Adds two numbers represented by linked lists with MSB first."""
    s1: list[int] = []
    s2: list[int] = []
    
    curr1 = l1
    while curr1:
        s1.append(curr1.val)
        curr1 = curr1.next
        
    curr2 = l2
    while curr2:
        s2.append(curr2.val)
        curr2 = curr2.next
        
    carry = 0
    head: ListNode | None = None
    
    while s1 or s2 or carry:
        val1 = s1.pop() if s1 else 0
        val2 = s2.pop() if s2 else 0
        
        total = val1 + val2 + carry
        digit = total % 10
        carry = total // 10
        
        new_node = ListNode(digit, head)
        head = new_node
        
    return head
