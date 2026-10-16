# Problem 5: Reverse Nodes in k-Group

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Complex multi-pointer block reversal | [Day 7: Linked Lists](../README.md) |

## Problem Statement

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k`, then left-out nodes at the end should remain in their original order.

You may not alter the values in the list's nodes; only the nodes themselves (pointers) may be changed.

## Input

`head`: Optional[ListNode], head of the linked list.
`k`: int, the group size.

## Output

Optional[ListNode], head of the modified list.

## Constraints

- The number of nodes in the list is n, where 1 <= n <= 5000.
- 0 <= Node.val <= 1000
- 1 <= k <= n
- Must use O(1) auxiliary space (iterative).

## Examples

**Example 1**

```text
Input:  head = [1, 2, 3, 4, 5], k = 2
Output: [2, 1, 4, 3, 5]
```

Groups of 2 are reversed: [1,2] -> [2,1], [3,4] -> [4,3]. The remaining node [5] is left as-is.

**Example 2**

```text
Input:  head = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]
```

The first 3 nodes [1, 2, 3] reverse to [3, 2, 1]. The remaining 2 nodes [4, 5] are fewer than k, so they remain unchanged.

## Function Signature

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverses nodes of list k at a time in O(1) auxiliary memory."""
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Count or lookahead k nodes. If k nodes exist, reverse that sub-segment and reconnect boundary pointers; repeat iteratively with O(1) extra space.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
