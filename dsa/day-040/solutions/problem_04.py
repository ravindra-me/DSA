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
