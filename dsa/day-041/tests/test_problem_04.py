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
from problem_04 import TreeNode, count_parity_balanced  # noqa: E402
# ---- End of generated header ----

import random
import sys

sys.setrecursionlimit(200_000)


class TestSubtreeWeightParityBalance(TestCase):
    def test_example_1(self):
        root = TreeNode(1, TreeNode(2), TreeNode(4))
        self.assertEqual(count_parity_balanced(root), 3)

    def test_empty_tree(self):
        self.assertEqual(count_parity_balanced(None), 0)

    def test_single_node(self):
        root = TreeNode(42)
        # Left sum = 0, Right sum = 0 -> balanced
        self.assertEqual(count_parity_balanced(root), 1)

    def test_negative_values_and_unbalanced_root(self):
        # Left child: 3 (sum 3, odd)
        # Right child: 2 (sum 2, even)
        # Node 3 is balanced (0 == 0), Node 2 is balanced (0 == 0)
        # Root 5 has left sum 3 (odd) and right sum 2 (even) -> not balanced
        root = TreeNode(5, TreeNode(3), TreeNode(2))
        self.assertEqual(count_parity_balanced(root), 2)

    def test_negative_numbers_parity(self):
        # Negative numbers: -3 % 2 == 1 (odd), -5 % 2 == 1 (odd)
        # Root left sum: -3 (odd), right sum: -5 (odd) -> root is balanced
        root = TreeNode(10, TreeNode(-3), TreeNode(-5))
        self.assertEqual(count_parity_balanced(root), 3)

    def test_skewed_chain_alternating_values(self):
        # Construct a right-skewed tree of 5 nodes with values [1, 2, 3, 4, 5]
        # Leaf is node 5 (val 5): left=0, right=0 -> balanced (count=1)
        # Node 4 (val 4): left=0, right=5 (odd) -> not balanced
        # Node 3 (val 3): left=0, right=4+5=9 (odd) -> not balanced
        # Node 2 (val 2): left=0, right=3+9=12 (even) -> balanced (count=2)
        # Node 1 (val 1): left=0, right=2+12=14 (even) -> balanced (count=3)
        curr = None
        for val in reversed([1, 2, 3, 4, 5]):
            curr = TreeNode(val, None, curr)
        self.assertEqual(count_parity_balanced(curr), 3)

    def test_large_balanced_binary_tree(self):
        # Deterministically build a complete binary tree of depth 14 (~16383 nodes)
        # Every node has value 2 (even).
        # In this tree, every subtree sum is even, so left and right sums are both even everywhere.
        # Therefore, every node must be parity-balanced.
        def build_even_tree(depth: int) -> TreeNode | None:
            if depth == 0:
                return None
            return TreeNode(2, build_even_tree(depth - 1), build_even_tree(depth - 1))

        total_nodes = (1 << 14) - 1
        root = build_even_tree(14)
        self.assertEqual(count_parity_balanced(root), total_nodes)

    def test_large_random_tree_linear_time(self):
        # Test that large inputs up to 20,000 nodes execute efficiently
        rng = random.Random(1337)
        nodes = [TreeNode(rng.randint(-1000, 1000)) for _ in range(20000)]
        for i in range(1, len(nodes)):
            parent = nodes[(i - 1) // 2]
            if (i - 1) % 2 == 0:
                parent.left = nodes[i]
            else:
                parent.right = nodes[i]

        res = count_parity_balanced(nodes[0])
        self.assertIsInstance(res, int)
        self.assertGreater(res, 0)
        self.assertLessEqual(res, 20000)
