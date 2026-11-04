# Problem 5: Flatten a Multilevel Doubly Linked List

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Complex pointer rewiring in hierarchical doubly linked structures | [Day 26: Linked Lists](../README.md) |

## Problem Statement

You are given a doubly linked list where nodes have a `next`, `prev`, and an additional `child` pointer. A child pointer may or may not point to a separate doubly linked list, which may also have children. Flatten the list so that all nodes appear in a single-level doubly linked list. Nodes should be flattened in depth-first search order.

## Input

head: Optional[Node]

## Output

Optional[Node]

## Constraints

- The number of Nodes will not exceed 1000.
- 1 <= Node.val <= 10^5

## Examples

**Example 1**

```text
Input:  1 <-> 2 <-> 3 <-> 4, where 3 has child 7 <-> 8
Output: 1 <-> 2 <-> 3 <-> 7 <-> 8 <-> 4
```

Child sublist 7-8 is inserted directly between 3 and 4.

**Example 2**

```text
Input:  1 <-> 2 with 1 having child 3
Output: 1 <-> 3 <-> 2
```

Child 3 is inserted right after 1.

## Function Signature

```python
class Node:
    def __init__(self, val: int, prev: 'Node | None' = None, next: 'Node | None' = None, child: 'Node | None' = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head: Node | None) -> Node | None:
    """Flattens a multilevel doubly linked list in pre-order DFS depth."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Traverse the list. When a child pointer is encountered, use DFS (or an explicit stack) to flatten the child segment, rewire pointers `prev`, `next`, and clear `child = None`. Achieve O(n) time and O(n) or O(1) auxiliary space.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
