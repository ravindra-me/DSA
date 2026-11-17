# Solution 3: Invert Binary Tree

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** In-place structural transformation via recursive swap

## Approach

Invert the binary tree by recursively swapping the left and right child pointers of each node. The base case is reached when encountering an empty subtree (`None`), which simply returns `None`.

## Thought Process

A binary tree is inverted if and only if for every node, its left and right subtrees are swapped, and both subtrees are themselves recursively inverted.

Because this operation has an optimal substructure (inverting the whole tree requires inverting subtrees first or swapping and then inverting subtrees), a post-order or pre-order traversal naturally fits the problem. At each node, we swap `node.left` and `node.right`, and recursively process both children. Since every node must be visited at least once, $O(n)$ time is optimal.

## Algorithm

1. Check the base case: if `root is None`, return `None`.
2. Swap `root.left` and `root.right`.
3. Recursively call `invert_tree(root.left)` and `invert_tree(root.right)`.
4. Return `root`.

## Complexity Analysis

- **Time:** O(n) where n is the number of nodes in the tree, because each node is visited and its child references are swapped exactly once.
- **Space:** O(h) where h is the height of the tree, representing the recursion stack depth. In the worst case (skewed tree), h = n, taking O(n) space; in a balanced tree, h = O(log n).

## Edge Cases

- Empty tree (root is None): handled immediately by the base case, returning None.
- Single node tree (no children): swapping two None references preserves the node unchanged and returns correctly.
- Asymmetric / skewed tree: works identically as a balanced tree, properly swapping None with an existing subtree.
- Duplicate or negative values: node values do not affect pointer swaps, handled seamlessly.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """Invert the binary tree by swapping every node's left and right subtrees."""
    if root is None:
        return None

    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```
