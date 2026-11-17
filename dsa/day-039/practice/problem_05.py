from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None


def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
    """Check if there is a root-to-leaf path whose node values sum to target_sum."""
    raise NotImplementedError
