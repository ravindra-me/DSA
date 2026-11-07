# Problem 5: Reverse Nodes in K-Group

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | in-place-reversal | [Day 29: Linked List Techniques](../README.md) |

## Problem Statement

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as they are.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

## Input

`head: Optional[ListNode]`, `k: int`

## Output

`Optional[ListNode]`

## Constraints

- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

## Examples

**Example 1**

```text
Input:  head = [1, 2, 3, 4, 5], k = 2
Output: [2, 1, 4, 3, 5]
```

First pair (1, 2) reversed to (2, 1); second pair (3, 4) reversed to (4, 3); last node 5 is untouched.

**Example 2**

```text
Input:  head = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]
```

First group of 3 (1, 2, 3) reversed to (3, 2, 1); remaining 2 nodes (4, 5) stay as is.

**Example 3**

```text
Input:  head = [1, 2], k = 2
Output: [2, 1]
```

Full list reversed.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverses nodes in groups of k in-place, leaving remainders untouched."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Count or probe k nodes forward to ensure a complete group exists. If so, reverse those k nodes in-place, stitch the sublist boundaries, and repeat iteratively using a dummy head.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
