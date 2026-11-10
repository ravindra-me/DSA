# Solution 5: Build Binary Tree from Preorder Traversal with Null Tokens

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Iterative tree construction from serialized string using explicit state stack

## Approach

We split the string into tokens and process them sequentially using an explicit stack. Each element in the stack tracks a created `TreeNode` alongside how many of its children (left, right) have been populated so far (0, 1, or 2). When a non-null node is encountered, we attach it to the parent at the top of the stack and push the new node. When a null node (`#`) is encountered, we attach `None` to the parent at the top of the stack. Whenever a stack frame reaches 2 populated children, it is popped.

## Thought Process

Preorder traversal visits the root, then left subtree, then right subtree. With explicit null representation (`#`), any binary tree is uniquely determined. Using recursion is intuitive, but the problem explicitly requires an iterative approach with a stack to simulate the call stack.

Instead of managing indices, we can store `[node, children_count]` on the stack. For every token:
1. Create a `TreeNode` if it's numeric, or `None` if `#`.
2. If the stack is empty, this node is the tree's root.
3. If the stack is non-empty, attach this node to the node at the top of the stack as left child (if `children_count == 0`) or right child (if `children_count == 1`), then increment `children_count` for the parent.
4. If the parent now has 2 children, pop it from the stack.
5. If the current node was non-null, push `[node, 0]` onto the stack.

## Algorithm

1. Handle the edge case where `preorder` is '#' by returning `None` immediately.
2. Split `preorder` by comma into a list of string tokens.
3. Initialize an empty stack and `root = None`.
4. Iterate through each token in the tokens list.
5. If token is '#', set `curr = None`. Otherwise, set `curr = TreeNode(int(token))`.
6. If stack is empty, set `root = curr` (this occurs for the first token).
7. Else, examine the top frame `[parent, children_count]` on the stack. If `children_count == 0`, assign `parent.left = curr`. If `children_count == 1`, assign `parent.right = curr`. Increment `children_count`.
8. If the updated `children_count` equals 2, pop the top frame from the stack.
9. If `curr` is not `None`, push `[curr, 0]` onto the stack.
10. Return `root`.

## Complexity Analysis

- **Time:** O(N) where N is the number of tokens in the preorder string. Splitting takes O(N) and each token is pushed/popped from the stack at most once.
- **Space:** O(H) where H is the height of the tree for the explicit stack storage (up to O(N) in a degenerate skewed tree).

## Edge Cases

- Single null token ('#'): returns `None` immediately.
- Single leaf node ('1,#,#'): correctly constructs a single node tree.
- Deeply skewed trees (left or right heavy): explicit stack prevents Python `RecursionError`.
- Trees with negative numbers and zero: correctly parsed via `int(token)`.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def deserialize_preorder(preorder: str) -> TreeNode | None:
    """Reconstructs a binary tree from a comma-separated preorder string iteratively using a stack."""
    if not preorder or preorder == "#":
        return None
    
    tokens = preorder.split(",")
    root: TreeNode | None = None
    # Stack holds mutable lists: [node, count_of_children_filled]
    stack: list[list] = []
    
    for token in tokens:
        curr = None if token == "#" else TreeNode(int(token))
        
        if not stack:
            root = curr
        else:
            parent_frame = stack[-1]
            parent = parent_frame[0]
            if parent_frame[1] == 0:
                parent.left = curr
            else:
                parent.right = curr
            parent_frame[1] += 1
            
            if parent_frame[1] == 2:
                stack.pop()
        
        if curr is not None:
            stack.append([curr, 0])
            
    return root
```
