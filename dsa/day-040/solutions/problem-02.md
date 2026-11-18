# Solution 2: Iterative Inorder Traversal

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Iterative DFS using an explicit stack

## Approach

Inorder traversal visits nodes in the order: Left subtree, Current node, Right subtree. To simulate recursion iteratively without call-stack overhead, we use an explicit stack. We traverse down the left spine of the tree, pushing each node onto the stack until reaching `None`. Then we pop the top node, record its value, and set the current pointer to its right child, repeating until both the pointer is `None` and the stack is empty.

## Thought Process

In a recursive inorder traversal, the runtime call stack implicitly preserves parent nodes while exploring left children. Once a left subtree is exhausted, execution resumes at the caller (parent), processes it, and proceeds to the right child.

To convert this to an iterative algorithm, we replace the call stack with an explicit Python list acting as a LIFO stack. A pointer `curr` tracks the current position. Starting from `root`, we repeatedly push `curr` and advance `curr = curr.left` until `curr` is `None`. At this point, the node at the top of the stack has no unprocessed left subtrees. We pop it, append its value to the result list, and transition `curr = popped_node.right` to process its right subtree. The loop continues as long as there is an active node (`curr is not None`) or nodes waiting on the stack (`stack` is non-empty).

## Algorithm

1. Initialize an empty list `result` and an empty list `stack`.
2. Initialize a pointer `curr = root`.
3. Loop while `curr is not None` or `stack` is non-empty.
4. While `curr is not None`, push `curr` onto `stack` and set `curr = curr.left`.
5. Pop the top node from `stack` into `node`.
6. Append `node.val` to `result`.
7. Set `curr = node.right`.
8. Return `result`.

## Complexity Analysis

- **Time:** O(N) where N is the number of nodes in the tree, because each node is pushed onto and popped from the stack exactly once.
- **Space:** O(H) where H is the height of the tree (O(N) in the worst case of a skewed tree, O(log N) for a balanced tree) to store nodes on the stack.

## Edge Cases

- Empty tree (root is None): the loop condition immediately evaluates to false, returning an empty list.
- Single node tree: the node is pushed, popped, its value recorded, right child is None, stack becomes empty, loop terminates.
- Left-skewed tree: all nodes are pushed onto the stack before any node is processed, achieving maximum stack depth of N.
- Right-skewed tree: each node is immediately pushed, popped, and its right child is explored, maintaining a stack depth of 1.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal_iterative(root: TreeNode | None) -> list[int]:
    """Return inorder traversal of binary tree iteratively using a stack."""
    result: list[int] = []
    stack: list[TreeNode] = []
    curr: TreeNode | None = root

    while curr is not None or stack:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        node = stack.pop()
        result.append(node.val)
        curr = node.right

    return result
```
