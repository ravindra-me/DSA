# Solution 4: Remove N-th Node From End of List

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Fast and slow runner pointers with gap

## Approach

We use a two-pointer technique with a 'dummy' head node to simplify edge cases. By creating a gap of size $n$ between two pointers (fast and slow), we can identify the node immediately preceding the target node in a single pass. When the fast pointer reaches the end, the slow pointer will be positioned just before the node to be removed.

## Thought Process

A naive approach would be to calculate the list length first, then traverse again to remove the node. While this is $O(L)$ where $L$ is length, it requires two passes. To do it in one pass, we use a 'sliding window' of pointers. By advancing one pointer $n$ steps ahead, we establish a distance equal to the offset from the end. Advancing both pointers until the leading one hits the end guarantees the trailing pointer is at the node before the removal target. The 'dummy' node is crucial to handle removing the head node itself, as the logic 'remove the node after the current one' needs a predecessor.

## Algorithm

1. 1. Initialize a dummy node with value 0, setting its next pointer to the given head.
2. 2. Create two pointers, fast and slow, both starting at the dummy node.
3. 3. Advance the fast pointer $n + 1$ steps forward.
4. 4. If the fast pointer becomes None prematurely, the list size was smaller than $n$ (though constraints prevent this here, it's good practice).
5. 5. Advance both fast and slow pointers one step at a time until fast is None.
6. 6. At this point, slow.next is the node to remove. Update slow.next to slow.next.next.
7. 7. Return dummy.next as the new head of the list.

## Complexity Analysis

- **Time:** O(L), where L is the number of nodes in the linked list. We traverse the list exactly once.
- **Space:** O(1), as we only use a constant amount of extra space for the pointers, regardless of list size.

## Edge Cases

- Removing the first node: Handled by the dummy node, which ensures we always have a 'previous' node even for the head.
- Removing the only node: Fast pointer advances beyond the list, the loop condition holds, and the dummy correctly updates to point to None.
- Removing the last node: Logic correctly identifies the node before the last one as the target and skips the last node.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
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
```
