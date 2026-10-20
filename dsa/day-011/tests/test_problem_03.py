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
from problem_03 import find_diagonal_order  # noqa: E402
# ---- End of generated header ----

import random
from collections import defaultdict


class TestDiagonalMatrixTraverse(TestCase):
    def test_example_1(self):
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 4, 7, 5, 3, 6, 8, 9]
        self.assertEqual(find_diagonal_order(mat), expected)

    def test_example_2(self):
        mat = [[1, 2], [3, 4]]
        expected = [1, 2, 3, 4]
        self.assertEqual(find_diagonal_order(mat), expected)

    def test_single_element(self):
        mat = [[42]]
        self.assertEqual(find_diagonal_order(mat), [42])

    def test_single_row(self):
        mat = [[1, 2, 3, 4]]
        expected = [1, 2, 3, 4]
        self.assertEqual(find_diagonal_order(mat), expected)

    def test_single_column(self):
        mat = [[1], [2], [3], [4]]
        expected = [1, 2, 3, 4]
        self.assertEqual(find_diagonal_order(mat), expected)

    def test_empty_matrix(self):
        self.assertEqual(find_diagonal_order([]), [])
        self.assertEqual(find_diagonal_order([[]]), [])

    def test_duplicates_and_negative_values(self):
        mat = [
            [-1, -2, 0],
            [-2, 0, 5],
            [5, 5, -1]
        ]
        expected = [-1, -2, -2, 5, 0, 0, 5, 5, -1]
        self.assertEqual(find_diagonal_order(mat), expected)

    def test_non_square_matrix(self):
        mat = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        # d=0: [1]
        # d=1: [2, 5]
        # d=2: [6, 3]
        # d=3: [4, 7]
        # d=4: [8]
        expected = [1, 2, 5, 6, 3, 4, 7, 8]
        self.assertEqual(find_diagonal_order(mat), expected)

    def test_large_matrix(self):
        rng = random.Random(42)
        rows, cols = 300, 300
        mat = [[rng.randint(-1000, 1000) for _ in range(cols)] for _ in range(rows)]

        # Compute expected result via grouping by r + c
        diagonals = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                diagonals[r + c].append(mat[r][c])

        expected = []
        for d in range(rows + cols - 1):
            if d % 2 == 0:
                expected.extend(reversed(diagonals[d]))
            else:
                expected.extend(diagonals[d])

        self.assertEqual(find_diagonal_order(mat), expected)
