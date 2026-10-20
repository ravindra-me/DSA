# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_02.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_02 import product_except_self  # noqa: E402
# ---- End of generated header ----

import random


class TestProductExceptSelf(TestCase):
    def test_example_one(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertEqual(product_except_self(nums), expected)

    def test_example_two_with_single_zero(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertEqual(product_except_self(nums), expected)

    def test_minimum_length_two(self):
        nums = [5, 10]
        expected = [10, 5]
        self.assertEqual(product_except_self(nums), expected)

    def test_multiple_zeros(self):
        nums = [0, 4, 0]
        expected = [0, 0, 0]
        self.assertEqual(product_except_self(nums), expected)

    def test_all_negative_values(self):
        nums = [-2, -3, -4]
        expected = [12, 8, 6]
        self.assertEqual(product_except_self(nums), expected)

    def test_ones_and_negatives(self):
        nums = [1, -1, 1, -1]
        expected = [1, -1, 1, -1]
        self.assertEqual(product_except_self(nums), expected)

    def test_large_input_performance(self):
        rng = random.Random(42)
        # Mostly 1s and -1s to ensure intermediate and total products don't overflow constraints
        nums = [rng.choice([-1, 1]) for _ in range(50000)]
        result = product_except_self(nums)
        self.assertEqual(len(result), 50000)

        # Verify with brute force check on first 5 and last 5 elements
        for check_idx in [0, 1, 2, 49998, 49999]:
            expected_val = 1
            for j, val in enumerate(nums):
                if j != check_idx:
                    expected_val *= val
            self.assertEqual(result[check_idx], expected_val)
