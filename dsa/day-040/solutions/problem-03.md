# Solution 3: Zigzag Level Order Traversal

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Level Order BFS with alternating direction

## Approach

Perform a standard breadth-first search (BFS) level by level using a queue. For each level, determine the traversal direction using a toggle flag; either append node values directly to a list or reverse them before adding them to the final result (or populate a fixed-size array in the required order).

## Thought Process

Standard level-order traversal visits nodes depth by depth from left to right using a queue (`collections.deque`). The zigzag requirement simply alters the reading order of values at alternating depths: even levels (0-indexed) are left-to-right, and odd levels are right-to-left.

A baseline approach could collect all nodes level by level into lists, then reverse every odd level. Since reversing a list of length $k$ takes $O(k)$ time and the sum of lengths is $N$, reversing odd levels takes $O(N)$ total time, which is already optimal.

Alternatively, we can use a double-ended structure (deque) for each level's values, appending to the right if left-to-right and appending to the left if right-to-left. Both achieve identical $O(N)$ time and $O(N)$ auxiliary space. Direct list reversal at odd levels is idiomatic, clean, and has very low overhead in Python.

## Algorithm

1. Check if root is None; if so, return an empty list.
2. Initialize a queue (deque) with the root node, an empty result list, and a boolean flag `left_to_right = True`.
3. While the queue is not empty, record the current level size `level_size = len(queue)`.
4. Iterate `level_size` times, popping nodes from the left of the queue, appending their values to a `current_level` list, and enqueuing their left and right children if present.
5. If `left_to_right` is False, reverse `current_level`.
6. Append `current_level` to the result list.
7. Toggle `left_to_right = not left_to_right`.
8. Return the result list when the queue is exhausted.

## Complexity Analysis

- **Time:** O(N) where N is the number of nodes in the tree. Each node is enqueued and dequeued exactly once, and each value is read or reversed once.
- **Space:** O(N) to store the result and hold up to O(W) nodes in the BFS queue, where W is the maximum width of the tree (up to N/2 for a complete binary tree).

## Edge Cases

- Empty tree (root is None): Handled immediately by returning [].
- Single node: Correctly returns [[root.val]].
- Left-skewed or right-skewed trees: Depth reaches N, alternating direction correctly for each single-node level.
- Trees with negative values and duplicates: Value types and ranges do not affect the structure or order.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
from collections import deque


class TreeNode:
    def __init__(self,
                 val: int = 0,
                 left: 'TreeNode | None' = None,
                 right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root: TreeNode | None) -> list[list[int]]:
    """Return zigzag level order traversal of nodes' values."""
    if not root:
        return []

    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level_vals: list[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            level_vals.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level_vals.reverse()

        result.append(level_vals)
        left_to_right = not left_to_right

    return result
```
