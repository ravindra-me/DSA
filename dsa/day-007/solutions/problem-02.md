# Solution 2: Remove Elements by Value

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Dummy head pattern for deletion

## Approach

To handle deleting nodes from a singly linked list—especially when the target node might be the `head`—we place a dummy sentinel node before `head`. We traverse the list with a `curr` pointer initialized to the dummy node. If `curr.next` has the value `val`, we bypass it by setting `curr.next = curr.next.next`. Otherwise, we advance `curr = curr.next`.

## Thought Process

Without a dummy node, removing the head node requires special branch logic to update `head`. If the list consists entirely of target values (e.g., `[7, 7, 7]`), the head keeps changing until the list is empty. By prepending a dummy node whose `next` pointer initially points to `head`, the head node becomes just another node preceded by a valid `curr` pointer. Thus, a single simple loop handles deletion uniformly at any position in $O(N)$ time and $O(1)$ auxiliary space.

## Algorithm

1. Create a sentinel node `dummy = ListNode(0, head)`.
2. Initialize a pointer `curr = dummy`.
3. While `curr.next` is not None:
4. If `curr.next.val == val`, re-link `curr.next = curr.next.next` (do not advance `curr`).
5. Else, advance `curr = curr.next`.
6. Return `dummy.next` as the new head of the list.

## Complexity Analysis

- **Time:** $O(N)$, where $N$ is the number of nodes in the linked list. We traverse each node in the list exactly once.
- **Space:** $O(1)$ auxiliary space. We only allocate a single dummy node and pointer variables.

## Edge Cases

- Empty list (`head is None`): loop does not run, returns `dummy.next` which is `None`.
- All nodes equal to `val`: every node is spliced out, returning `None`.
- No nodes equal to `val`: list remains unchanged.
- Single node list: handled seamlessly whether it matches `val` or not.
- Consecutive matching nodes (e.g., `[1, 2, 2, 1]`): by not advancing `curr` when a deletion occurs, consecutive target values are cleanly removed.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """Removes all nodes with Node.val == val using a dummy sentinel."""
    dummy = ListNode(0, head)
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next
```
