# Problem 4: Check Symmetric Tree

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Mirror recursion / symmetric divide and conquer | [Day 39: Binary Trees](../README.md) |

## Problem Statement

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

A tree is symmetric if its left subtree is a mirror reflection of its right subtree.

## Input

`root: TreeNode | None` — the root node of the tree.

## Output

`bool` — True if the tree is symmetric, False otherwise.

## Constraints

- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

## Examples

**Example 1**

```text
Input:  root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
Output: True
```

Subtrees mirror each other across the root.

**Example 2**

```text
Input:  root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
Output: False
```

The right child of the left subtree is 3, but the right child of the right subtree is 3, which is not a reflection.

## Function Signature

```python
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None

def is_symmetric(root: TreeNode | None) -> bool:
    """Determine if the binary tree is symmetric around its center."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Define a helper function is_mirror(t1, t2). Two trees are mirrors if both roots match and t1.left is a mirror of t2.right AND t1.right is a mirror of t2.left.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
