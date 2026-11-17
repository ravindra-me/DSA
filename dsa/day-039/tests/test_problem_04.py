# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_04.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_04 import TreeNode, is_symmetric  # noqa: E402
# ---- End of generated header ----

class TestCheckSymmetricTree(TestCase):
    def test_example_1_symmetric(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(3)),
        )
        self.assertTrue(is_symmetric(root))

    def test_example_2_asymmetric_structure(self):
        root = TreeNode(
            1,
            TreeNode(2, None, TreeNode(3)),
            TreeNode(2, None, TreeNode(3)),
        )
        self.assertFalse(is_symmetric(root))

    def test_empty_tree(self):
        self.assertTrue(is_symmetric(None))

    def test_single_node(self):
        self.assertTrue(is_symmetric(TreeNode(42)))

    def test_negative_values_and_duplicates(self):
        root = TreeNode(
            -10,
            TreeNode(-5, TreeNode(0), TreeNode(7)),
            TreeNode(-5, TreeNode(7), TreeNode(0)),
        )
        self.assertTrue(is_symmetric(root))

        # Break symmetry by changing one leaf value
        root.right.right.val = 1
        self.assertFalse(is_symmetric(root))

    def test_asymmetric_values_same_structure(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(3), TreeNode(4)),
        )
        self.assertFalse(is_symmetric(root))

    def test_large_symmetric_and_asymmetric_tree(self):
        def build_symmetric_tree(depth: int, val: int) -> TreeNode | None:
            if depth == 0:
                return None
            node = TreeNode(val)
            node.left = build_symmetric_tree(depth - 1, val + 1)
            node.right = build_symmetric_tree(depth - 1, val + 1)
            return node

        # Perfect binary tree of depth 10 has 1023 nodes
        root = build_symmetric_tree(10, 1)
        self.assertTrue(is_symmetric(root))

        # Modify a deep leaf node on the far right
        curr = root
        while curr.right is not None:
            curr = curr.right
        curr.val = 9999
        self.assertFalse(is_symmetric(root))
