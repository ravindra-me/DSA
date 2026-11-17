# Problem 5: Path Sum Validation and Target Matching

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Root-to-leaf recursive path tracking and backtracking accumulation | [Day 39: Binary Trees](../README.md) |

## Problem Statement

Given the root of a binary tree and an integer `target_sum`, return `True` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `target_sum`.

A **leaf** is a node with no children (`left is None` and `right is None`). A path must start at the root and terminate at a leaf (an empty tree contains no root-to-leaf paths, so it must return `False`).

## Input

`root: TreeNode | None` — the root node.
`target_sum: int` — the target sum to check.

## Output

`bool` — True if a valid root-to-leaf path sums to target_sum, False otherwise.

## Constraints

- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -10^5 <= target_sum <= 10^5

## Examples

**Example 1**

```text
Input:  root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), target_sum = 22
Output: True
```

Path 5 -> 4 -> 11 -> 2 sums to 22.

**Example 2**

```text
Input:  root = TreeNode(1, TreeNode(2)), target_sum = 1
Output: False
```

Node 1 is not a leaf because it has a child 2. The only root-to-leaf path is 1 -> 2 (sum 3).

## Function Signature

```python
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None

def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
    """Check if there is a root-to-leaf path whose node values sum to target_sum."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Subtract current node value from target_sum. If at a leaf, check if the remaining value is 0. Otherwise, recursively check left OR right subtrees. Beware of single-child nodes: they are not leaves.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
