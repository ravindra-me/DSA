# Solution 5: Reverse Nodes in k-Group

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Complex multi-pointer block reversal

## Approach

This problem is solved by using a 'dummy' node to simplify boundary conditions and iterating through the list while maintaining a `prev_group_end` pointer. For each group of `k` nodes, we verify if a full group exists; if so, we reverse the segment in-place and reconnect the surrounding list segments by updating the `next` pointers of the `prev_group_end` and the new tail of the reversed group.

## Thought Process

A naive approach might involve converting to an array, reversing segments, and rebuilding the list, but that consumes O(n) space. To achieve O(1) space, we must perform pointer manipulation directly on the linked list. The core challenge is 'sewing' the groups back together: the node before the group needs to point to the new head of the reversed group, and the old head of the group (now the tail) must connect to the start of the next group. By identifying the segment start and end, we can perform a standard linked-list reversal on that sub-segment and carefully link the pointers.

## Algorithm

1. Create a dummy node pointing to head to handle head-reversal cases gracefully.
2. Initialize `prev_group_end` to dummy.
3. Traverse the list to find the start and end of the current group of size k.
4. If fewer than k nodes remain, stop; the remaining nodes stay as they are.
5. Reverse the identified k-group using a standard pointer-reversal algorithm.
6. Connect `prev_group_end.next` to the new head of the reversed group.
7. Connect the tail of the newly reversed group to the next node in the original sequence.
8. Move `prev_group_end` to the end of the newly reversed group and repeat.

## Complexity Analysis

- **Time:** O(n), where n is the number of nodes. We visit each node a constant number of times (once to find the group end, once to reverse the group).
- **Space:** O(1), as we only use a few pointers regardless of list size.

## Edge Cases

- k=1: The list remains unchanged; the algorithm handles this as single-node reversals.
- List length < k: The loop identifying the group fails, the list remains unchanged.
- List length is a multiple of k: The entire list is processed into groups perfectly.
- Last group length < k: The loop identifies the tail as None or stops early, preserving the tail correctly.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
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
```
