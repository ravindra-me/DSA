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
from problem_05 import max_area  # noqa: E402
# ---- End of generated header ----

import random


class TestContainerWithMostWater(TestCase):
    def test_examples(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(max_area([1, 1]), 1)
        self.assertEqual(max_area([4, 3, 2, 1, 4]), 16)

    def test_minimum_length(self):
        self.assertEqual(max_area([2, 5]), 2)
        self.assertEqual(max_area([5, 2]), 2)
        self.assertEqual(max_area([10000, 10000]), 10000)

    def test_all_zeros_and_isolated_tall_lines(self):
        self.assertEqual(max_area([0, 0, 0, 0]), 0)
        self.assertEqual(max_area([0, 10, 0]), 0)
        self.assertEqual(max_area([10, 0, 0, 10]), 30)

    def test_strictly_monotonic(self):
        # Strictly increasing: [1, 2, 3, 4, 5]
        # Max area formed by 2 and 5 (width 3, height 2 -> 6) or 3 and 5 (width 2, height 3 -> 6)
        self.assertEqual(max_area([1, 2, 3, 4, 5]), 6)
        # Strictly decreasing
        self.assertEqual(max_area([5, 4, 3, 2, 1]), 6)

    def test_equal_heights(self):
        self.assertEqual(max_area([5, 5, 5, 5, 5]), 20)

    def test_tall_middle_vs_wide_outer(self):
        # Narrow very tall pair vs wide short pair
        # Outer: indices 0 and 5 -> width 5, height 2 -> 10
        # Middle: indices 2 and 3 -> width 1, height 100 -> 100
        self.assertEqual(max_area([2, 1, 100, 100, 1, 2]), 100)

    def test_large_random_input(self):
        rng = random.Random(42)
        # Large input of 50,000 elements to verify linear time performance
        n = 50000
        heights = [rng.randint(0, 1000) for _ in range(n)]
        # Place known large pillars at known locations
        heights[0] = 5000
        heights[-1] = 5000
        # The outer pillars provide at least 5000 * (n - 1)
        expected_floor = 5000 * (n - 1)
        result = max_area(heights)
        self.assertGreaterEqual(result, expected_floor)
