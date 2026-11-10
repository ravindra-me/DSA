class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

def deserialize_preorder(preorder: str) -> TreeNode | None:
    """Reconstructs a binary tree from a comma-separated preorder string iteratively using a stack."""
    raise NotImplementedError
