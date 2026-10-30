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

    def test_example_two_with_zero(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertEqual(product_except_self(nums), expected)

    def test_two_elements_minimum_length(self):
        nums = [5, 10]
        expected = [10, 5]
        self.assertEqual(product_except_self(nums), expected)

    def test_two_elements_negative(self):
        nums = [-3, -7]
        expected = [-7, -3]
        self.assertEqual(product_except_self(nums), expected)

    def test_multiple_zeros(self):
        nums = [0, 4, 0]
        expected = [0, 0, 0]
        self.assertEqual(product_except_self(nums), expected)

    def test_all_ones_and_negative_ones(self):
        nums = [1, -1, 1, -1]
        expected = [1, -1, 1, -1]
        self.assertEqual(product_except_self(nums), expected)

    def test_odd_negative_ones(self):
        nums = [-1, 1, 1]
        expected = [1, -1, -1]
        self.assertEqual(product_except_self(nums), expected)

    def test_duplicate_values(self):
        nums = [2, 2, 2, 2]
        expected = [8, 8, 8, 8]
        self.assertEqual(product_except_self(nums), expected)

    def test_large_input_performance(self):
        # Large input of 50,000 elements (alternating 1 and -1)
        n = 50000
        nums = [1 if i % 2 == 0 else -1 for i in range(n)]
        result = product_except_self(nums)
        self.assertEqual(len(result), n)
        for i in range(100):
            self.assertEqual(result[i], nums[i])
        for i in range(n - 100, n):
            self.assertEqual(result[i], nums[i])
