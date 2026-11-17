from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None


def is_symmetric(root: TreeNode | None) -> bool:
    """Determine if the binary tree is symmetric around its center."""
    if root is None:
        return True

    def is_mirror(t1: TreeNode | None, t2: TreeNode | None) -> bool:
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (
            t1.val == t2.val
            and is_mirror(t1.left, t2.right)
            and is_mirror(t1.right, t2.left)
        )

    return is_mirror(root.left, root.right)
