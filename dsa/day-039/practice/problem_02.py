from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None

def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """Determine if two trees are structurally identical with equal values."""
    raise NotImplementedError
