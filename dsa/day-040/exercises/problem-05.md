# Problem 5: Vertical Order Traversal of a Binary Tree

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Coordinate-based BFS / DFS with multi-key sorting | [Day 40: Tree Traversals](../README.md) |

## Problem Statement

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position `(row, col)`, its left child will be at `(row + 1, col - 1)` and its right child will be at `(row + 1, col + 1)`. The root is at `(0, 0)`.

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values in ascending order.

## Input

`root: TreeNode | None` representing the root of the tree.

## Output

`list[list[int]]` containing the vertical order traversal grouped by column from leftmost to rightmost.

## Constraints

- The number of nodes in the tree is in the range [0, 1000].
- 0 <= Node.val <= 1000

## Examples

**Example 1**

```text
Input:  root = [3, 9, 20, null, null, 15, 7]
Output: [[9], [3, 15], [20], [7]]
```

Column -1: [9]
Column 0: [3, 15] (3 at row 0, 15 at row 2)
Column 1: [20]
Column 2: [7]

**Example 2**

```text
Input:  root = [1, 2, 3, 4, 6, 5, 7]
Output: [[4], [2], [1, 5, 6], [3], [7]]
```

Nodes 5 and 6 are both at row 2, column 0. Since 5 < 6, 5 comes before 6.

## Function Signature

```python
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def vertical_traversal(root: TreeNode | None) -> list[list[int]]:
    """Return vertical order traversal of the binary tree sorted by column, row, and value."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Traverse the tree (using BFS or DFS) while recording `(col, row, val)` for each node. Group nodes by `col`, sort within each column primarily by `row` ascending and secondarily by `val` ascending.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
