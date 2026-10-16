# Solution 1: Reverse a Linked List

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Basic pointer manipulation and iterative reversal

## Approach

Iterate through the linked list maintaining three pointers: `prev` (initially `None`), `curr` (initially `head`), and a temporary `next_node` to save the forward link before inverting `curr.next` to point to `prev`. At the end of the traversal, `prev` points to the new head of the reversed list.

## Thought Process

A naive or brute-force approach would be to traverse the linked list, collect all node values into an array, reverse the array, and then construct a new linked list or overwrite the node values. However, this requires $O(n)$ extra memory and does not reverse the structure in-place as demanded.

To achieve $O(1)$ auxiliary space, we must mutate the `next` pointers directly. At any node `curr`, reversing its link means setting `curr.next = prev`. But modifying `curr.next` severs the reference to the remainder of the list. Therefore, before modifying `curr.next`, we must cache `curr.next` in a temporary variable (`next_node`). We then advance `prev` to `curr` and `curr` to `next_node`. Repeating this until `curr` becomes `None` leaves `prev` referencing the last non-null node, which is the new head.

## Algorithm

1. Initialize `prev` to `None` and `curr` to `head`.
2. Loop while `curr` is not `None`.
3. Store the reference to the next node: `next_node = curr.next`.
4. Reverse the pointer: `curr.next = prev`.
5. Advance `prev` to `curr`.
6. Advance `curr` to `next_node`.
7. Return `prev` as the head of the reversed list.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the number of nodes in the linked list, because each node is visited and its pointer redirected exactly once.
- **Space:** $O(1)$ auxiliary space since only a constant number of pointer variables (`prev`, `curr`, `next_node`) are used.

## Edge Cases

- Empty list (`head is None`): The loop does not execute and returns `prev` which is `None`.
- Single node list (`head.next is None`): The loop runs once; `head.next` becomes `None`, and `head` is returned.
- List with two elements: Pointers are cleanly swapped without cycles or detached nodes.
- Negative numbers and duplicate values: Pointer reversal only manipulates node references, so node values (negatives, zeroes, duplicates) are preserved untouched.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
from typing import Optional


class ListNode:
    """Node in a singly linked list."""

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverses a singly linked list in-place and returns the new head."""
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev
```
