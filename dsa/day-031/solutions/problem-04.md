# Solution 4: Insertion Sort on Linked List

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Insertion sort adaptation on linked data structures and pointer manipulation

## Approach

We build a sorted list by iteratively taking nodes from the original list and inserting each one into its correct position within the sorted segment. A dummy head node simplifies insertions at the very beginning of the sorted list, and keeping a pointer to the last sorted node avoids re-scanning when the current element is already in sorted order.

## Thought Process

In an array, insertion sort shifts elements to the right to make room for the current item. In a singly-linked list, shifting is not required; instead, we only need to rewire pointer references to insert a node. However, singly-linked lists do not support backward traversal. Therefore, to insert a node, we must search forward from the beginning of the sorted portion to find the insertion point (the node just before where the new node belongs).

If we start scanning from the dummy head for every single node, nearly-sorted or already-sorted lists still take $O(n^2)$ time. We can optimize this by maintaining a pointer `last_sorted` to the tail of the currently sorted prefix. If `last_sorted.val <= curr.val`, `curr` is already in the right place, so we simply advance `last_sorted`. Only when `curr.val < last_sorted.val` do we search from the dummy head. This preserves $O(n)$ best-case time for sorted lists while keeping $O(1)$ extra memory.

## Algorithm

1. Handle the base case: if `head` is `None` or `head.next` is `None`, return `head`.
2. Initialize a `dummy` node whose `.next` points to `head`.
3. Set `last_sorted = head` and `curr = head.next`.
4. While `curr` is not `None`:
5. If `last_sorted.val <= curr.val`, advance `last_sorted = curr`.
6. Else: find the predecessor node `prev` starting from `dummy` such that `prev.next.val > curr.val`.
7. Splice `curr` out of its current position by setting `last_sorted.next = curr.next`.
8. Splice `curr` into its new position by setting `curr.next = prev.next` and `prev.next = curr`.
9. Advance `curr` to `last_sorted.next`.
10. Return `dummy.next`.

## Complexity Analysis

- **Time:** O(n^2) worst and average case, where n is the number of nodes in the list. O(n) best case when the list is already sorted or nearly sorted, because the inner search from dummy is skipped when `last_sorted.val <= curr.val`.
- **Space:** O(1) auxiliary space as all pointer manipulations are done in-place without allocating new nodes or auxiliary containers.

## Edge Cases

- Empty list (`head is None`): returned immediately without modification.
- Single node list (`head.next is None`): returned immediately without modification.
- Already sorted list: runs in linear O(n) time by advancing `last_sorted` without searching from dummy.
- Reverse sorted list: inserts each element at the very beginning of the sorted list.
- Duplicate elements: `<` vs `<=` maintains stable ordering of duplicate values.
- Negative numbers and zero: standard integer comparison works seamlessly.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


def insertion_sort_list(head: ListNode | None) -> ListNode | None:
    """Sorts a singly-linked list using insertion sort."""
    if head is None or head.next is None:
        return head

    dummy = ListNode(0, head)
    last_sorted = head
    curr = head.next

    while curr is not None:
        if last_sorted.val <= curr.val:
            last_sorted = curr
        else:
            prev = dummy
            while prev.next is not None and prev.next.val <= curr.val:
                prev = prev.next

            last_sorted.next = curr.next
            curr.next = prev.next
            prev.next = curr

        curr = last_sorted.next

    return dummy.next
```
