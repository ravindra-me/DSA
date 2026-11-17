from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None


def max_depth(root: TreeNode | None) -> int:
    """Return the maximum depth (number of nodes from root to furthest leaf)."""
    raise NotImplementedError
