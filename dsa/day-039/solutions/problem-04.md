# Solution 4: Check Symmetric Tree

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Mirror recursion / symmetric divide and conquer

## Approach

A binary tree is symmetric if its left and right subtrees are mirror reflections of each other. We use a helper function `is_mirror(t1, t2)` that checks whether two subtrees are mirrors by verifying that their root values match, `t1.left` mirrors `t2.right`, and `t1.right` mirrors `t2.left`.

## Thought Process

When considering symmetry across a central vertical axis, a single node's left child must correspond to its mirror partner's right child, and vice versa. An empty tree or a tree with a single node is trivially symmetric.

A brute-force or alternative way is to perform an in-order traversal and check if the resulting array is a palindrome. However, in-order traversal alone does not capture structural shape without recording `None` children or structure markers, and it requires $O(N)$ extra memory for the serialized array. 

Direct mirror recursion (or an iterative queue-based approach) compares nodes pairwise from the top down. At each step:
1. If both nodes are `None`, they mirror each other.
2. If exactly one is `None` or their values differ, symmetry is violated.
3. Otherwise, recursively verify `is_mirror(t1.left, t2.right)` and `is_mirror(t1.right, t2.left)`.
This traverses each node once and short-circuits as soon as any asymmetry is detected.

## Algorithm

1. Check if root is None; if so, return True.
2. Define a recursive helper `is_mirror(t1, t2)`.
3. If both `t1` and `t2` are None, return True.
4. If either `t1` or `t2` is None (but not both), return False.
5. If `t1.val != t2.val`, return False.
6. Return `is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)`.
7. Call `is_mirror(root.left, root.right)` and return the result.

## Complexity Analysis

- **Time:** $O(N)$ where $N$ is the number of nodes in the tree, because we visit each node at most once.
- **Space:** $O(H)$ where $H$ is the height of the tree, for the call stack. In the worst case of a skewed tree, $H = O(N)$; for a balanced tree, $H = O(\log N)$.

## Edge Cases

- Empty tree (`root is None`): returns True immediately.
- Single-node tree: left and right children are both None, returning True.
- Asymmetric tree structures (one branch has a child while the mirror branch does not): detected when one node is None and the other is not.
- Identical subtree values but matching same-side instead of mirror (e.g. Example 2): detected because outer and inner pairs are cross-compared.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None


def is_symmetric(root: TreeNode | None) -> bool:
    """Determine if the binary tree is symmetric around its center."""
    if root is None:
        return True

    def is_mirror(t1: TreeNode | None, t2: TreeNode | None) -> bool:
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (
            t1.val == t2.val
            and is_mirror(t1.left, t2.right)
            and is_mirror(t1.right, t2.left)
        )

    return is_mirror(root.left, root.right)
```
