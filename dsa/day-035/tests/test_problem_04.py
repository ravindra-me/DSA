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
from problem_04 import maximal_rectangle  # noqa: E402
# ---- End of generated header ----

import random

class TestMaximalRectangle(unittest.TestCase):
    def test_example_1(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
        self.assertEqual(maximal_rectangle(matrix), 6)

    def test_example_2(self):
        matrix = [["0"]]
        self.assertEqual(maximal_rectangle(matrix), 0)

    def test_single_one(self):
        matrix = [["1"]]
        self.assertEqual(maximal_rectangle(matrix), 1)

    def test_all_ones(self):
        matrix = [
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"]
        ]
        self.assertEqual(maximal_rectangle(matrix), 9)

    def test_all_zeros(self):
        matrix = [
            ["0", "0"],
            ["0", "0"]
        ]
        self.assertEqual(maximal_rectangle(matrix), 0)

    def test_single_row_and_column(self):
        row_matrix = [["1", "1", "0", "1", "1", "1"]]
        self.assertEqual(maximal_rectangle(row_matrix), 3)

        col_matrix = [["1"], ["1"], ["0"], ["1"]]
        self.assertEqual(maximal_rectangle(col_matrix), 2)

    def test_large_input_performance(self):
        rng = random.Random(42)
        R, C = 200, 200
        matrix = []
        for r in range(R):
            row = []
            for c in range(C):
                row.append("1" if rng.random() > 0.15 else "0")
            matrix.append(row)

        result = maximal_rectangle(matrix)
        self.assertGreater(result, 0)
        self.assertLessEqual(result, R * C)
