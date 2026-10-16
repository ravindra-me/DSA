# Problem 2: Remove Elements by Value

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Dummy head pattern for deletion | [Day 7: Linked Lists](../README.md) |

## Problem Statement

Given the `head` of a singly linked list and an integer `val`, remove all nodes of the linked list that have `Node.val == val`, and return the new head.

## Input

`head`: Optional[ListNode], the head of the linked list.
`val`: int, the value to remove.

## Output

Optional[ListNode], the head of the modified list.

## Constraints

- The number of nodes in the list is in the range [0, 10^4].
- 1 <= Node.val <= 50
- 0 <= val <= 50

## Examples

**Example 1**

```text
Input:  head = [1, 2, 6, 3, 4, 5, 6], val = 6
Output: [1, 2, 3, 4, 5]
```

All nodes containing value 6 are spliced out.

**Example 2**

```text
Input:  head = [7, 7, 7, 7], val = 7
Output: []
```

Every node matches val, returning an empty list.

## Function Signature

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """Removes all nodes with Node.val == val using a dummy sentinel."""
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a dummy head pointing to head. Iterate with a pointer examining `curr.next`, bypassing matching nodes.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
