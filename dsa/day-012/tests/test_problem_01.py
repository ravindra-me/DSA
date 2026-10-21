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
from problem_01 import daily_temperatures  # noqa: E402
# ---- End of generated header ----

import random


class TestDailyTemperatures(TestCase):
    def test_example_1(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        expected = [1, 1, 4, 2, 1, 1, 0, 0]
        self.assertEqual(daily_temperatures(temperatures), expected)

    def test_example_2_strictly_decreasing(self):
        temperatures = [90, 80, 70]
        expected = [0, 0, 0]
        self.assertEqual(daily_temperatures(temperatures), expected)

    def test_single_element(self):
        temperatures = [50]
        expected = [0]
        self.assertEqual(daily_temperatures(temperatures), expected)

    def test_strictly_increasing(self):
        temperatures = [30, 40, 50, 60, 70]
        expected = [1, 1, 1, 1, 0]
        self.assertEqual(daily_temperatures(temperatures), expected)

    def test_duplicates(self):
        temperatures = [70, 70, 70, 75]
        expected = [3, 2, 1, 0]
        self.assertEqual(daily_temperatures(temperatures), expected)

    def test_all_identical(self):
        temperatures = [60, 60, 60, 60]
        expected = [0, 0, 0, 0]
        self.assertEqual(daily_temperatures(temperatures), expected)

    def test_large_input_performance(self):
        # Large test with 10^5 elements that would TLE on an O(N^2) brute force.
        # Pattern: strictly decreasing run followed by a single max value at the end.
        n = 100_000
        temperatures = [100 - (i % 50) for i in range(n - 1)] + [101]
        result = daily_temperatures(temperatures)
        self.assertEqual(len(result), n)
        self.assertEqual(result[-1], 0)
        # Each element should find a warmer day at or before the last element
        self.assertTrue(all(val > 0 for val in result[:-1]))
