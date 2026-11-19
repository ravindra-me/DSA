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
    raise NotImplementedError
