# Solution 1: Partition List Around Pivot

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy/Medium | **Concept:** pointer-partitioning

## Approach

Maintain two separate linked lists using dummy head nodes: one for nodes strictly less than `x` (`less_dummy`) and one for nodes greater than or equal to `x` (`greater_dummy`). Iterate through the original list, appending each node to the appropriate sublist, and finally splice the two sublists together while ensuring the tail's `next` pointer is set to `None` to prevent cycles.

## Thought Process

A brute-force array-based approach would collect all node values or references into a dynamic array, partition them using a stable sort or two-pass filter, and reconstruct a new linked list. While this works in $O(n)$ time, it incurs extra space and requires creating new nodes or overwriting node values.

Since linked list nodes can be rearranged in-place by re-pointing their `.next` pointers, we can achieve true $O(1)$ auxiliary space and $O(n)$ time. To preserve the relative order of nodes within each partition (stability), we can maintain two separate chains: one for elements $< x$ and one for elements $\ge x$. Using dummy (sentinel) heads for both chains simplifies pointer manipulation because we avoid null checks when inserting the very first node into either chain. Once we process all nodes, we terminate the 'greater-or-equal' chain with `None` (preventing an accidental cycle) and connect the tail of the 'less' chain to the head of the 'greater-or-equal' chain.

## Algorithm

1. Create two dummy nodes: `less_dummy` and `greater_dummy`.
2. Initialize two pointers, `less_tail = less_dummy` and `greater_tail = greater_dummy`.
3. Traverse the input list with a pointer `curr` starting from `head`.
4. For each node `curr`, if `curr.val < x`, attach it to `less_tail.next` and advance `less_tail`; otherwise, attach it to `greater_tail.next` and advance `greater_tail`.
5. Advance `curr = curr.next` at each iteration.
6. Set `greater_tail.next = None` to ensure the list is properly terminated without creating cycles.
7. Connect the two partitions by setting `less_tail.next = greater_dummy.next`.
8. Return `less_dummy.next` as the new head of the partitioned list.

## Complexity Analysis

- **Time:** O(n), where n is the number of nodes in the linked list. We traverse each node exactly once.
- **Space:** O(1) auxiliary space. We rearrange the existing list nodes by altering their next pointers in-place without allocating new list nodes.

## Edge Cases

- Empty list (`head is None`): Handled cleanly because the traversal loop does not execute; `less_tail.next` becomes `None` and `less_dummy.next` returns `None`.
- Single node: The single node goes into one of the two sublists and is rejoined properly without cycles.
- All nodes are less than `x`: `greater_dummy.next` remains `None`, so `less_tail.next` connects to `None`, preserving all elements.
- All nodes are greater than or equal to `x`: `less_dummy.next` connects directly to `greater_dummy.next`, returning the original order.
- Duplicate values and negative values: Handled naturally by standard comparison operators `<` and `>=`.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
from typing import Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """Partition list such that nodes < x appear before nodes >= x preserving relative order."""
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)

    less_tail = less_dummy
    greater_tail = greater_dummy

    curr = head
    while curr:
        if curr.val < x:
            less_tail.next = curr
            less_tail = less_tail.next
        else:
            greater_tail.next = curr
            greater_tail = greater_tail.next
        curr = curr.next

    greater_tail.next = None
    less_tail.next = greater_dummy.next

    return less_dummy.next
```
