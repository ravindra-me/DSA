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


def vertical_traversal(root: TreeNode | None) -> list[list[int]]:
    """Return vertical order traversal of the binary tree sorted by column, row, and value."""
    raise NotImplementedError
