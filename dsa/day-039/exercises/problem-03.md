# Problem 3: Invert Binary Tree

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | In-place structural transformation via recursive swap | [Day 39: Binary Trees](../README.md) |

## Problem Statement

Given the root of a binary tree, invert the tree, and return its root.

Inverting a binary tree means that for every node, its left and right children are swapped.

## Input

`root: TreeNode | None` — the root node of the binary tree.

## Output

`TreeNode | None` — the root of the inverted tree.

## Constraints

- The number of nodes in the tree is in the range [0, 1000].
- -1000 <= Node.val <= 1000

## Examples

**Example 1**

```text
Input:  root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
Output: TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))
```

Every node's left and right children are swapped.

**Example 2**

```text
Input:  root = None
Output: None
```

An empty tree inverted is still None.

## Function Signature

```python
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None

def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """Invert the binary tree by swapping every node's left and right subtrees."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Perform post-order or pre-order recursive swapping: swap left and right references of the current node, then recursively invert both subtrees.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
