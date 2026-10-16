# Solution 3: Merge Two Sorted Lists

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Two-pointer list merging with dummy head

## Approach

We maintain a 'dummy' node to simplify list construction. Using two pointers, we compare the current nodes of `list1` and `list2`, attaching the smaller node to our merged list's tail, and advancing the respective pointer until one list is exhausted. Finally, we attach the remainder of the non-empty list.

## Thought Process

A brute-force approach would involve collecting all node values into an array, sorting them, and rebuilding the list, which requires O(N+M) extra space and O((N+M) log(N+M)) time. The two-pointer approach is more efficient because it leverages the existing sorting. Since we only traverse each list once, we achieve linear time complexity without requiring extra space for data structures, as we simply rewire the existing `next` pointers.

## Algorithm

1. 1. Initialize a dummy ListNode and a 'tail' pointer pointing to it.
2. 2. While both list1 and list2 are not None, compare list1.val and list2.val.
3. 3. Set tail.next to the node with the smaller value and advance the pointer for that list.
4. 4. Advance the tail pointer.
5. 5. Once one list is exhausted, point tail.next to the remaining portion of the other list.
6. 6. Return dummy.next as the head of the merged list.

## Complexity Analysis

- **Time:** O(N + M), where N and M are the lengths of the two lists, as we traverse each node exactly once.
- **Space:** O(1), as we only use a constant amount of extra space for pointers, modifying the list in-place.

## Edge Cases

- Empty lists: If both are empty, the dummy.next remains None, which is correct.
- Single empty list: If one list is empty, the loop terminates immediately, and the remaining list is attached correctly.
- Duplicate values: The comparison logic handles duplicates by picking from either list (stable sort order isn't required here, but the code handles it naturally).

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    tail.next = list1 if list1 else list2
    return dummy.next
```
