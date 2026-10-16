# Problem 4: Remove N-th Node From End of List

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Fast and slow runner pointers with gap | [Day 7: Linked Lists](../README.md) |

## Problem Statement

Given the `head` of a singly linked list, remove the $n$-th node from the end of the list and return its head in a single pass.

## Input

`head`: Optional[ListNode], head of the linked list.
`n`: int, 1-indexed position from the end.

## Output

Optional[ListNode], head of the list after removal.

## Constraints

- The number of nodes in the list is sz, where 1 <= sz <= 30.
- 0 <= Node.val <= 100
- 1 <= n <= sz

## Examples

**Example 1**

```text
Input:  head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]
```

The 2nd node from the end is 4. Removing it leaves [1, 2, 3, 5].

**Example 2**

```text
Input:  head = [1], n = 1
Output: []
```

The only node is removed, resulting in an empty list.

## Function Signature

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Removes the nth node from the end of the list in a single pass."""
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Advance a fast pointer n steps ahead, then move slow and fast together until fast reaches the end.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
