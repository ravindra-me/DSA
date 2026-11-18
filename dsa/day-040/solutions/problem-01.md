# Solution 1: Binary Tree Level Order Traversal

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Level Order (BFS) with layer separation

## Approach

We perform a breadth-first search (BFS) using a double-ended queue (`collections.deque`). At each step, we record the number of nodes currently in the queue, which represents the entire current level. We then pop that exact number of nodes, append their values to a level list, and push any non-null children into the queue.

## Thought Process

A level-order traversal visits all nodes at depth $d$ before any node at depth $d + 1$. This matches the behavior of Breadth-First Search (BFS).

A naive approach might run depth-first search (DFS) with a depth counter or use BFS without level tracking and later sort nodes by depth, but grouping on-the-fly during BFS is both simpler and optimal.

To distinguish between different levels during a standard queue-based BFS, we leverage the snapshot property: whenever we finish processing level $k$, the queue contains exclusively all nodes of level $k + 1$. By inspecting `len(queue)` before popping, we know exactly how many nodes belong to the upcoming level, allowing us to process them in a single batch without extra delimiter tokens.

## Algorithm

1. Check if `root` is `None`; if so, return an empty list `[]`.
2. Initialize a double-ended queue `queue` containing `root` and an empty list `levels` to hold the result.
3. While `queue` is not empty, determine `level_size = len(queue)` and initialize an empty list `current_level`.
4. Loop `level_size` times: pop the leftmost node from `queue`, append its value `node.val` to `current_level`, and push `node.left` and `node.right` into `queue` if they are not `None`.
5. Append `current_level` to `levels`.
6. Once the queue is empty, return `levels`.

## Complexity Analysis

- **Time:** O(N) where N is the number of nodes in the binary tree. Every node is enqueued and dequeued exactly once.
- **Space:** O(N) where N is the number of nodes. The queue holds at most the maximum width of the tree, which can be up to ceil(N / 2) nodes in a balanced tree.

## Edge Cases

- Empty tree (`root is None`): handled immediately at the start by returning `[]`.
- Single node tree: the queue runs for one iteration, producing `[[root.val]]`.
- Skewed tree (linked list structure): each level contains exactly one element; the queue size remains 1 throughout.
- Negative values and duplicates: node values are preserved directly without affecting queue logic.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
    """Return level order traversal of binary tree nodes level by level."""
    if root is None:
        return []

    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)
        current_level: list[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.append(current_level)

    return result
```
