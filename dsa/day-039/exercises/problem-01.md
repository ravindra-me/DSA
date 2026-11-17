# Problem 1: Calculate Maximum Tree Depth

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Fundamental bottom-up tree recursion | [Day 39: Binary Trees](../README.md) |

## Problem Statement

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

An empty tree has a depth of 0.

## Input

`root: TreeNode | None` — the root node of the binary tree.

## Output

`int` — the maximum depth of the tree.

## Constraints

- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000

## Examples

**Example 1**

```text
Input:  root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
Output: 3
```

Longest path is 3 -> 20 -> 15 (or 7), which has 3 nodes.

**Example 2**

```text
Input:  root = None
Output: 0
```

An empty tree has depth 0.

## Function Signature

```python
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None

def max_depth(root: TreeNode | None) -> int:
    """Return the maximum depth (number of nodes from root to furthest leaf)."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use recursion: base case returns 0 for None; otherwise return 1 plus the maximum depth of the left and right subtrees. Target O(N) time and O(H) auxiliary space.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
