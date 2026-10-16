# Problem 3: Merge Two Sorted Lists

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Two-pointer list merging with dummy head | [Day 7: Linked Lists](../README.md) |

## Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list by splicing together the nodes of the first two lists. Return the head of the merged linked list.

## Input

`list1`: Optional[ListNode], head of first sorted list.
`list2`: Optional[ListNode], head of second sorted list.

## Output

Optional[ListNode], head of the merged sorted list.

## Constraints

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

## Examples

**Example 1**

```text
Input:  list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
```

Nodes are spliced in ascending order.

**Example 2**

```text
Input:  list1 = [], list2 = [0]
Output: [0]
```

One list is empty, return the other list.

## Function Signature

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merges two sorted singly linked lists into one sorted list."""
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Create a dummy sentinel node and advance a tail pointer, attaching the smaller node of list1 or list2 at each step.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
