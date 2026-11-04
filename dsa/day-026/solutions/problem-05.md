# Solution 5: Flatten a Multilevel Doubly Linked List

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Complex pointer rewiring in hierarchical doubly linked structures

## Approach

Traverse the doubly linked list level by level. Whenever a node with a non-null `child` pointer is encountered, splice the child sublist into the main list between the current node and its original `next` node. Recursively flatten the child sublist (or use an iterative stack/pointer approach) and set the `child` pointer to `None` after splicing.

## Thought Process

The depth-first search order means child sublists take precedence over the `next` node of the parent. An intuitive way to solve this iteratively is to walk through the list starting at `head`. When a node `curr` has a `child`, we locate the end (tail) of the child sublist. We then rewire: `curr.next` becomes `curr.child`, `curr.child.prev` points to `curr`, and the child tail's `next` connects to the original `curr.next` (if it existed). We reset `curr.child = None` and continue iterating forward. Because we advance `curr` node by node (`curr = curr.next`), any nested child pointers will be processed in correct DFS sequence seamlessly.

## Algorithm

1. Initialize a pointer `curr = head`.
2. While `curr` is not None:
3. If `curr.child` exists, find the tail of the child sublist by advancing a temporary pointer `child_tail = curr.child` until `child_tail.next` is None.
4. If `curr.next` is not None, set `curr.next.prev = child_tail` and `child_tail.next = curr.next`.
5. Set `curr.next = curr.child` and `curr.child.prev = curr`.
6. Set `curr.child = None`.
7. Move `curr = curr.next`.

## Complexity Analysis

- **Time:** O(N) where N is the total number of nodes in the multilevel structure. Each node is visited at most a constant number of times during traversal and tail finding.
- **Space:** O(1) auxiliary space as the iterative pointer manipulations modify links in-place without stack or list memory overhead.

## Edge Cases

- Empty list (`head` is None): Return None directly.
- Single node with no child: Handled naturally; loop completes in one step.
- Multiple nested children (children having children): Correctly processed in pre-order as `curr` steps into the spliced child list step-by-step.
- Child at the last node of a sublist (`curr.next` is None): Handled correctly by checking `if curr.next is not None` before updating `curr.next.prev`.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
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
```
