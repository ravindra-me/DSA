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
from problem_04 import largest_rectangle_area  # noqa: E402
# ---- End of generated header ----

import random
from typing import List


class TestLargestRectangleArea(TestCase):
    def test_example_one(self):
        self.assertEqual(largest_rectangle_area([2, 1, 5, 6, 2, 3]), 10)

    def test_example_two(self):
        self.assertEqual(largest_rectangle_area([2, 4]), 4)

    def test_single_element(self):
        self.assertEqual(largest_rectangle_area([5]), 5)
        self.assertEqual(largest_rectangle_area([0]), 0)

    def test_all_zeros(self):
        self.assertEqual(largest_rectangle_area([0, 0, 0, 0]), 0)

    def test_all_equal_elements(self):
        self.assertEqual(largest_rectangle_area([3, 3, 3, 3]), 12)

    def test_strictly_increasing_and_decreasing(self):
        self.assertEqual(largest_rectangle_area([1, 2, 3, 4, 5]), 9)  # 3 * 3 = 9
        self.assertEqual(largest_rectangle_area([5, 4, 3, 2, 1]), 9)  # 3 * 3 = 9

    def test_valley_and_peak(self):
        self.assertEqual(largest_rectangle_area([6, 1, 6]), 6)
        self.assertEqual(largest_rectangle_area([1, 6, 1]), 6)

    def test_large_uniform_input(self):
        n = 100_000
        heights = [100] * n
        self.assertEqual(largest_rectangle_area(heights), 100 * n)

    def test_large_deterministic_staircase(self):
        n = 10_000
        # Increasing staircase: i * (n - i + 1) max
        heights = list(range(1, n + 1))
        expected = max(h * (n - h + 1) for h in heights)
        self.assertEqual(largest_rectangle_area(heights), expected)
