import sys

sys.setrecursionlimit(200_000)


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


def count_parity_balanced(root: TreeNode | None) -> int:
    """Count nodes whose left and right subtree sums have matching parity in O(n) time and O(h) space."""
    balanced_count = 0

    def get_sum(node: TreeNode | None) -> int:
        nonlocal balanced_count
        if node is None:
            return 0

        left_sum = get_sum(node.left)
        right_sum = get_sum(node.right)

        if (left_sum % 2) == (right_sum % 2):
            balanced_count += 1

        return node.val + left_sum + right_sum

    get_sum(root)
    return balanced_count
