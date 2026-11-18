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
from problem_03 import TreeNode, zigzag_level_order  # noqa: E402
# ---- End of generated header ----

from collections import deque


def build_tree_from_level_order(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        curr = queue.popleft()
        if i < len(values) and values[i] is not None:
            curr.left = TreeNode(values[i])
            queue.append(curr.left)
        i += 1
        if i < len(values) and values[i] is not None:
            curr.right = TreeNode(values[i])
            queue.append(curr.right)
        i += 1
    return root


class TestZigzagLevelOrder(TestCase):
    def test_example_1(self):
        root = build_tree_from_level_order([3, 9, 20, None, None, 15, 7])
        self.assertEqual(zigzag_level_order(root), [[3], [20, 9], [15, 7]])

    def test_example_2(self):
        root = TreeNode(1)
        self.assertEqual(zigzag_level_order(root), [[1]])

    def test_empty_tree(self):
        self.assertEqual(zigzag_level_order(None), [])

    def test_linear_skewed_tree(self):
        # 1 -> right: 2 -> right: 3 -> right: 4
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        expected = [[1], [2], [3], [4]]
        self.assertEqual(zigzag_level_order(root), expected)

    def test_negative_values_and_duplicates(self):
        root = TreeNode(0,
                        TreeNode(-1, TreeNode(5), TreeNode(-1)),
                        TreeNode(-1, TreeNode(10), TreeNode(20)))
        # Level 0 (L->R): [0]
        # Level 1 (R->L): [-1, -1]
        # Level 2 (L->R): [5, -1, 10, 20]
        expected = [[0], [-1, -1], [5, -1, 10, 20]]
        self.assertEqual(zigzag_level_order(root), expected)

    def test_complete_binary_tree_four_levels(self):
        # 1 to 15
        nodes = [TreeNode(i) for i in range(16)]
        for i in range(1, 8):
            nodes[i].left = nodes[2 * i]
            nodes[i].right = nodes[2 * i + 1]
        root = nodes[1]
        expected = [
            [1],
            [3, 2],
            [4, 5, 6, 7],
            [15, 14, 13, 12, 11, 10, 9, 8]
        ]
        self.assertEqual(zigzag_level_order(root), expected)

    def test_large_tree_alternation(self):
        # Build a complete binary tree of 1023 nodes (depth 10)
        size = 1023
        nodes = [TreeNode(i) for i in range(size + 1)]
        for i in range(1, size // 2 + 1):
            nodes[i].left = nodes[2 * i]
            nodes[i].right = nodes[2 * i + 1]

        res = zigzag_level_order(nodes[1])
        self.assertEqual(len(res), 10)

        # Verify each level directly
        depth = 0
        start = 1
        while start <= size:
            count = 1 << depth
            vals = list(range(start, start + count))
            if depth % 2 == 1:
                vals.reverse()
            self.assertEqual(res[depth], vals)
            start += count
            depth += 1
