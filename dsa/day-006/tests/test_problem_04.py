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
from problem_04 import single_number_two_uniques  # noqa: E402
# ---- End of generated header ----

import random


class TestSingleNumberTwoUniques(TestCase):
    def test_example_1(self):
        nums = [1, 2, 1, 3, 2, 5]
        self.assertEqual(single_number_two_uniques(nums), [3, 5])

    def test_example_2(self):
        nums = [-1, 0]
        self.assertEqual(single_number_two_uniques(nums), [-1, 0])

    def test_minimum_length_two_elements(self):
        nums = [42, 17]
        self.assertEqual(single_number_two_uniques(nums), [17, 42])

    def test_negative_and_positive_numbers(self):
        nums = [-10, 5, -10, 7, 5, -3]
        self.assertEqual(single_number_two_uniques(nums), [-3, 7])

    def test_boundary_values_32_bit_integers(self):
        min_int = -(1 << 31)
        max_int = (1 << 31) - 1
        nums = [min_int, 0, max_int, 0]
        self.assertEqual(single_number_two_uniques(nums), [min_int, max_int])

    def test_with_zero_as_unique(self):
        nums = [100, 0, 100, 250]
        self.assertEqual(single_number_two_uniques(nums), [0, 250])

    def test_large_input_linear_time(self):
        rng = random.Random(42)
        unique_a = -123456789
        unique_b = 987654321
        # Generate 40,000 paired numbers (80,000 elements) + 2 unique numbers = 80,002 elements
        paired = rng.sample(range(1_000_000, 2_000_000), 40000)
        nums = paired + paired + [unique_a, unique_b]
        rng.shuffle(nums)

        expected = sorted([unique_a, unique_b])
        self.assertEqual(single_number_two_uniques(nums), expected)
