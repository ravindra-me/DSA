# Problem 1: Binary Tree Level Order Traversal

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Level Order (BFS) with layer separation | [Day 40: Tree Traversals](../README.md) |

## Problem Statement

Given the root of a binary tree, return the level order traversal of its nodes' values as a list of lists, where each inner list contains the node values at that depth from left to right.

## Input

`root: TreeNode | None` representing the root of a binary tree.

## Output

`list[list[int]]` containing the values level by level.

## Constraints

- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

## Examples

**Example 1**

```text
Input:  root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]
```

Level 0 has node 3. Level 1 has nodes 9 and 20. Level 2 has nodes 15 and 7.

**Example 2**

```text
Input:  root = None
Output: []
```

An empty tree has no levels.

## Function Signature

```python
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: TreeNode | None) -> list[list[int]]:
    """Return level order traversal of binary tree nodes level by level."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a FIFO queue (`collections.deque`). For each level, loop over `len(queue)` nodes, pop them, collect their values, and enqueue their children.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
