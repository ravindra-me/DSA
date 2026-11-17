# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_01 import TreeNode, max_depth  # noqa: E402
# ---- End of generated header ----

class TestMaxDepth(TestCase):
    def test_example_1(self):
        # Tree: [3, 9, 20, None, None, 15, 7]
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(max_depth(root), 3)

    def test_example_2_empty_tree(self):
        self.assertEqual(max_depth(None), 0)

    def test_single_node(self):
        root = TreeNode(42)
        self.assertEqual(max_depth(root), 1)

    def test_left_skewed_tree_with_negatives(self):
        # 0 -> -10 -> -20 -> -30
        root = TreeNode(0, TreeNode(-10, TreeNode(-20, TreeNode(-30))))
        self.assertEqual(max_depth(root), 4)

    def test_right_skewed_tree_with_duplicates(self):
        # 5 -> 5 -> 5
        root = TreeNode(5, None, TreeNode(5, None, TreeNode(5)))
        self.assertEqual(max_depth(root), 3)

    def test_symmetric_tree(self):
        # Level 1: 1
        # Level 2: 2, 2
        # Level 3: 3, 4, 4, 3
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(3))
        )
        self.assertEqual(max_depth(root), 3)

    def test_unbalanced_branches(self):
        # Left depth is 2, right depth is 5
        right_spine = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5))))
        root = TreeNode(1, TreeNode(10), right_spine)
        self.assertEqual(max_depth(root), 5)

    def test_large_skewed_tree(self):
        # Deep skewed chain of 5,000 nodes
        n = 5000
        curr = None
        for val in range(n, 0, -1):
            curr = TreeNode(val, left=curr)
        self.assertEqual(max_depth(curr), n)
