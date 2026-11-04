class Node:
    def __init__(self, val: int, prev: 'Node | None' = None, next: 'Node | None' = None, child: 'Node | None' = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head: Node | None) -> Node | None:
    """Flattens a multilevel doubly linked list in pre-order DFS depth."""
    raise NotImplementedError
