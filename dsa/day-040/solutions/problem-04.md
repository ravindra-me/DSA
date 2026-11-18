# Solution 4: Iterative Postorder Traversal

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Iterative Postorder with two-pointer tracking or two-stack approach

## Approach

We can traverse postorder using a single explicit stack along with a `last_visited` pointer. We descend as far left as possible, pushing nodes onto the stack. At each step, we inspect the stack's top node: if it has a right child that hasn't been visited yet, we transition to that right subtree; otherwise, we pop the node, record its value, and mark it as `last_visited`.

## Thought Process

In a postorder traversal (Left -> Right -> Root), a node can only be processed after both its left and right subtrees have been completely traversed.

A recursive approach naturally maintains this state using the call stack. To simulate this iteratively without recursion:
1. A two-stack approach exists where we simulate Root -> Right -> Left (reverse postorder) and push to a second stack, which is then popped. While simple, it requires $O(N)$ extra storage for the second collection.
2. The one-stack with a `last_visited` tracking pointer approach faithfully mirrors the recursive call stack: we descend left until reaching `None`. Then we peek at the top of the stack. If the node has a right child and that right child was not the node we just visited, we move our current pointer to that right child. If the right child is `None` or was already visited, both subtrees are done: we can safely pop the node, append its value, and set `last_visited = popped_node`.

This ensures every edge and node is visited a constant number of times with $O(H)$ auxiliary space.

## Algorithm

1. Initialize an empty list `result`, an empty list `stack`, `curr = root`, and `last_visited = None`.
2. While `curr` is not None or `stack` is not empty:
3. If `curr` is not None, push `curr` onto `stack` and set `curr = curr.left` (descend left).
4. If `curr` is None, peek at `peek_node = stack[-1]`.
5. If `peek_node.right` exists and `peek_node.right != last_visited`, set `curr = peek_node.right` to explore the right subtree.
6. Otherwise, pop `peek_node` from `stack`, append `peek_node.val` to `result`, update `last_visited = peek_node`, and keep `curr = None` (to continue processing the parent in the next iteration).

## Complexity Analysis

- **Time:** O(N) where N is the number of nodes in the binary tree. Each node is pushed onto the stack once and popped once.
- **Space:** O(H) where H is the height of the binary tree (O(log N) for balanced trees, O(N) in the worst case for skewed trees), representing the maximum stack depth.

## Edge Cases

- Empty tree (root is None): the outer while loop does not execute and an empty list is immediately returned.
- Single node tree: the node is pushed, curr becomes None, peek checks no right child, pops node, and terminates.
- Left-skewed tree: descends all the way to the leaf, popping back up in reverse order as right children are None.
- Right-skewed tree: descends right step-by-step, popping nodes in postorder without infinite loops due to `last_visited` checks.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal_iterative(root: TreeNode | None) -> list[int]:
    """Return postorder traversal of binary tree iteratively."""
    result: list[int] = []
    stack: list[TreeNode] = []
    curr = root
    last_visited: TreeNode | None = None

    while curr is not None or stack:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        else:
            peek_node = stack[-1]
            if peek_node.right is not None and last_visited != peek_node.right:
                curr = peek_node.right
            else:
                stack.pop()
                result.append(peek_node.val)
                last_visited = peek_node

    return result
```
