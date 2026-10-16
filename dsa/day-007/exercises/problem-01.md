# Problem 1: Reverse a Linked List

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Basic pointer manipulation and iterative reversal | [Day 7: Linked Lists](../README.md) |

## Problem Statement

Given the `head` of a singly linked list, reverse the list in-place and return the new head node.

## Input

`head`: Optional[ListNode], the head node of a singly linked list.

## Output

Optional[ListNode], the head of the reversed list.

## Constraints

- The number of nodes in the list is in the range [0, 5000].
- -5000 <= Node.val <= 5000
- Must be solved in O(n) time and O(1) auxiliary space.

## Examples

**Example 1**

```text
Input:  head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

Pointers are inverted between each adjacent pair.

**Example 2**

```text
Input:  head = []
Output: []
```

An empty list reversed remains an empty list.

## Function Signature

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverses a singly linked list in-place."""
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain `prev`, `curr`, and `nxt` pointers to reverse arrows iteratively in a single traversal.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
