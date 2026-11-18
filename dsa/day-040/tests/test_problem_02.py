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
from problem_02 import TreeNode, inorder_traversal_iterative  # noqa: E402
# ---- End of generated header ----

class TestInorderTraversalIterative(TestCase):
    def test_example_1(self):
        # root = [1, null, 2, 3]
        root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
        self.assertEqual(inorder_traversal_iterative(root), [1, 3, 2])

    def test_example_2_empty(self):
        self.assertEqual(inorder_traversal_iterative(None), [])

    def test_single_node(self):
        root = TreeNode(42)
        self.assertEqual(inorder_traversal_iterative(root), [42])

    def test_complete_binary_tree(self):
        #       1
        #      / \
        #     2   3
        #    / \   \
        #   4   5   6
        root = TreeNode(1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, None, TreeNode(6))
        )
        self.assertEqual(inorder_traversal_iterative(root), [4, 2, 5, 1, 3, 6])

    def test_left_skewed_and_negative_values(self):
        # Skewed left: -1 <- -2 <- -3
        root = TreeNode(-1, TreeNode(-2, TreeNode(-3)))
        self.assertEqual(inorder_traversal_iterative(root), [-3, -2, -1])

    def test_right_skewed_and_duplicates(self):
        # Skewed right with duplicate values: 0 -> 0 -> 0
        root = TreeNode(0, None, TreeNode(0, None, TreeNode(0)))
        self.assertEqual(inorder_traversal_iterative(root), [0, 0, 0])

    def test_large_balanced_bst(self):
        values = list(range(-1000, 1001))

        def build_bst(nums: list[int]) -> TreeNode | None:
            if not nums:
                return None
            mid = len(nums) // 2
            return TreeNode(
                val=nums[mid],
                left=build_bst(nums[:mid]),
                right=build_bst(nums[mid + 1:])
            )

        root = build_bst(values)
        self.assertEqual(inorder_traversal_iterative(root), values)
