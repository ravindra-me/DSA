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
from problem_05 import TreeNode, vertical_traversal  # noqa: E402
# ---- End of generated header ----

import random
from collections import deque
from itertools import groupby


def build_tree(vals: list[int | None]) -> TreeNode | None:
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    idx = 1
    while q and idx < len(vals):
        node = q.popleft()
        if idx < len(vals) and vals[idx] is not None:
            node.left = TreeNode(vals[idx])
            q.append(node.left)
        idx += 1
        if idx < len(vals) and vals[idx] is not None:
            node.right = TreeNode(vals[idx])
            q.append(node.right)
        idx += 1
    return root


class TestVerticalTraversal(TestCase):
    def test_empty_tree(self):
        self.assertEqual(vertical_traversal(None), [])

    def test_single_node(self):
        root = TreeNode(42)
        self.assertEqual(vertical_traversal(root), [[42]])

    def test_example_1(self):
        # root = [3, 9, 20, null, null, 15, 7]
        root = build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(vertical_traversal(root), [[9], [3, 15], [20], [7]])

    def test_example_2_overlapping_row_and_col(self):
        # root = [1, 2, 3, 4, 6, 5, 7]
        # 2's right is 6 -> row 2, col 0
        # 3's left is 5  -> row 2, col 0
        # 5 < 6, so 5 appears before 6
        root = build_tree([1, 2, 3, 4, 6, 5, 7])
        self.assertEqual(vertical_traversal(root), [[4], [2], [1, 5, 6], [3], [7]])

    def test_duplicate_values_and_tie_breaking(self):
        # Left child and right child have identical values
        root = TreeNode(0)
        root.left = TreeNode(5)
        root.right = TreeNode(5)
        root.left.right = TreeNode(10)
        root.right.left = TreeNode(10)
        # Both 10s are at row 2, col 0; values are equal
        self.assertEqual(vertical_traversal(root), [[5], [0, 10, 10], [5]])

    def test_left_skewed_tree(self):
        curr = root = TreeNode(0)
        for i in range(1, 6):
            curr.left = TreeNode(i)
            curr = curr.left
        # Each node goes to col -i, row i
        expected = [[5], [4], [3], [2], [1], [0]]
        self.assertEqual(vertical_traversal(root), expected)

    def test_large_random_tree(self):
        rng = random.Random(1337)
        nodes: list[TreeNode | None] = [TreeNode(rng.randint(0, 1000))]
        for _ in range(800):
            val = rng.randint(0, 1000)
            parent = rng.choice([n for n in nodes if n is not None])
            if rng.choice([True, False]):
                if parent.left is None:
                    parent.left = TreeNode(val)
                    nodes.append(parent.left)
            else:
                if parent.right is None:
                    parent.right = TreeNode(val)
                    nodes.append(parent.right)

        # Reference calculation via simple DFS
        ref_entries: list[tuple[int, int, int]] = []

        def dfs(node: TreeNode | None, r: int, c: int):
            if not node:
                return
            ref_entries.append((c, r, node.val))
            dfs(node.left, r + 1, c - 1)
            dfs(node.right, r + 1, c + 1)

        dfs(nodes[0], 0, 0)
        ref_entries.sort()
        expected = [[v for _, _, v in grp] for _, grp in groupby(ref_entries, key=lambda x: x[0])]

        self.assertEqual(vertical_traversal(nodes[0]), expected)
