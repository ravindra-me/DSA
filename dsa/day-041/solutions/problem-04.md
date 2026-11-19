# Solution 4: Subtree Weight Parity Balance

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Recursive Tree Traversal with O(H) call stack analysis

## Approach

We perform a single post-order traversal (`left`, `right`, `node`). Each recursive step computes the subtree sum of the current node and returns it to its parent while checking if the left and right child subtree sums share the same parity (`left_sum % 2 == right_sum % 2`), incrementing a running counter whenever they match.

## Thought Process

A naive approach might compute the sum of the left and right subtrees independently for every node by calling a helper `subtree_sum(node)` function. Since finding the sum takes $O(k)$ for a subtree of size $k$, doing this for all $n$ nodes results in $O(n^2)$ time in the worst case (e.g., a degenerate linked-list tree) or $O(n \log n)$ in balanced trees.

To achieve $O(n)$ time, observe that the sum of a subtree rooted at `u` is simply `u.val + sum(u.left) + sum(u.right)`. If we visit nodes bottom-up (post-order traversal), the child sums are already computed when we visit `u`. We can determine whether `u` is parity-balanced in $O(1)$ time by comparing `(left_sum % 2) == (right_sum % 2)`. Because each node is visited once and each step takes $O(1)$ time, total time is strictly $O(n)$, and the auxiliary space is bounded by the recursion depth, which is $O(h)$.

## Algorithm

1. Initialize an integer counter `balanced_count = 0`.
2. Define a helper function `post_order(node) -> int` that returns the total sum of values in the subtree rooted at `node`.
3. Base case: If `node is None`, return 0 (an empty tree has sum 0).
4. Recursively call `left_sum = post_order(node.left)` and `right_sum = post_order(node.right)`.
5. Check if `(left_sum % 2) == (right_sum % 2)`. If true, increment `balanced_count` by 1.
6. Return `node.val + left_sum + right_sum`.
7. Call `post_order(root)` and return `balanced_count`.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the number of nodes in the tree. Each node is visited exactly once, performing $O(1)$ arithmetic and comparison operations.
- **Space:** $O(h)$ auxiliary space, where $h$ is the height of the tree, corresponding to the maximum depth of the recursive call stack ($O(\log n)$ best-case balanced tree, $O(n)$ worst-case degenerate tree).

## Edge Cases

- Empty tree (`root = None`): Handled immediately by returning 0 without traversal.
- Single node: Both left and right subtrees are empty with sum 0 (even), so the single node is parity-balanced, returning 1.
- Negative values and modulo: In Python, `-3 % 2 == 1` and `-4 % 2 == 0`, matching non-negative parity seamlessly. Even under bitwise `& 1`, parity is consistent.
- Deep/skewed trees: Call stack depth can reach $n$. For large inputs in Python, `sys.setrecursionlimit` ensures safety when tree height is large.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
import sys

sys.setrecursionlimit(200_000)


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def count_parity_balanced(root: TreeNode | None) -> int:
    """Count nodes whose left and right subtree sums have matching parity in O(n) time and O(h) space."""
    balanced_count = 0

    def get_sum(node: TreeNode | None) -> int:
        nonlocal balanced_count
        if node is None:
            return 0

        left_sum = get_sum(node.left)
        right_sum = get_sum(node.right)

        if (left_sum % 2) == (right_sum % 2):
            balanced_count += 1

        return node.val + left_sum + right_sum

    get_sum(root)
    return balanced_count
```
