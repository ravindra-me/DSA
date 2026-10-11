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
from problem_04 import set_zeroes  # noqa: E402
# ---- End of generated header ----

import random

class TestSetZeroes(TestCase):
    def test_example_1(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        set_zeroes(matrix)
        self.assertEqual(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    def test_example_2(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        set_zeroes(matrix)
        self.assertEqual(matrix, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])

    def test_single_element_non_zero(self):
        matrix = [[1]]
        set_zeroes(matrix)
        self.assertEqual(matrix, [[1]])

    def test_single_element_zero(self):
        matrix = [[0]]
        set_zeroes(matrix)
        self.assertEqual(matrix, [[0]])

    def test_single_row_and_single_col(self):
        row_matrix = [[1, 0, 3]]
        set_zeroes(row_matrix)
        self.assertEqual(row_matrix, [[0, 0, 0]])

        col_matrix = [[1], [0], [3]]
        set_zeroes(col_matrix)
        self.assertEqual(col_matrix, [[0], [0], [0]])

    def test_negative_and_large_numbers(self):
        matrix = [
            [-2**31, 2, 3],
            [4, 0, -5],
            [6, 7, 2**31 - 1]
        ]
        set_zeroes(matrix)
        expected = [
            [-2**31, 0, 3],
            [0, 0, 0],
            [6, 0, 2**31 - 1]
        ]
        self.assertEqual(matrix, expected)

    def test_large_matrix(self):
        rng = random.Random(42)
        rows, cols = 150, 150
        matrix = [[rng.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
        
        zero_points = [(10, 20), (50, 60), (100, 110)]
        for r, c in zero_points:
            matrix[r][c] = 0
            
        expected_zero_rows = {r for r, _ in zero_points}
        expected_zero_cols = {c for _, c in zero_points}
        
        set_zeroes(matrix)
        
        for r in range(rows):
            for c in range(cols):
                if r in expected_zero_rows or c in expected_zero_cols:
                    self.assertEqual(matrix[r][c], 0)
                else:
                    self.assertNotEqual(matrix[r][c], 0)
