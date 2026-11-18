from collections import deque
from itertools import groupby


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def vertical_traversal(root: TreeNode | None) -> list[list[int]]:
    """Return vertical order traversal of the binary tree sorted by column, row, and value."""
    if not root:
        return []

    nodes: list[tuple[int, int, int]] = []
    queue: deque[tuple[TreeNode, int, int]] = deque([(root, 0, 0)])

    while queue:
        node, row, col = queue.popleft()
        nodes.append((col, row, node.val))
        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    nodes.sort()

    result: list[list[int]] = []
    for _, group in groupby(nodes, key=lambda item: item[0]):
        result.append([val for _, _, val in group])

    return result
