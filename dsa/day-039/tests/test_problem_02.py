# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_02.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_02 import TreeNode, is_same_tree  # noqa: E402
# ---- End of generated header ----

import random

class TestSameTree(TestCase):
    def test_example_1_identical_trees(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(is_same_tree(p, q))

    def test_example_2_structural_mismatch(self):
        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        self.assertFalse(is_same_tree(p, q))

    def test_both_empty(self):
        self.assertTrue(is_same_tree(None, None))

    def test_one_empty_one_non_empty(self):
        p = TreeNode(1)
        self.assertFalse(is_same_tree(p, None))
        self.assertFalse(is_same_tree(None, p))

    def test_single_node_equal_and_unequal(self):
        self.assertTrue(is_same_tree(TreeNode(42), TreeNode(42)))
        self.assertFalse(is_same_tree(TreeNode(42), TreeNode(-42)))

    def test_negative_values_and_zeros(self):
        p = TreeNode(0, TreeNode(-10), TreeNode(10))
        q = TreeNode(0, TreeNode(-10), TreeNode(10))
        self.assertTrue(is_same_tree(p, q))

        q_diff = TreeNode(0, TreeNode(-10), TreeNode(11))
        self.assertFalse(is_same_tree(p, q_diff))

    def test_duplicate_values_different_structure(self):
        # p: 1 -> left: 1
        p = TreeNode(1, TreeNode(1), None)
        # q: 1 -> right: 1
        q = TreeNode(1, None, TreeNode(1))
        self.assertFalse(is_same_tree(p, q))

    def test_large_identical_and_differing_trees(self):
        def build_deterministic_tree(depth: int, seed: int) -> TreeNode | None:
            if depth == 0:
                return None
            val = (seed * 37 + depth) % 20000 - 10000
            return TreeNode(
                val=val,
                left=build_deterministic_tree(depth - 1, seed * 2 + 1),
                right=build_deterministic_tree(depth - 1, seed * 2 + 2)
            )

        # Complete binary tree of depth 8 has 255 nodes, well within constraints
        tree_a = build_deterministic_tree(8, 42)
        tree_b = build_deterministic_tree(8, 42)
        self.assertTrue(is_same_tree(tree_a, tree_b))

        # Modify a single deep leaf node
        curr = tree_b
        while curr.left is not None:
            curr = curr.left
        curr.val += 1
        self.assertFalse(is_same_tree(tree_a, tree_b))
