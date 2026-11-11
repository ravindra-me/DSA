# Problem 1: Merge Two Sorted Lists

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Core merging operation of Merge Sort applied to linked structures | [Day 33: Merge Sort](../README.md) |

## Problem Statement

Given the heads of two sorted linked lists `list1` and `list2`, merge them into one sorted linked list by splicing together the nodes of the original lists without allocating new `ListNode` instances (except for an optional dummy head). Return the head of the merged linked list.

## Input

`list1: Optional[ListNode]`, `list2: Optional[ListNode]` representing the heads of two non-decreasing sorted singly linked lists.

## Output

`Optional[ListNode]` representing the head of the combined non-decreasing sorted list.

## Constraints

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both `list1` and `list2` are sorted in non-decreasing order.

## Examples

**Example 1**

```text
Input:  list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
```

Pointers weave nodes in ascending order while preserving equal elements.

**Example 2**

```text
Input:  list1 = [], list2 = []
Output: []
```

Merging two empty lists results in an empty list.

**Example 3**

```text
Input:  list1 = [], list2 = [0]
Output: [0]
```

If one list is empty, return the other list.

## Function Signature

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merges two sorted linked lists into one sorted linked list in-place."""
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a dummy head node and a tail pointer. Compare current nodes of both lists using two pointers, attaching the smaller node to tail, advancing that pointer. Attach the remainder at the end.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
