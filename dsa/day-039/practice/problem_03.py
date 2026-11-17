from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """Invert the binary tree by swapping every node's left and right subtrees."""
    raise NotImplementedError
