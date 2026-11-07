# Solution 5: Reverse Nodes in K-Group

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** in-place-reversal

## Approach

We process the linked list group by group iteratively using a sentinel dummy node. For each potential group, we first check if at least `k` nodes remain. If fewer than `k` nodes remain, we stop and leave them untouched; otherwise, we reverse the `k` nodes in-place, reconnect the previous group's tail to the new group head, and advance our pointer to the end of the newly reversed group.

## Thought Process

A naive or out-of-place approach would collect node references or values into an array, reverse segments of length `k`, and rebuild the linked list. While $O(n)$ time and straightforward, the problem specifies modifying node links in-place without altering node values, and $O(1)$ auxiliary space is strongly preferred for linked list operations.

To achieve $O(1)$ extra space, we can count `k` steps forward from a pointer `group_prev` that sits right before the current group. If we find a `k`-th node (`kth`), we know the group is complete and can be reversed. The sublist to reverse spans from `group_prev.next` to `kth`. After reversing those `k` nodes, the old head becomes the new tail (connected to `kth.next`), and the old `kth` node becomes the new head (connected from `group_prev`). We repeat this until fewer than `k` nodes remain.

## Algorithm

1. Create a dummy node pointing to `head` and initialize `group_prev = dummy`.
2. Loop: starting from `group_prev`, advance a pointer `kth = group_prev` by `k` steps.
3. If fewer than `k` nodes are found before hitting `None`, break the loop (the remaining nodes stay as they are).
4. Record `group_next = kth.next`, `curr = group_prev.next`, and `prev = group_next`.
5. Reverse the `k` nodes by iterating from `curr` up to `group_next`: save `nxt = curr.next`, set `curr.next = prev`, update `prev = curr`, and `curr = nxt`.
6. Reconnect: save `old_group_head = group_prev.next`, set `group_prev.next = kth`, and advance `group_prev = old_group_head`.
7. Return `dummy.next`.

## Complexity Analysis

- **Time:** O(n) where n is the number of nodes in the linked list. Every node is visited twice: once during the scan to check for k nodes, and once during the pointer reversal.
- **Space:** O(1) auxiliary space as only a constant number of pointers are allocated.

## Edge Cases

- k = 1: No reversal is necessary; every group has length 1. The code handles this naturally or could early-exit.
- List length less than k: The lookahead cannot find k nodes and terminates immediately, leaving the list unmodified.
- List length is an exact multiple of k: All nodes are reversed in groups with no remainder.
- Single-element list with k = 1: Returns the single node unaltered.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverses nodes in groups of k in-place, leaving remainders untouched."""
    if not head or k <= 1:
        return head

    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        # Check if there are at least k nodes remaining
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next

        group_next = kth.next

        # Reverse k nodes: [curr ... kth]
        # We can initialize prev to group_next so the new tail directly links to group_next
        prev = group_next
        curr = group_prev.next
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Connect the previous group's tail to the new head of this reversed group
        temp = group_prev.next
        group_prev.next = kth
        group_prev = temp
```
