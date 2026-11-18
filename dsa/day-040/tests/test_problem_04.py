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
from problem_04 import TreeNode, postorder_traversal_iterative  # noqa: E402
# ---- End of generated header ----

import random

class TestPostorderIterative(TestCase):
    def test_empty_tree(self):
        self.assertEqual(postorder_traversal_iterative(None), [])

    def test_single_node(self):
        root = TreeNode(42)
        self.assertEqual(postorder_traversal_iterative(root), [42])

    def test_example_one(self):
        # root = [1, null, 2, 3]
        root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
        self.assertEqual(postorder_traversal_iterative(root), [3, 2, 1])

    def test_complete_binary_tree(self):
        #        1
        #      /   \
        #     2     3
        #    / \   / \
        #   4   5 6   7
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7))
        )
        self.assertEqual(postorder_traversal_iterative(root), [4, 5, 2, 6, 7, 3, 1])

    def test_negative_values_and_duplicates(self):
        root = TreeNode(
            0,
            TreeNode(-10, TreeNode(-10), None),
            TreeNode(0, None, TreeNode(5))
        )
        self.assertEqual(postorder_traversal_iterative(root), [-10, -10, 5, 0, 0])

    def test_left_skewed_tree(self):
        # 3 -> 2 -> 1 (left children)
        root = TreeNode(3, TreeNode(2, TreeNode(1)))
        self.assertEqual(postorder_traversal_iterative(root), [1, 2, 3])

    def test_right_skewed_tree(self):
        # 1 -> 2 -> 3 (right children)
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(postorder_traversal_iterative(root), [3, 2, 1])

    def test_large_tree_against_reference(self):
        rng = random.Random(42)
        values = [rng.randint(-1000, 1000) for _ in range(2000)]

        nodes = [TreeNode(v) for v in values]
        for i in range(len(nodes)):
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                nodes[i].left = nodes[left_idx]
            if right_idx < len(nodes):
                nodes[i].right = nodes[right_idx]

        # Reference postorder using standard recursive logic
        def ref_postorder(node: TreeNode | None) -> list[int]:
            if not node:
                return []
            return ref_postorder(node.left) + ref_postorder(node.right) + [node.val]

        expected = ref_postorder(nodes[0])
        actual = postorder_traversal_iterative(nodes[0])
        self.assertEqual(actual, expected)
