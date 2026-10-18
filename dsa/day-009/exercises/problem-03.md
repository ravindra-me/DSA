# Problem 3: Find Cycle Entrance Value

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Floyd's Tortoise and Hare cycle detection and entrance resolution | [Day 9: Linked List Techniques](../README.md) |

## Problem Statement

Given the `head` of a singly linked list, determine if the list has a cycle. If a cycle is present, return the integer value stored at the node where the cycle begins. If there is no cycle, return `None`.

You may not modify the linked list. Your solution must use $O(1)$ auxiliary space.

## Input

`head`: The head `ListNode` of a singly linked list, which may or may not contain a cycle.

## Output

`int | None`: The value of the cycle start node, or `None` if no cycle exists.

## Constraints

- The number of nodes in the list is between 0 and 10^5.
- -10^9 <= ListNode.val <= 10^9
- ListNode values in the list are distinct across cycle entry points.

## Examples

**Example 1**

```text
Input:  head = [3, 2, 0, -4] where -4 links back to node with value 2
Output: 2
```

The tail connects to node index 1 (val = 2), so 2 is the entrance to the cycle.

**Example 2**

```text
Input:  head = [1, 2] where 2 links back to 1
Output: 1
```

The tail connects back to the head node (val = 1).

**Example 3**

```text
Input:  head = [1], with no cycle
Output: None
```

There is no cycle in the list.

## Function Signature

```python
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next

def find_cycle_entrance_value(head: ListNode | None) -> int | None:
    """Return the value of the cycle's entrance node, or None if acyclic."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Detect intersection using fast and slow pointers. Once collided, reset one pointer to head and advance both by 1 step until they meet at the cycle entry.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
