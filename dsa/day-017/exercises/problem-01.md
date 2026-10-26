# Problem 1: Pairwise Swap Linked List Nodes

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Recursive structural rewiring on singly linked lists | [Day 17: Recursion](../README.md) |

## Problem Statement

Given the `head` of a singly-linked list, swap every two adjacent nodes and return its new head. You must solve the problem without modifying the values in the list's nodes; only the node connections themselves may be changed.

Implement this purely using recursion where each recursive call processes a pair and links its result to the remainder of the swapped list.

## Input

`head`: The head node of a singly-linked list of type `ListNode | None`.

## Output

Return the head node of the modified linked list after pairwise swapping.

## Constraints

- The number of nodes in the list is in the range [0, 100].
- 0 <= Node.val <= 100
- Must be solved recursively.

## Examples

**Example 1**

```text
Input:  head = [1, 2, 3, 4]
Output: [2, 1, 4, 3]
```

Pairs (1, 2) and (3, 4) are swapped.

**Example 2**

```text
Input:  head = []
Output: []
```

An empty list has no pairs to swap.

**Example 3**

```text
Input:  head = [1]
Output: [1]
```

A single node cannot be paired, so it remains unchanged.

## Function Signature

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Identify the base cases (head is None or head.next is None). In the recursive step, preserve pointers to the first and second nodes, recurse on `second.next`, and rewire the pair.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
