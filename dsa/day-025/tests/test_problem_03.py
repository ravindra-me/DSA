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
from problem_03 import find_first_local_minimum  # noqa: E402
# ---- End of generated header ----

import random

class TestFindFirstLocalMinimum(TestCase):
    def test_example_1(self):
        matrix = [[9, 8, 7], [6, 2, 5], [4, 3, 1]]
        self.assertEqual(find_first_local_minimum(matrix), [1, 1])

    def test_example_2(self):
        matrix = [[5, 5], [5, 5]]
        self.assertEqual(find_first_local_minimum(matrix), [-1, -1])

    def test_single_element(self):
        matrix = [[42]]
        self.assertEqual(find_first_local_minimum(matrix), [0, 0])

    def test_row_vector(self):
        matrix = [[5, 4, 3, 2, 6]]
        self.assertEqual(find_first_local_minimum(matrix), [0, 3])

    def test_column_vector(self):
        matrix = [[10], [8], [6], [7]]
        self.assertEqual(find_first_local_minimum(matrix), [2, 0])

    def test_negative_numbers_and_zeros(self):
        matrix = [
            [0, -1, 2],
            [-3, -5, -2],
            [1, 4, 0]
        ]
        self.assertEqual(find_first_local_minimum(matrix), [1, 1])

    def test_large_input_performance_and_correctness(self):
        rows, cols = 300, 300
        # Construct grid with strict decreasing order so no element is a local minimum
        total = rows * cols
        matrix = [[total - (r * cols + c) for c in range(cols)] for r in range(rows)]
        # Place a local minimum at row 250, col 250
        matrix[250][250] = -999999999
        
        self.assertEqual(find_first_local_minimum(matrix), [250, 250])
