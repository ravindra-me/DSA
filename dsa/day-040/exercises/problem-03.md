# Problem 3: Zigzag Level Order Traversal

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Level Order BFS with alternating direction | [Day 40: Tree Traversals](../README.md) |

## Problem Statement

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

## Input

`root: TreeNode | None` representing the root of a binary tree.

## Output

`list[list[int]]` representing values at each depth alternating left-to-right and right-to-left.

## Constraints

- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

## Examples

**Example 1**

```text
Input:  root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [20, 9], [15, 7]]
```

Level 0: [3] (left to right)
Level 1: [20, 9] (right to left)
Level 2: [15, 7] (left to right)

**Example 2**

```text
Input:  root = [1]
Output: [[1]]
```

Single node tree has only one level.

## Function Signature

```python
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root: TreeNode | None) -> list[list[int]]:
    """Return zigzag level order traversal of nodes' values."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Perform standard BFS level-order traversal, keeping track of depth or a boolean flag. Reverse the list for odd-indexed levels (or prepend using a deque).

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
