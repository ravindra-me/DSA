# Solution 1: Calculate Maximum Tree Depth

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Fundamental bottom-up tree recursion

## Approach

Use bottom-up recursion (divide and conquer) or an iterative depth-first/breadth-first traversal to compute the tree's height. The maximum depth of any subtree rooted at `node` is `1 + max(max_depth(node.left), max_depth(node.right))`, with a base case of `0` for an empty tree (`None`). An iterative post-order DFS or BFS level-order traversal also avoids Python recursion limit concerns for deep trees.

## Thought Process

The maximum depth of a binary tree is defined recursively: if a tree is empty, its depth is 0. If it is non-empty, its depth is 1 (for the root node) plus the maximum depth of its left and right subtrees.

While a direct recursive solution is concise and natural, a degenerate tree with $10^4$ nodes (a skewed linked-list-like tree) could exceed Python's default recursion limit of 1000. To ensure robust handling within Python's constraints without artificially modifying system limits, we can implement an iterative traversal (such as Breadth-First Search level-by-level using a queue, or Depth-First Search using an explicit stack). Iterative level-order traversal with `collections.deque` counts the exact number of levels, visiting each node once and naturally avoiding recursion depth limits.

## Algorithm

1. If `root` is `None`, return 0 immediately.
2. Initialize a queue `deque` containing `(root, 1)` or process level-by-level.
3. Alternatively, track levels: initialize `queue = deque([root])` and `depth = 0`.
4. While the queue is not empty, increment `depth` by 1.
5. Determine the number of nodes at the current level (`len(queue)`).
6. Pop that many nodes from the queue, appending any non-null left and right children back into the queue.
7. When the queue is empty, all levels have been traversed; return `depth`.

## Complexity Analysis

- **Time:** O(N), where N is the number of nodes in the binary tree. Every node is enqueued and dequeued exactly once.
- **Space:** O(W) = O(N), where W is the maximum width of the tree. In a complete binary tree, the queue holds at most ceil(N / 2) nodes at the bottom level.

## Edge Cases

- Empty tree (`root is None`): Handled upfront, returns 0.
- Single node tree: Returns 1 after processing the single level.
- Left-skewed or right-skewed tree (up to 10^4 nodes): Handled iteratively without hitting Python's call-stack recursion limit.
- Negative node values or duplicate values: Node values do not affect depth computation.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None


def max_depth(root: TreeNode | None) -> int:
    """Return the maximum depth (number of nodes from root to furthest leaf)."""
    if root is None:
        return 0

    queue: deque[TreeNode] = deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return depth
```
