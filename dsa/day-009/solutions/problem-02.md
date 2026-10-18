# Solution 2: Remove K-th Node From End

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Fixed-gap runner pointers and dummy head node

## Approach

Use a dummy head node and two pointers (`fast` and `slow`) separated by a fixed gap of $k$ steps. When `fast` reaches the end of the list (`None`), `slow` will point directly to the node preceding the target, enabling an $O(1)$ pointer update `slow.next = slow.next.next` in a single traversal.

## Thought Process

A naive or two-pass approach traverses the list once to count the total length $N$, and then traverses a second time to index $N - k$. While $O(N)$ in time, it requires two traversals.

To accomplish this in a single traversal with $O(1)$ extra space, we can maintain a gap of $k$ nodes between two pointers. If `fast` is advanced $k + 1$ steps ahead of `slow`, advancing both pointers synchronously until `fast` hits `None` leaves `slow` pointing exactly one node before the $k$-th node from the end.

Pre-pending a dummy node before `head` elegantly handles the edge case where the head itself must be deleted (e.g., when $k = N$), removing the need for special conditionals.

## Algorithm

1. Create a dummy node `dummy` whose `next` pointer points to `head`.
2. Initialize two pointers, `fast` and `slow`, both pointing to `dummy`.
3. Advance `fast` forward $k + 1$ times so that the distance between `fast` and `slow` is $k + 1$ nodes.
4. Advance both `fast` and `slow` one step at a time until `fast` becomes `None`.
5. Remove the target node by setting `slow.next = slow.next.next`.
6. Return `dummy.next` as the new head of the list.

## Complexity Analysis

- **Time:** $O(N)$ where $N$ is the number of nodes in the linked list. The list is traversed exactly once.
- **Space:** $O(1)$ auxiliary memory since only two pointer references and a single dummy node are allocated.

## Edge Cases

- k equals the length of the list (deleting the head node): Handled seamlessly by the dummy node, as `slow` stays on `dummy` and updates its `next` to skip the original head.
- Single-element list with k = 1: The dummy's next is set to `None`, correctly returning an empty list.
- Removing the last node (k = 1): `fast` moves to the end, `slow` ends at the second-to-last node, and sets its `next` to `None`.
- Large lists up to 10^5 elements: Linear traversal completes comfortably within 100 milliseconds without recursion depth issues.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def remove_kth_from_end(head: ListNode | None, k: int) -> ListNode | None:
    """Remove the k-th node from the end and return the head of the modified list."""
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Move fast k + 1 steps ahead so the gap between fast and slow is k + 1
    for _ in range(k + 1):
        if fast is None:
            break
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast is not None:
        fast = fast.next
        slow = slow.next

    # slow.next is the node to delete
    if slow.next is not None:
        slow.next = slow.next.next

    return dummy.next
```
