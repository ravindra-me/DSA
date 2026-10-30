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
from problem_04 import NumMatrix  # noqa: E402
# ---- End of generated header ----

import random


class TestNumMatrix(TestCase):
    def test_example_1(self) -> None:
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
        num_matrix = NumMatrix(matrix)
        self.assertEqual(num_matrix.sum_region(2, 1, 4, 3), 8)
        self.assertEqual(num_matrix.sum_region(1, 1, 2, 2), 11)
        self.assertEqual(num_matrix.sum_region(1, 2, 2, 4), 12)

    def test_single_element(self) -> None:
        num_matrix = NumMatrix([[-5]])
        self.assertEqual(num_matrix.sum_region(0, 0, 0, 0), -5)

    def test_single_row_and_column(self) -> None:
        # 1 x 4 row vector
        row_mat = [[1, 2, 3, 4]]
        nm_row = NumMatrix(row_mat)
        self.assertEqual(nm_row.sum_region(0, 1, 0, 2), 5)
        self.assertEqual(nm_row.sum_region(0, 0, 0, 3), 10)

        # 4 x 1 column vector
        col_mat = [[-1], [2], [-3], [4]]
        nm_col = NumMatrix(col_mat)
        self.assertEqual(nm_col.sum_region(1, 0, 3, 0), 3)
        self.assertEqual(nm_col.sum_region(0, 0, 3, 0), 2)

    def test_negative_numbers_and_zeros(self) -> None:
        matrix = [
            [-2, 0, -1],
            [0, -5, 2],
            [3, -1, 0],
        ]
        num_matrix = NumMatrix(matrix)
        # Entire matrix: (-2+0-1) + (0-5+2) + (3-1+0) = -3 - 3 + 2 = -4
        self.assertEqual(num_matrix.sum_region(0, 0, 2, 2), -4)
        # Middle single element
        self.assertEqual(num_matrix.sum_region(1, 1, 1, 1), -5)
        # Bottom-right 2x2: -5 + 2 - 1 + 0 = -4
        self.assertEqual(num_matrix.sum_region(1, 1, 2, 2), -4)

    def test_full_subgrid_boundary_corners(self) -> None:
        matrix = [
            [10, 20],
            [30, 40],
        ]
        nm = NumMatrix(matrix)
        self.assertEqual(nm.sum_region(0, 0, 0, 0), 10)
        self.assertEqual(nm.sum_region(0, 1, 0, 1), 20)
        self.assertEqual(nm.sum_region(1, 0, 1, 0), 30)
        self.assertEqual(nm.sum_region(1, 1, 1, 1), 40)
        self.assertEqual(nm.sum_region(0, 0, 1, 1), 100)

    def test_large_random_matrix_and_many_queries(self) -> None:
        rng = random.Random(42)
        m, n = 50, 50
        matrix = [[rng.randint(-50, 50) for _ in range(n)] for _ in range(m)]
        num_matrix = NumMatrix(matrix)

        # Run 200 random queries and check against direct summing
        for _ in range(200):
            r1 = rng.randint(0, m - 1)
            r2 = rng.randint(r1, m - 1)
            c1 = rng.randint(0, n - 1)
            c2 = rng.randint(c1, n - 1)

            expected = sum(
                matrix[r][c] for r in range(r1, r2 + 1) for c in range(c1, c2 + 1)
            )
            actual = num_matrix.sum_region(r1, c1, r2, c2)
            self.assertEqual(actual, expected)
