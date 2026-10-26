# Solution 1: Pairwise Swap Linked List Nodes

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy/Medium | **Concept:** Recursive structural rewiring on singly linked lists

## Approach

We can view pairwise swapping as a recursive process on sublists: swap the first two nodes (`first` and `second`) by pointing `second.next` to `first`, and setting `first.next` to the result of recursively calling `swap_pairs` on the remainder of the list (`second.next`). The base case occurs when there are fewer than two nodes remaining.

## Thought Process

When considering linked list manipulations, recursion offers an intuitive divide-and-conquer mental model. A linked list consists of a head node and a tail linked list. To swap pairs, we need at least two nodes available: `first = head` and `second = head.next`.

If the list is empty (`head is None`) or contains only a single node (`head.next is None`), no swap can occur; we simply return `head`. Otherwise, we detach the rest of the list starting at `second.next`, recursively process that remainder, and rewire `first.next` to point to the head of the swapped remainder. Finally, `second.next` points to `first`, and `second` becomes the new head of this two-node segment.

Modifying node values instead of pointers is explicitly prohibited. The recursive approach rewires the actual `ListNode` pointers in-place without allocating new nodes.

## Algorithm

1. Check base cases: if `head is None` or `head.next is None`, return `head`.
2. Identify the two nodes to swap: let `first = head` and `second = head.next`.
3. Recursively call `swap_pairs(second.next)` to obtain the new head of the remaining list after pairwise swapping.
4. Rewire pointers: set `first.next` to the result of the recursive call.
5. Set `second.next = first` to complete the swap of the current pair.
6. Return `second`, which is the new head of the swapped sublist.

## Complexity Analysis

- **Time:** O(N) where N is the number of nodes in the linked list. Each recursive step processes exactly two nodes, making N / 2 recursive calls total.
- **Space:** O(N) call stack space in Python due to recursion depth of N / 2 frames. Given N <= 100, this requires at most 50 stack frames, well within Python's default recursion limit.

## Edge Cases

- Empty list (`head is None`): Handled immediately by the base case, returning `None`.
- Single-node list (`head.next is None`): Handled by the base case, returning `head` untouched.
- Odd number of nodes: The final unpaired node is detected by the base case (`head.next is None`) and correctly appended to the tail of the preceding swapped pair.
- Duplicate node values: Pointers are swapped rather than values, so identical values do not affect correctness.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """Recursively swap every two adjacent nodes in a linked list and return the new head."""
    if head is None or head.next is None:
        return head

    first = head
    second = head.next

    # Recurse on the remaining list and connect to first
    first.next = swap_pairs(second.next)
    # Put second before first
    second.next = first

    return second
```
