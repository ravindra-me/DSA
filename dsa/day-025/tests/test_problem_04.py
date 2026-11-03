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
from problem_04 import max_equal_frequency_with_skips  # noqa: E402
# ---- End of generated header ----

import random
import unittest

class TestMaxEqualFrequencyWithSkips(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(max_equal_frequency_with_skips([1, 2, 1, 1, 3, 1], 1), 4)

    def test_example_2(self):
        self.assertEqual(max_equal_frequency_with_skips([4, 4, 4], 2), 3)

    def test_empty_list(self):
        self.assertEqual(max_equal_frequency_with_skips([], 5), 0)

    def test_single_element(self):
        self.assertEqual(max_equal_frequency_with_skips([42], 0), 1)
        self.assertEqual(max_equal_frequency_with_skips([42], 5), 1)

    def test_zero_skips(self):
        self.assertEqual(max_equal_frequency_with_skips([1, 1, 2, 1, 1, 1, 3], 0), 3)

    def test_all_unique(self):
        self.assertEqual(max_equal_frequency_with_skips([10, 20, 30, 40], 1), 2)

    def test_negative_and_zero(self):
        self.assertEqual(max_equal_frequency_with_skips([0, -1, 0, -1, 0], 1), 3)

    def test_large_input_performance(self):
        rng = random.Random(42)
        n = 50000
        nums = [rng.choice([1, 2, 3, 4, 5]) for _ in range(n)]
        k = 100
        
        res = max_equal_frequency_with_skips(nums, k)
        self.assertGreater(res, 0)
        self.assertLessEqual(res, n)
