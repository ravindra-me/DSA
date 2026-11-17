from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None


def is_symmetric(root: TreeNode | None) -> bool:
    """Determine if the binary tree is symmetric around its center."""
    raise NotImplementedError
