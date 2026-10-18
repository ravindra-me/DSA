# Solution 4: Merge Two Sorted Linked Lists

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Sentinel node pointer splicing for sorted list combination

## Approach

Use a dummy (sentinel) head node and a traversal pointer `tail`. Repeatedly compare the current node values of `list1` and `list2`, attaching the smaller node to `tail.next` and advancing that list's pointer. When one list is exhausted, attach the entirety of the remaining list in $O(1)$ operations.

## Thought Process

A naive approach might extract all values into an array, sort them, and reconstruct a new linked list. However, that consumes $O(N + M)$ extra memory, violating the $O(1)$ auxiliary space constraint. 

Since both input lists are already sorted, we can use a two-pointer merge strategy identical to the merge step in MergeSort. When manipulating linked lists, special cases often arise around setting the initial head pointer (determining whether `list1` or `list2` has the smallest first element). We can eliminate these branch conditions using a sentinel (dummy) node. A `tail` pointer tracks the end of the newly spliced list. At each step, we splice the smaller node to `tail.next` and advance. Crucially, once either list is exhausted, we do not need to iterate through the rest of the remaining list: because linked lists are pointer-linked chains, we can splice the entire remaining segment with a single pointer assignment (`tail.next = list1 if list1 else list2`).

## Algorithm

1. Create a sentinel node `dummy = ListNode(0)` and initialize a pointer `tail = dummy`.
2. While both `list1` and `list2` are not `None`:
3. Compare `list1.val` and `list2.val`.
4. If `list1.val <= list2.val`, set `tail.next = list1` and advance `list1 = list1.next`.
5. Otherwise, set `tail.next = list2` and advance `list2 = list2.next`.
6. Advance `tail = tail.next`.
7. Attach whichever list is non-empty directly to `tail.next` (`tail.next = list1 if list1 is not None else list2`).
8. Return `dummy.next`, which points to the true head of the merged sorted list.

## Complexity Analysis

- **Time:** $O(n + m)$ where $n$ and $m$ are the lengths of `list1` and `list2`. Each step advances at least one pointer and executes in $O(1)$ time, performing at most $n + m$ iterations.
- **Space:** $O(1)$ auxiliary space. Only a single dummy node and pointer references are allocated; existing nodes are rearranged in-place.

## Edge Cases

- Both lists are empty: loop does not run, both remain `None`, returning `dummy.next` which is `None`.
- One list is empty while the other is not: the while loop terminates immediately, and the non-empty list is attached directly.
- Lists of unequal lengths: once the shorter list is exhausted, the rest of the longer list is spliced in $O(1)$ time.
- Duplicate elements: values that are equal are preserved in non-decreasing order (stable merge).
- Negative values and values spanning $[-10^9, 10^9]$: standard comparison `<` handles positive, negative, and zero values correctly.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def merge_two_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted linked lists by splicing nodes in-place."""
    dummy = ListNode(0)
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2
    return dummy.next
```
