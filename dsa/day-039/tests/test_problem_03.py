# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_03.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_03 import TreeNode, invert_tree  # noqa: E402
# ---- End of generated header ----

def tree_to_list(root: TreeNode | None) -> list[int | None]:
    """Helper to convert a binary tree to level-order list representation."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if curr:
            result.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


class TestInvertBinaryTree(TestCase):
    def test_example_1_full_tree(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
        inverted = invert_tree(root)
        self.assertEqual(tree_to_list(inverted), [4, 7, 2, 9, 6, 3, 1])

    def test_example_2_empty_tree(self):
        self.assertIsNone(invert_tree(None))

    def test_single_node(self):
        root = TreeNode(42)
        inverted = invert_tree(root)
        self.assertIsNotNone(inverted)
        self.assertEqual(inverted.val, 42)
        self.assertIsNone(inverted.left)
        self.assertIsNone(inverted.right)

    def test_skewed_tree_and_negatives(self):
        # Left-skewed tree with negative values
        root = TreeNode(-10, TreeNode(-20, TreeNode(-30)))
        inverted = invert_tree(root)
        # Should now be right-skewed
        self.assertEqual(inverted.val, -10)
        self.assertIsNone(inverted.left)
        self.assertIsNotNone(inverted.right)
        self.assertEqual(inverted.right.val, -20)
        self.assertIsNone(inverted.right.left)
        self.assertIsNotNone(inverted.right.right)
        self.assertEqual(inverted.right.right.val, -30)

    def test_asymmetric_with_duplicates(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2))
        inverted = invert_tree(root)
        self.assertEqual(tree_to_list(inverted), [1, 2, 2, None, None, 3])
        self.assertEqual(inverted.left.val, 2)
        self.assertIsNone(inverted.left.left)
        self.assertIsNone(inverted.left.right)
        self.assertEqual(inverted.right.val, 2)
        self.assertIsNotNone(inverted.right.left)
        self.assertEqual(inverted.right.left.val, 3)
        self.assertIsNone(inverted.right.right)

    def test_double_inversion_is_identity(self):
        root = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(15, TreeNode(12), TreeNode(20)))
        original_repr = tree_to_list(root)
        inverted = invert_tree(root)
        restored = invert_tree(inverted)
        self.assertEqual(tree_to_list(restored), original_repr)

    def test_large_complete_tree(self):
        # Build a complete binary tree with 1023 nodes (depth 10)
        nodes = [TreeNode(i) for i in range(1023)]
        for i in range(511):
            nodes[i].left = nodes[2 * i + 1]
            nodes[i].right = nodes[2 * i + 2]

        inverted = invert_tree(nodes[0])
        self.assertIs(inverted, nodes[0])
        # In inverted tree, root's left should be what used to be root's right
        self.assertEqual(inverted.left.val, 2)
        self.assertEqual(inverted.right.val, 1)
        # Check subtrees
        self.assertEqual(inverted.left.left.val, 6)
        self.assertEqual(inverted.left.right.val, 5)
        self.assertEqual(inverted.right.left.val, 4)
        self.assertEqual(inverted.right.right.val, 3)
