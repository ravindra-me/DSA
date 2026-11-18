from collections import deque


class TreeNode:
    def __init__(self,
                 val: int = 0,
                 left: 'TreeNode | None' = None,
                 right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root: TreeNode | None) -> list[list[int]]:
    """Return zigzag level order traversal of nodes' values."""
    if not root:
        return []

    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level_vals: list[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            level_vals.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level_vals.reverse()

        result.append(level_vals)
        left_to_right = not left_to_right

    return result
