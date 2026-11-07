# Solution 2: Swap Nodes in Pairs

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Medium | **Concept:** in-place-reversal

## Approach

Use a dummy head node pointing to the input list to handle changes at the head cleanly. Maintain a pointer `prev` (initially pointing to the dummy node), identify the pair of nodes to swap (`first` and `second`), and adjust three pointers per iteration: `prev.next = second`, `first.next = second.next`, and `second.next = first`. Then advance `prev` past the swapped pair.

## Thought Process

A naive approach might swap node values directly instead of rewiring pointers, but the problem explicitly forbids value modifications. To swap nodes via pointers, the predecessor of each pair must be updated to point to the new first node of that pair. Using a dummy node avoids treating the head as a special case. At each step, if fewer than two nodes remain, iteration terminates immediately, leaving an odd trailing node in place. This achieves in-place swapping with strictly $O(1)$ auxiliary space and a single pass.

## Algorithm

1. Create a dummy node `dummy = ListNode(0, head)` and set `prev = dummy`.
2. Loop while `prev.next` and `prev.next.next` both exist.
3. Assign `first = prev.next` and `second = prev.next.next`.
4. Rewire pointers: `prev.next = second`, `first.next = second.next`, and `second.next = first`.
5. Advance `prev` to `first`.
6. Return `dummy.next`.

## Complexity Analysis

- **Time:** O(N) where N is the number of nodes in the linked list, visiting each node a constant number of times.
- **Space:** O(1) auxiliary space as all rewiring is performed in-place with a few pointers.

## Edge Cases

- Empty list (head is None): loop condition fails immediately and returns None.
- Single node: loop condition fails immediately and returns the single node unmodified.
- Odd number of nodes: the final odd node has no second partner, terminating the loop and keeping its position intact.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """Swaps adjacent nodes in pairs in-place."""
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next is not None and prev.next.next is not None:
        first = prev.next
        second = prev.next.next

        # Rewire pointers to swap first and second
        prev.next = second
        first.next = second.next
        second.next = first

        # Move prev to the end of the swapped pair
        prev = first

    return dummy.next
```
