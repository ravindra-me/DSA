from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None


def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
    """Check if there is a root-to-leaf path whose node values sum to target_sum."""
    if root is None:
        return False

    # Iterative DFS using an explicit stack storing (node, remaining_sum)
    stack: list[tuple[TreeNode, int]] = [(root, target_sum - root.val)]

    while stack:
        node, remaining = stack.pop()

        # Check if current node is a leaf
        if node.left is None and node.right is None:
            if remaining == 0:
                return True
            continue

        if node.right is not None:
            stack.append((node.right, remaining - node.right.val))
        if node.left is not None:
            stack.append((node.left, remaining - node.left.val))

    return False
