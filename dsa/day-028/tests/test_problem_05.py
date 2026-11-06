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
from problem_05 import search_matrix  # noqa: E402
# ---- End of generated header ----

import random

class TestSearchMatrix(TestCase):
    def test_example_1_target_exists(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self.assertTrue(search_matrix(matrix, 5))

    def test_example_2_target_absent(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self.assertFalse(search_matrix(matrix, 20))

    def test_single_element(self):
        matrix = [[-5]]
        self.assertTrue(search_matrix(matrix, -5))
        self.assertFalse(search_matrix(matrix, 0))

    def test_negative_numbers_and_zero(self):
        matrix = [
            [-10, -5, 0],
            [-3, -1, 4],
            [2, 3, 8]
        ]
        self.assertTrue(search_matrix(matrix, -5))
        self.assertTrue(search_matrix(matrix, 0))
        self.assertFalse(search_matrix(matrix, 1))

    def test_duplicates(self):
        matrix = [
            [1, 2, 2],
            [2, 2, 3],
            [2, 3, 4]
        ]
        self.assertTrue(search_matrix(matrix, 2))
        self.assertTrue(search_matrix(matrix, 3))
        self.assertFalse(search_matrix(matrix, 5))

    def test_large_matrix(self):
        m, n = 300, 300
        matrix = [[i + j for j in range(n)] for i in range(m)]
        
        # Test existing elements
        self.assertTrue(search_matrix(matrix, 0))
        self.assertTrue(search_matrix(matrix, m + n - 2))
        self.assertTrue(search_matrix(matrix, 150))
        
        # Test non-existing elements
        self.assertFalse(search_matrix(matrix, -1))
        self.assertFalse(search_matrix(matrix, m + n))
