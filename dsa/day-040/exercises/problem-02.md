# Problem 2: Iterative Inorder Traversal

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Iterative DFS using an explicit stack | [Day 40: Tree Traversals](../README.md) |

## Problem Statement

Given the root of a binary tree, return the inorder traversal of its nodes' values without using recursion.

## Input

`root: TreeNode | None` representing the root of a binary tree.

## Output

`list[int]` containing the node values visited in inorder.

## Constraints

- The number of nodes in the tree is in the range [0, 2500].
- -1000 <= Node.val <= 1000
- Must be implemented iteratively using an explicit stack.

## Examples

**Example 1**

```text
Input:  root = [1, null, 2, 3]
Output: [1, 3, 2]
```

Node 1 is root with right child 2. Node 2 has left child 3. Inorder visits left, root, right: 1, 3, 2.

**Example 2**

```text
Input:  root = None
Output: []
```

Empty tree yields an empty list.

## Function Signature

```python
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal_iterative(root: TreeNode | None) -> list[int]:
    """Return inorder traversal of binary tree iteratively using a stack."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use an explicit stack. Push nodes while traversing left; when hitting `None`, pop a node, record its value, and transition to its right child.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
