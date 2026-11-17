from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None

def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """Determine if two trees are structurally identical with equal values."""
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
