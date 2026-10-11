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
from problem_03 import spiral_order  # noqa: E402
# ---- End of generated header ----

class TestSpiralOrder(TestCase):
    def test_example_1_square_3x3(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(spiral_order(matrix), expected)

    def test_example_2_single_element(self):
        matrix = [[1]]
        expected = [1]
        self.assertEqual(spiral_order(matrix), expected)

    def test_example_3_rectangular_3x4(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(spiral_order(matrix), expected)

    def test_single_row(self):
        matrix = [[1, 2, 3, 4, 5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(spiral_order(matrix), expected)

    def test_single_column(self):
        matrix = [[1], [2], [3], [4], [5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(spiral_order(matrix), expected)

    def test_negative_values_and_duplicates(self):
        matrix = [
            [-5, -4, 0],
            [-5, 10, 0],
            [-1, -2, -3]
        ]
        expected = [-5, -4, 0, 0, -3, -2, -1, -5, 10]
        self.assertEqual(spiral_order(matrix), expected)

    def test_large_matrix_boundary_simulation(self):
        # 100 x 100 matrix with sequential numbers
        m, n = 100, 100
        matrix = [[r * n + c for c in range(n)] for r in range(m)]
        result = spiral_order(matrix)

        self.assertEqual(len(result), m * n)
        # Verify distinct elements were all visited exactly once
        self.assertEqual(set(result), set(range(m * n)))
        # First row check
        self.assertEqual(result[:n], list(range(n)))
        # Element immediately after the top-row is matrix[1][n-1]
        self.assertEqual(result[n], matrix[1][n - 1])
