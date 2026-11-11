# Solution 1: Merge Two Sorted Lists

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Core merging operation of Merge Sort applied to linked structures

## Approach

Maintain a dummy head node and a current pointer to weave the two sorted lists together. At each step, compare the heads of both lists, attach the smaller node to `current.next`, and advance that list's pointer. When one list is exhausted, splice the remainder of the other list directly in $O(1)$ time.

## Thought Process

A brute-force approach could extract all values into a dynamic array, sort the array in $O((n+m) \log(n+m))$ time, and construct an entirely new linked list. However, this violates the problem constraint of splicing existing nodes without allocating new nodes, and fails to exploit the existing sorted order of both input lists.

Because both lists are already sorted in non-decreasing order, the overall smallest unplaced element is always at either `list1.val` or `list2.val`. By repeatedly picking the minimum of the two current heads, we can merge the lists in linear time $O(n + m)$. Using a dummy head node simplifies edge cases like choosing the initial head of the merged list.

## Algorithm

1. Create a dummy `ListNode(0)` to anchor the merged list, and set `current = dummy`.
2. While both `list1` and `list2` are not `None`, compare `list1.val` and `list2.val`.
3. If `list1.val <= list2.val`, set `current.next = list1` and advance `list1 = list1.next`.
4. Otherwise, set `current.next = list2` and advance `list2 = list2.next`.
5. Advance `current = current.next`.
6. Once the loop terminates, at least one list is exhausted; attach the non-empty list by setting `current.next = list1 if list1 is not None else list2`.
7. Return `dummy.next` as the head of the merged list.

## Complexity Analysis

- **Time:** O(n + m) where n and m are the number of nodes in list1 and list2 respectively. Each iteration advances one node pointer, and the remaining nodes are attached in O(1).
- **Space:** O(1) auxiliary space since the nodes are spliced in-place using only pointer reassignments and a single dummy node.

## Edge Cases

- Both lists empty: The loop is skipped, `current.next` is set to `None`, and `dummy.next` returns `None`.
- One list empty: The loop is skipped, the non-empty list is attached directly to `dummy.next`, and returned in O(1).
- Duplicate values across or within lists: The `<=` comparison ensures stable, deterministic ordering.
- Negative values: Standard integer comparison correctly orders negative numbers before zero and positive numbers.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merges two sorted linked lists into one sorted linked list in-place."""
    dummy = ListNode(0)
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 is not None else list2
    return dummy.next
```
