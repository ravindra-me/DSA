# Problem 2: Same Tree Verification

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Dual-node recursive traversal and structural identity | [Day 39: Binary Trees](../README.md) |

## Problem Statement

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

## Input

`p: TreeNode | None`, `q: TreeNode | None` — roots of the two binary trees.

## Output

`bool` — True if trees are structurally and value-wise identical, False otherwise.

## Constraints

- The number of nodes in both trees is in the range [0, 500].
- -10^4 <= Node.val <= 10^4

## Examples

**Example 1**

```text
Input:  p = TreeNode(1, TreeNode(2), TreeNode(3)), q = TreeNode(1, TreeNode(2), TreeNode(3))
Output: True
```

Both trees have the same structure and values.

**Example 2**

```text
Input:  p = TreeNode(1, TreeNode(2)), q = TreeNode(1, None, TreeNode(2))
Output: False
```

Structurally different: in p, 2 is a left child; in q, 2 is a right child.

## Function Signature

```python
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None

def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """Determine if two trees are structurally identical with equal values."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Recurse simultaneously on both nodes: if both are None, return True; if only one is None or values differ, return False; otherwise check that left subtrees match AND right subtrees match.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
