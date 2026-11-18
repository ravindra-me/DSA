class TreeNode:
    def __init__(self,
                 val: int = 0,
                 left: 'TreeNode | None' = None,
                 right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root: TreeNode | None) -> list[list[int]]:
    """Return zigzag level order traversal of nodes' values."""
    raise NotImplementedError
