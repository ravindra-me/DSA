# Problem 5: Build Binary Tree from Preorder Traversal with Null Tokens

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Iterative tree construction from serialized string using explicit state stack | [Day 32: Stack](../README.md) |

## Problem Statement

Given a comma-separated string `preorder` representing the preorder traversal of a binary tree where `#` represents a null node and numeric strings represent node integer values, reconstruct the binary tree and return its root.

You must implement an explicit stack (iterative approach) without relying on system recursion.

## Input

`preorder: str`

## Output

`TreeNode | None` (TreeNode is defined with attributes `val`, `left`, `right`).

## Constraints

- 1 <= len(preorder) <= 10^5
- `preorder` consists of integers and '#' separated by commas.

## Examples

**Example 1**

```text
Input:  preorder = "1,2,#,#,3,#,#"
Output: TreeNode(1, left=TreeNode(2), right=TreeNode(3))
```

1 is root, 2 is left child (leaf), 3 is right child (leaf).

**Example 2**

```text
Input:  preorder = "#"
Output: None
```

Empty tree represented by single null token.

## Function Signature

```python
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def deserialize_preorder(preorder: str) -> TreeNode | None:
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Process tokens sequentially. Maintain a stack of nodes whose left or right children need to be populated, along with state flags for left vs right child assignment. Target O(N) time and O(N) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
