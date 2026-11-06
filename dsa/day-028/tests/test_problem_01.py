# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_01 import search_range  # noqa: E402
# ---- End of generated header ----

import random
import unittest

class TestSearchRange(unittest.TestCase):
    def test_example_found(self):
        self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 8), [3, 4])

    def test_example_not_found(self):
        self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 6), [-1, -1])

    def test_example_empty(self):
        self.assertEqual(search_range([], 0), [-1, -1])

    def test_single_element_hit(self):
        self.assertEqual(search_range([5], 5), [0, 0])

    def test_single_element_miss(self):
        self.assertEqual(search_range([5], 3), [-1, -1])

    def test_all_elements_same(self):
        self.assertEqual(search_range([2, 2, 2, 2, 2], 2), [0, 4])

    def test_negative_numbers(self):
        self.assertEqual(search_range([-10, -5, -5, -5, 0, 3], -5), [1, 3])

    def test_large_input_performance(self):
        # Large array filled with repeated numbers to test logarithmic performance
        n = 10**5
        nums = [1] * (n // 4) + [5] * (n // 2) + [10] * (n // 4)
        first_expected = n // 4
        last_expected = first_expected + (n // 2) - 1
        self.assertEqual(search_range(nums, 5), [first_expected, last_expected])
