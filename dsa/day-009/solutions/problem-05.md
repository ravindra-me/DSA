# Solution 5: Reorder and Interweave List

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Combining midpoint split, in-place reversal, and alternating merge

## Approach

We solve the problem in three linear-time steps using $O(1)$ auxiliary space: (1) find the midpoint of the linked list using slow and fast pointers to split it into two halves, (2) reverse the second half in-place, and (3) interweave the first half and the reversed second half node-by-node.

## Thought Process

A naive approach collects all node references into an array or deque, then alternates taking nodes from the front and back. While this takes $O(N)$ time, it requires $O(N)$ auxiliary memory for the array/deque references, violating the $O(1)$ space constraint.

To achieve $O(1)$ space, notice the structure of the desired output: elements from the first half are paired with elements from the second half traversed backwards ($L_0 \to L_n \to L_1 \to L_{n-1} \dots$). A singly linked list cannot be traversed backwards, but we can reverse a sublist in-place in $O(N)$ time and $O(1)$ space. Therefore, splitting the list at its midpoint, reversing the entire second half, and then splicing the two lists by alternating their links gives the desired order completely in-place.

## Algorithm

1. Handle trivial lists: if head is None or head.next is None, return head immediately.
2. Use slow and fast pointers (slow moves 1 step, fast moves 2 steps) to locate the middle of the list.
3. Sever the link between the first half and the second half by setting slow.next = None after storing the start of the second half.
4. Reverse the second half in-place using standard three-pointer pointer reversal (prev, curr, next_node).
5. Merge the two lists (first half starting at head, reversed second half starting at prev) by alternating links until the second half is exhausted.
6. Return the original head.

## Complexity Analysis

- **Time:** $O(N)$ because finding the midpoint takes $N/2$ steps, reversing the second half takes $N/2$ steps, and interweaving takes $N$ steps. Total operations are proportional to $N$.
- **Space:** $O(1)$ auxiliary space as we only reassign existing node pointers without allocating any new nodes, arrays, or recursive call stack frames.

## Edge Cases

- Empty list (`head = None`): Handled by early return, returns `None`.
- Single node (`head.next = None`): Handled by early return, returns unchanged node.
- Two nodes: First half has 1 node, second half has 1 node. Reversal leaves the single node intact, and merge keeps the order [1, 2].
- Odd vs. even length: The slow/fast pointer configuration leaves the first half equal to or one node longer than the second half, ensuring clean termination when interweaving.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def reorder_list(head: ListNode | None) -> ListNode | None:
    """Reorder the list in-place to L0 -> Ln -> L1 -> Ln-1 -> ..."""
    if head is None or head.next is None or head.next.next is None:
        return head

    # Step 1: Find the midpoint of the linked list
    slow: ListNode = head
    fast: ListNode | None = head
    while fast and fast.next and fast.next.next:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next

    # Split into two lists
    second: ListNode | None = slow.next
    slow.next = None

    # Step 2: Reverse the second half in-place
    prev: ListNode | None = None
    curr: ListNode | None = second
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Step 3: Interweave first half (head) and reversed second half (prev)
    first: ListNode | None = head
    second = prev
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

    return head
```
