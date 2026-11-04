class Node:
    def __init__(self, val: int, prev: 'Node | None' = None, next: 'Node | None' = None, child: 'Node | None' = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head: Node | None) -> Node | None:
    """Flattens a multilevel doubly linked list in pre-order DFS depth."""
    curr = head
    while curr:
        if curr.child:
            # Save the next node
            next_node = curr.next
            
            # Find the tail of the child list
            child_tail = curr.child
            while child_tail.next:
                child_tail = child_tail.next
            
            # Connect child tail with next_node
            child_tail.next = next_node
            if next_node:
                next_node.prev = child_tail
            
            # Connect curr with child
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
            
        curr = curr.next
        
    return head
