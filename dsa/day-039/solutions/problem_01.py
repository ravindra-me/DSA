from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: 'TreeNode | None' = None
    right: 'TreeNode | None' = None


def max_depth(root: TreeNode | None) -> int:
    """Return the maximum depth (number of nodes from root to furthest leaf)."""
    if root is None:
        return 0

    queue: deque[TreeNode] = deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return depth
