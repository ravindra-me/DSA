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
from problem_05 import TreeNode, deserialize_preorder  # noqa: E402
# ---- End of generated header ----

class TestDeserializePreorder(TestCase):
    def test_example_1(self):
        preorder = "1,2,#,#,3,#,#"
        root = deserialize_preorder(preorder)
        self.assertIsNotNone(root)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertEqual(root.right.val, 3)
        self.assertIsNone(root.right.left)
        self.assertIsNone(root.right.right)

    def test_single_null(self):
        self.assertIsNone(deserialize_preorder("#"))

    def test_single_node(self):
        root = deserialize_preorder("42,#,#")
        self.assertIsNotNone(root)
        self.assertEqual(root.val, 42)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_negative_values_and_zeros(self):
        preorder = "0,-5,#,#,-10,#,#"
        root = deserialize_preorder(preorder)
        self.assertIsNotNone(root)
        self.assertEqual(root.val, 0)
        self.assertEqual(root.left.val, -5)
        self.assertEqual(root.right.val, -10)

    def test_left_skewed_chain(self):
        preorder = "1,2,3,#,#,#,#"
        root = deserialize_preorder(preorder)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.left.left.val, 3)
        self.assertIsNone(root.right)

    def test_large_input_iterative(self):
        # Construct deep left-skewed string: 1000 nodes
        n = 1000
        tokens = [str(i) for i in range(n)] + ["#"] * (n + 1)
        preorder = ",".join(tokens)
        
        root = deserialize_preorder(preorder)
        curr = root
        for i in range(n):
            self.assertIsNotNone(curr)
            self.assertEqual(curr.val, i)
            curr = curr.left
        self.assertIsNone(curr)
