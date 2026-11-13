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
from problem_05 import constrained_subset_sum  # noqa: E402
# ---- End of generated header ----

import unittest
import random

class TestConstrainedSubsetSum(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(constrained_subset_sum([10, 2, -10, 5, 20], 2), 37)

    def test_example_2(self):
        self.assertEqual(constrained_subset_sum([-1, -2, -3], 1), -1)

    def test_single_element(self):
        self.assertEqual(constrained_subset_sum([42], 1), 42)
        self.assertEqual(constrained_subset_sum([-10], 5), -10)

    def test_k_equals_one(self):
        # Must pick adjacent elements or single elements
        nums = [10, -2, -10, -5, 20]
        # Valid sequences with k=1: [10], [20], [10, -2] -> 8, etc. Max is 20.
        self.assertEqual(constrained_subset_sum(nums, 1), 20)

    def test_all_positive(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(constrained_subset_sum(nums, 2), 15)

    def test_all_negative(self):
        nums = [-5, -1, -8, -10]
        self.assertEqual(constrained_subset_sum(nums, 2), -1)

    def test_large_input_performance(self):
        rng = random.Random(42)
        n = 50000
        k = 1000
        nums = [rng.randint(-100, 100) for _ in range(n)]
        
        # Verify solution finishes quickly without TLE
        result = constrained_subset_sum(nums, k)
        self.assertIsInstance(result, int)
