# Solution 3: Reverse Sub-List Between Positions

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium/Hard | **Concept:** In-place partial list reversal with local pointer reconnection

## Approach

Use a dummy head node to simplify edge cases where `left = 1`. Traverse to node `left - 1`, then iteratively reverse `right - left` links in-place by moving the node immediately following the sublist tail to the front of the sublist.

## Thought Process

A straightforward baseline converts the linked list to an array, reverses the slice between `left - 1` and `right - 1`, and updates the list node values. While $O(N)$ time, it uses $O(N)$ extra space. To achieve $O(1)$ auxiliary space, we perform in-place pointer manipulation. Using a dummy node avoids special branching when `left` is the very first node. We reach `left - 1` with a `prev` pointer. Then, for each step in the range `right - left`, we remove `curr.next` from its current spot and insert it right after `prev`.

## Algorithm

1. Create a `dummy` node pointing to `head` and initialize `prev = dummy`.
2. Advance `prev` `left - 1` times so it sits right before the sublist to reverse.
3. Set `curr = prev.next`, which is the first node of the sublist.
4. Perform `right - left` iterations: set `nxt = curr.next`, re-link `curr.next = nxt.next`, re-link `nxt.next = prev.next`, and set `prev.next = nxt`.
5. Return `dummy.next`.

## Complexity Analysis

- **Time:** O(N) single-pass traversal up to position `right`.
- **Space:** O(1) auxiliary space as pointers are updated in-place without allocating new nodes or recursion stacks.

## Edge Cases

- `left == right`: Loop runs 0 times; list remains unchanged.
- `left == 1`: Dummy node handles reversing from the absolute head cleanly without a separate `head` update standard standard condition.
- `right == n`: Reverses through to the very end of the list; final node becomes sublist head successfully.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None:
    """Reverses linked list nodes between left and right positions in-place."""
    if not head or left == right:
        return head

    dummy = ListNode(0, head)
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next
    for _ in range(right - left):
        nxt = curr.next
        curr.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt

    return dummy.next
```
