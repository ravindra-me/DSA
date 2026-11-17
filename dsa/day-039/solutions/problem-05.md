# Solution 5: Path Sum Validation and Target Matching

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Root-to-leaf recursive path tracking and backtracking accumulation

## Approach

Traverse the binary tree using depth-first search (DFS). At each node, subtract the current node's value from the remaining target sum. When reaching a leaf node (`left is None` and `right is None`), check if the remaining target sum equals 0. Recursively propagate `True` if either child subtree contains a valid path.

## Thought Process

A valid path must start strictly at the root and terminate at a leaf (a node with no children). An empty tree has no nodes and therefore no root-to-leaf paths, so it should return `False`.

A straightforward approach is to maintain a running sum or subtract the current node's value from `target_sum`. If we are at a leaf node and `target_sum - root.val == 0`, we have found a valid path.

Notice that if a node has only one child (for instance, only a left child), we cannot conclude path validity at this node even if `target_sum - root.val == 0`, because it is not a leaf node. The search must continue down the existing child branch. To handle deep trees (up to 5000 nodes in skewed trees), we can implement the traversal either iteratively with an explicit stack to avoid recursion depth limits or recursively while ensuring Python's recursion limit is accommodated. An iterative DFS with an explicit stack storing `(node, remaining_sum)` is clean, robust, and avoids stack overflow entirely.

## Algorithm

1. If `root` is `None`, return `False` immediately.
2. Initialize an explicit stack containing the tuple `(root, target_sum - root.val)`.
3. While the stack is not empty, pop `(node, current_rem)`.
4. If `node` is a leaf (`node.left is None and node.right is None`) and `current_rem == 0`, return `True`.
5. If `node.right` exists, push `(node.right, current_rem - node.right.val)` onto the stack.
6. If `node.left` exists, push `(node.left, current_rem - node.left.val)` onto the stack.
7. If the stack becomes empty without finding a matching leaf, return `False`.

## Complexity Analysis

- **Time:** O(N) where N is the number of nodes in the tree, because each node is visited at most once.
- **Space:** O(H) where H is the height of the tree (O(N) in the worst case for a skewed tree, O(log N) for a balanced tree) to store nodes on the traversal stack.

## Edge Cases

- Empty tree (`root is None`): returns `False` as required by definition.
- Single node tree: checks if `root.val == target_sum` because the single root node is also a leaf.
- Tree with single-child parents: paths must continue to leaves; a match at an intermediate non-leaf node does not return `True`.
- Negative node values and negative target sum: subtraction correctly tracks negative values and signs.
- Deep linear/skewed tree (up to 5000 nodes): explicit stack prevents Python `RecursionError`.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None


def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
    """Check if there is a root-to-leaf path whose node values sum to target_sum."""
    if root is None:
        return False

    # Iterative DFS using an explicit stack storing (node, remaining_sum)
    stack: list[tuple[TreeNode, int]] = [(root, target_sum - root.val)]

    while stack:
        node, remaining = stack.pop()

        # Check if current node is a leaf
        if node.left is None and node.right is None:
            if remaining == 0:
                return True
            continue

        if node.right is not None:
            stack.append((node.right, remaining - node.right.val))
        if node.left is not None:
            stack.append((node.left, remaining - node.left.val))

    return False
```
