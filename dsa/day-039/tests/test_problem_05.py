# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_05.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_05 import TreeNode, has_path_sum  # noqa: E402
# ---- End of generated header ----

import unittest


class TestHasPathSum(unittest.TestCase):
    def test_example_1(self) -> None:
        root = TreeNode(
            5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
        )
        self.assertTrue(has_path_sum(root, 22))

    def test_example_2_non_leaf_sum_match(self) -> None:
        # Path 1 -> 2 has sum 3. Sum 1 would end at node 1 which is not a leaf.
        root = TreeNode(1, TreeNode(2))
        self.assertFalse(has_path_sum(root, 1))

    def test_empty_tree(self) -> None:
        self.assertFalse(has_path_sum(None, 0))
        self.assertFalse(has_path_sum(None, 10))

    def test_single_node(self) -> None:
        root = TreeNode(42)
        self.assertTrue(has_path_sum(root, 42))
        self.assertFalse(has_path_sum(root, 0))
        self.assertFalse(has_path_sum(root, -42))

    def test_negative_values(self) -> None:
        # Path: -2 -> -3 = -5
        # Path: -2 -> 5 = 3
        root = TreeNode(-2, TreeNode(-3), TreeNode(5))
        self.assertTrue(has_path_sum(root, -5))
        self.assertTrue(has_path_sum(root, 3))
        self.assertFalse(has_path_sum(root, -2))

    def test_duplicate_values_and_zeros(self) -> None:
        root = TreeNode(0, TreeNode(0, TreeNode(0)), TreeNode(0))
        # Leaves are at 0 -> 0 -> 0 (sum 0) and 0 -> 0 (sum 0)
        self.assertTrue(has_path_sum(root, 0))
        self.assertFalse(has_path_sum(root, 1))

    def test_deep_skewed_tree_no_stack_overflow(self) -> None:
        # Construct a right-skewed tree with 5000 nodes of value 1
        # Total sum from root to the single leaf is 5000
        depth = 5000
        root = TreeNode(1)
        curr = root
        for _ in range(depth - 1):
            curr.right = TreeNode(1)
            curr = curr.right

        self.assertTrue(has_path_sum(root, 5000))
        self.assertFalse(has_path_sum(root, 4999))
        self.assertFalse(has_path_sum(root, 5001))
