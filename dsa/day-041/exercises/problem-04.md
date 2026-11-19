# Problem 4: Subtree Weight Parity Balance

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Recursive Tree Traversal with O(H) call stack analysis | [Day 41: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

Given the root of a binary tree where each node contains an integer `val`, we say a node is *parity-balanced* if the sum of all node values in its left subtree and the sum of all node values in its right subtree have the same parity (both even or both odd). An empty subtree has sum 0 (which is even).

Return the count of all parity-balanced nodes in the tree. The solution must execute in $O(n)$ time and $O(h)$ auxiliary space, where $h$ is the tree height.

## Input

The `root` of a binary tree (or `None`).

## Output

An integer representing the count of parity-balanced nodes.

## Constraints

- The number of nodes in the tree is in the range [0, 10^5].
- -10^9 <= Node.val <= 10^9

## Examples

**Example 1**

```text
Input:  root = TreeNode(1, TreeNode(2), TreeNode(4))
Output: 3
```

Node 2: left sum = 0, right sum = 0 (both even -> balanced). Node 4: left sum = 0, right sum = 0 (both even -> balanced). Node 1: left sum = 2 (even), right sum = 4 (even) -> balanced. Total = 3.

**Example 2**

```text
Input:  root = None
Output: 0
```

An empty tree has 0 nodes.

## Function Signature

```python
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def count_parity_balanced(root: TreeNode | None) -> int:
    """Count nodes whose left and right subtree sums have matching parity in O(n) time and O(h) space."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Perform a bottom-up post-order DFS that returns the subtree sum while accumulating the count of balanced nodes.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
