# Solution 2: Same Tree Verification

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Dual-node recursive traversal and structural identity

## Approach

We simultaneously traverse both binary trees recursively. At each step, if both current nodes are `None`, the subtrees match; if exactly one is `None` or their values differ, they do not match. Otherwise, we recursively verify both the left subtrees and the right subtrees.

## Thought Process

Two binary trees are identical if and only if their roots are equal and their corresponding subtrees are identical. This naturally forms a dual-tree recursive formulation.

An alternative approach would be to serialize both trees (e.g., preorder traversal including null markers) and compare the resulting lists/strings. However, serialization requires allocating extra memory proportional to the number of nodes and processes the entire tree even if a mismatch is found at the very root.

By comparing nodes in lockstep via simultaneous depth-first search, we can short-circuit immediately upon detecting any mismatch without requiring extra heap allocation for serialization.

## Algorithm

1. Base case 1: If both `p` and `q` are `None`, return `True` (both branches ended identically).
2. Base case 2: If either `p` is `None` or `q` is `None` (but not both), return `False` (structural mismatch).
3. Value check: If `p.val != q.val`, return `False` (value mismatch).
4. Recursive step: Return `is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)`.

## Complexity Analysis

- **Time:** O(min(N, M)) where N and M are the number of nodes in trees `p` and `q`. In the worst case (when trees are identical), we visit every node once. When trees differ, the traversal terminates at the first discrepancy.
- **Space:** O(H) where H is the height of the smaller tree, representing the recursion stack depth. In the worst case of a skewed tree, this is O(min(N, M)); in a balanced tree, O(log(min(N, M))).

## Edge Cases

- Both trees are empty (`p = None, q = None`): Handled by base case 1, returns `True`.
- One tree is empty and the other is not: Handled by base case 2, returns `False`.
- Structurally identical trees with mismatched values: Handled by the node value comparison.
- Same node values but swapped child orientations (e.g., left vs right child): Handled since left and right branches are verified separately.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None

def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """Determine if two trees are structurally identical with equal values."""
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
```
