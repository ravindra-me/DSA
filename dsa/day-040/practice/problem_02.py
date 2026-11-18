class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal_iterative(root: TreeNode | None) -> list[int]:
    """Return inorder traversal of binary tree iteratively using a stack."""
    raise NotImplementedError
