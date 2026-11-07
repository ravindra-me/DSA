# Solution 3: Sort Linked List in O(n log n)

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium/Hard | **Concept:** fast-slow-pointers

## Approach

We implement top-down Merge Sort on the linked list. We split the list into two halves using the fast and slow pointer technique, recursively sort both halves, and then merge the two sorted halves using standard two-pointer merging.

## Thought Process

Sorting an array in $O(n \log n)$ time can be done with algorithms like Quicksort, Heapsort, or Mergesort. For singly linked lists, Mergesort is particularly well-suited because merging two sorted linked lists requires only $O(1)$ auxiliary space (just rearranging pointers) compared to $O(n)$ auxiliary space required for arrays.

A naive approach would be to extract all node values into an array, sort the array in $O(n \log n)$ time, and rewrite or rebuild the linked list. While this achieves $O(n \log n)$ time, it requires $O(n)$ extra memory to store node references or values, violating strict $O(1)$ auxiliary space (excluding recursion stack).

To perform Merge Sort directly on the linked list:
1. Base case: lists with 0 or 1 node are already sorted.
2. Divide: Find the midpoint of the linked list using the fast-slow pointer pattern. We advance `fast` twice as fast as `slow`. By starting `fast = head.next` and `slow = head`, when `fast` reaches the end, `slow` points to the end of the first half. Severing the link (`slow.next = None`) splits the list into two independent halves without allocating new nodes.
3. Conquer: Recursively sort each half.
4. Combine: Merge the two sorted halves using a dummy head and pointer splicing.

## Algorithm

1. Check base cases: if `head` is None or `head.next` is None, return `head`.
2. Find the middle node using fast and slow pointers: initialize `slow = head` and `fast = head.next`. Advance `fast` by two steps and `slow` by one step until `fast` or `fast.next` is None.
3. Split the list into two halves: let `mid = slow.next`, then set `slow.next = None`.
4. Recursively call `sort_list` on `head` (left half) and `mid` (right half).
5. Merge the two sorted halves using a dummy node: compare values at the heads of both lists, append the smaller node to the merged list, and advance the corresponding pointer.
6. Attach any remaining nodes from either half to the end of the merged list.
7. Return `dummy.next` as the new head of the sorted list.

## Complexity Analysis

- **Time:** $O(n \log n)$ where $n$ is the number of nodes in the linked list. Finding the midpoint and merging take linear time $O(n)$ at each of the $\log n$ levels of the recursion tree.
- **Space:** $O(\log n)$ auxiliary space due to the call stack of the recursive divide-and-conquer strategy. No new list nodes are allocated; existing nodes are simply rewired.

## Edge Cases

- Empty list (`head is None`): returns None immediately.
- Single-node list (`head.next is None`): returns `head` immediately.
- Two-node list: `slow` stops at the first node, splitting into two single-node lists cleanly without an infinite loop.
- List with all duplicate values: stable comparisons maintain correct order and terminate properly.
- Large lists (up to 50,000 nodes): recursion depth is at most $\lceil \log_2(50000) \rceil \approx 16$, well within standard Python recursion limits.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def _split_list(head: ListNode) -> tuple[ListNode, ListNode]:
    """Splits a list into two halves using fast and slow pointers."""
    slow: ListNode = head
    fast: Optional[ListNode] = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    return head, mid  # type: ignore[return-value]


def _merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Merges two sorted linked lists into one sorted list."""
    dummy = ListNode(0)
    tail = dummy
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 is not None else l2
    return dummy.next


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Sorts linked list in O(n log n) time using merge sort."""
    if head is None or head.next is None:
        return head
    left, right = _split_list(head)
    sorted_left = sort_list(left)
    sorted_right = sort_list(right)
    return _merge(sorted_left, sorted_right)
```
