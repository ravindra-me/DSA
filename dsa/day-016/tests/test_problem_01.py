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
from problem_01 import find_difference_pair  # noqa: E402
# ---- End of generated header ----

import random


class TestTwoSumTargetDifference(TestCase):
    def test_example_1(self):
        nums = [1, 5, 3, 4, 2]
        diff = 2
        self.assertEqual(find_difference_pair(nums, diff), (1, 2))

    def test_example_2_no_pair(self):
        nums = [2, 4, 6]
        diff = 5
        self.assertIsNone(find_difference_pair(nums, diff))

    def test_example_3_zero_diff(self):
        nums = [3, 3]
        diff = 0
        self.assertEqual(find_difference_pair(nums, diff), (0, 1))

    def test_tie_breaking_order(self):
        # For diff = 1, i = 1 (nums[1]=3, nums[j]=2) vs i = 2 (nums[2]=2, nums[j]=1)
        # i = 1 with j = 0 gives 3 - 2 = 1. i = 1 with j = 3 gives 3 - 2 = 1.
        # Smallest j is 0.
        nums = [2, 3, 2, 2]
        diff = 1
        self.assertEqual(find_difference_pair(nums, diff), (1, 0))

    def test_negative_values_and_diff(self):
        # nums[i] - nums[j] = diff => -5 - (-2) = -3
        nums = [-2, 0, -5, 4]
        diff = -3
        # i = 2 (nums[2] = -5), target = -5 - (-3) = -2 (nums[0])
        self.assertEqual(find_difference_pair(nums, diff), (2, 0))

    def test_minimum_size_two_elements(self):
        nums = [10, 20]
        self.assertEqual(find_difference_pair(nums, -10), (0, 1))
        self.assertEqual(find_difference_pair(nums, 10), (1, 0))
        self.assertIsNone(find_difference_pair(nums, 15))

    def test_large_input_performance(self):
        rng = random.Random(42)
        n = 100_000
        # Generate array of numbers where diff pair is placed predictably
        # Even numbers everywhere except one odd pair at known locations
        nums = [i * 2 for i in range(n)]
        diff = 10
        # nums[i] - nums[j] = 10 => 2*i - 2*j = 10 => i - j = 5
        # Smallest i >= 5 is i = 5, j = 0
        result = find_difference_pair(nums, diff)
        self.assertEqual(result, (5, 0))
