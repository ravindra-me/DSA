# Solution 3: Sort Linked List in O(n log n)

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Divide-and-conquer merge sort on singly linked lists with O(1) auxiliary node space

## Approach

Use top-down merge sort on the linked list. Split the list into two halves using the fast and slow pointer technique, recursively sort each half, and merge the two sorted halves by relinking node pointers without allocating new node objects.

## Thought Process

Sorting an array with merge sort requires $O(n)$ auxiliary space to buffer elements during the merge phase because array elements cannot be spliced in place without shifting. In contrast, linked list nodes can be spliced and rearranged in $O(1)$ auxiliary space simply by rewiring `.next` pointers.

A brute-force or naive approach might extract all values into a dynamic array, sort the array in $O(n \log n)$ time, and rebuild a linked list (or overwrite node values). However, this uses $O(n)$ extra space and violates the spirit of in-place node manipulation.

To achieve true merge sort on linked lists:
1. **Base Case**: If the list is empty (`head is None`) or has a single node (`head.next is None`), it is already sorted.
2. **Split**: Find the middle node using a slow pointer (advances 1 step) and a fast pointer (advances 2 steps). Crucially, advance `fast` one step ahead initially (`fast = head.next`) or keep track of the node before `slow` so that when splitting a 2-node list, it splits into `[node1]` and `[node2]` rather than looping indefinitely.
3. **Divide**: Disconnect the two halves by setting `prev.next = None` or `slow.next = None`.
4. **Recurse & Merge**: Recursively sort both sublists and combine them using a standard two-way merge using a dummy head.

## Algorithm

1. Check base cases: if head is None or head.next is None, return head.
2. Find the middle of the list using slow and fast pointers. Initialize slow = head and fast = head.next so that slow lands on the end of the first half.
3. Split the list into two halves: left = head, right = slow.next, and sever the link with slow.next = None.
4. Recursively call sort_list(left) and sort_list(right).
5. Merge the two sorted sublists using a dummy node and a tail pointer, iteratively appending the smaller node by updating next pointers.
6. Attach any remaining nodes from either half to the end of the merged list.
7. Return dummy.next as the head of the sorted list.

## Complexity Analysis

- **Time:** $O(n \log n)$ because the list is divided in half $\log n$ times, and each level of recursion does $O(n)$ total work finding midpoints and merging.
- **Space:** $O(\log n)$ due to the call stack depth of the divide-and-conquer recursion tree. No new list nodes are allocated.

## Edge Cases

- Empty list (`head = None`): Handled immediately by the base case returning `None`.
- Single node (`head.next = None`): Handled immediately by the base case returning `head`.
- Two nodes: Setting `fast = head.next` ensures `slow` stops at the first node, cleanly splitting the two nodes into sublists of size 1 and preventing infinite recursion.
- Already sorted or reverse sorted lists: Handled properly without extra branch penalties.
- Lists with all duplicate values or negative values: Node values are compared via `<=` preserving stability and handling negative/zero values seamlessly.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
from typing import Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def _merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Merges two sorted linked lists into one sorted linked list."""
    dummy = ListNode()
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
    """Sorts a singly linked list in O(n log n) time using merge sort."""
    if head is None or head.next is None:
        return head

    # Split list into two halves using slow and fast pointers
    slow: ListNode = head
    fast: Optional[ListNode] = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sort_list(head)
    right = sort_list(mid)

    return _merge(left, right)
```
