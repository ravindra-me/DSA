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
from problem_01 import TreeNode, level_order  # noqa: E402
# ---- End of generated header ----

from collections import deque


class TestLevelOrder(TestCase):
    def test_empty_tree(self):
        self.assertEqual(level_order(None), [])

    def test_single_node(self):
        root = TreeNode(42)
        self.assertEqual(level_order(root), [[42]])

    def test_example_one(self):
        # [3, 9, 20, null, null, 15, 7]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20, TreeNode(15), TreeNode(7))
        expected = [[3], [9, 20], [15, 7]]
        self.assertEqual(level_order(root), expected)

    def test_left_skewed_with_negatives_and_zeros(self):
        # Skewed tree: 0 -> -5 -> -10 -> 0
        root = TreeNode(0)
        root.left = TreeNode(-5)
        root.left.left = TreeNode(-10)
        root.left.left.left = TreeNode(0)
        expected = [[0], [-5], [-10], [0]]
        self.assertEqual(level_order(root), expected)

    def test_complete_binary_tree_with_duplicates(self):
        # Tree with duplicate values
        #        1
        #      /   \
        #     2     2
        #    / \   / \
        #   3   3 3   3
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(3)),
            TreeNode(2, TreeNode(3), TreeNode(3)),
        )
        expected = [[1], [2, 2], [3, 3, 3, 3]]
        self.assertEqual(level_order(root), expected)

    def test_large_complete_tree(self):
        # Build a complete binary tree of 2000 nodes
        n = 2000
        nodes = [TreeNode(i) for i in range(n)]
        for i in range(n):
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < n:
                nodes[i].left = nodes[left_idx]
            if right_idx < n:
                nodes[i].right = nodes[right_idx]

        # Compute expected levels mathematically by powers of two
        expected: list[list[int]] = []
        start = 0
        count = 1
        while start < n:
            end = min(start + count, n)
            expected.append(list(range(start, end)))
            start = end
            count *= 2

        self.assertEqual(level_order(nodes[0]), expected)
