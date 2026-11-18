# Problem 4: Iterative Postorder Traversal

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Iterative Postorder with two-pointer tracking or two-stack approach | [Day 40: Tree Traversals](../README.md) |

## Problem Statement

Given the root of a binary tree, return the postorder traversal of its nodes' values without using recursion.

Notice that postorder is Left -> Right -> Root. Iteratively processing this requires careful tracking to ensure both left and right subtrees have been fully explored before visiting the root.

## Input

`root: TreeNode | None` representing the root of a binary tree.

## Output

`list[int]` containing the postorder sequence.

## Constraints

- The number of nodes in the tree is in the range [0, 2500].
- -1000 <= Node.val <= 1000
- Must be iterative (no recursive helper functions).

## Examples

**Example 1**

```text
Input:  root = [1, null, 2, 3]
Output: [3, 2, 1]
```

Left of 1 is None. Right subtree of 1 has root 2 and left child 3. Subtree 2 yields [3, 2]. Then root 1 yields [3, 2, 1].

**Example 2**

```text
Input:  root = None
Output: []
```

Empty tree produces empty traversal.

## Function Signature

```python
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal_iterative(root: TreeNode | None) -> list[int]:
    """Return postorder traversal of binary tree iteratively."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Can use a single stack tracking the last visited node, or produce a modified preorder (Root -> Right -> Left) and reverse the final result.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
