# Problem 1: Find Middle Node Value

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Fast and slow pointers for finding midpoints | [Day 9: Linked List Techniques](../README.md) |

## Problem Statement

Given the `head` of a singly linked list, return the value of the middle node.

If the list contains an even number of nodes, return the value of the **second** middle node.

You must solve this in a single pass using $O(1)$ auxiliary space without first counting the length of the list.

## Input

`head`: The head `ListNode` of a non-empty singly linked list.

## Output

`int`: The value stored in the middle node.

## Constraints

- The list contains between 1 and 10^5 nodes.
- -10^9 <= ListNode.val <= 10^9

## Examples

**Example 1**

```text
Input:  head = [1, 2, 3, 4, 5]
Output: 3
```

The list has 5 nodes. The middle node is 3.

**Example 2**

```text
Input:  head = [1, 2, 3, 4, 5, 6]
Output: 4
```

The list has 6 nodes. The two middle nodes are 3 and 4; return the second middle node, 4.

**Example 3**

```text
Input:  head = [42]
Output: 42
```

Single-node list; the middle node is the only node.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def find_middle_value(head: ListNode) -> int:
    """Return the value of the middle node (second middle if even)."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use fast and slow pointers both starting at the head. Advance slow by 1 step and fast by 2 steps while fast and fast.next are non-null.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
