# Problem 2: Swap Nodes in Pairs

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | in-place-reversal | [Day 29: Linked List Techniques](../README.md) |

## Problem Statement

Given a singly linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (only pointer mutations are allowed).

If the list has an odd number of nodes, the final node remains in its position.

## Input

`head: Optional[ListNode]`

## Output

`Optional[ListNode]`

## Constraints

- The number of nodes in the list is in the range [0, 1000].
- -1000 <= Node.val <= 1000

## Examples

**Example 1**

```text
Input:  head = [1, 2, 3, 4]
Output: [2, 1, 4, 3]
```

1 and 2 swap; 3 and 4 swap.

**Example 2**

```text
Input:  head = [1, 2, 3]
Output: [2, 1, 3]
```

Node 3 remains unpaired at the end.

**Example 3**

```text
Input:  head = []
Output: []
```

Empty list yields empty list.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """Swaps adjacent nodes in pairs in-place."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a dummy node pointing to head and iterate while `curr.next` and `curr.next.next` exist. Rewire the two nodes by adjusting 3 pointers per pair.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
