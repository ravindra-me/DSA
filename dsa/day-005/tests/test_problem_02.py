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
from problem_02 import array_gcd_lcm  # noqa: E402
# ---- End of generated header ----

import math
import random
from functools import reduce


class TestArrayGcdLcm(TestCase):
    def test_examples(self):
        self.assertEqual(array_gcd_lcm([12, 18, 24]), (6, 72))
        self.assertEqual(array_gcd_lcm([7]), (7, 7))
        self.assertEqual(array_gcd_lcm([4, 6, 8, 12]), (2, 24))

    def test_single_element(self):
        self.assertEqual(array_gcd_lcm([42]), (42, 42))
        self.assertEqual(array_gcd_lcm([1]), (1, 1))

    def test_all_identical_elements(self):
        self.assertEqual(array_gcd_lcm([15, 15, 15, 15]), (15, 15))

    def test_coprime_elements(self):
        self.assertEqual(array_gcd_lcm([3, 5, 7, 11]), (1, 3 * 5 * 7 * 11))

    def test_contains_one(self):
        self.assertEqual(array_gcd_lcm([1, 10, 20]), (1, 20))
        self.assertEqual(array_gcd_lcm([10, 20, 1]), (1, 20))

    def test_powers_of_two(self):
        nums = [2, 4, 8, 16, 32, 64]
        self.assertEqual(array_gcd_lcm(nums), (2, 64))

    def test_large_input_linear_time(self):
        # 10,000 numbers with known common factors
        rng = random.Random(42)
        base_gcd = 6
        # Each number is 6 * small multiplier from {1, 2, 3, 4, 5}
        nums = [base_gcd * rng.choice([1, 2, 3, 4, 5]) for _ in range(10_000)]
        nums.append(base_gcd)  # guarantees overall GCD is 6

        res_gcd, res_lcm = array_gcd_lcm(nums)
        self.assertEqual(res_gcd, 6)
        # LCM of 6 * {1, 2, 3, 4, 5} is 6 * lcm(1,2,3,4,5) = 6 * 60 = 360
        self.assertEqual(res_lcm, 360)
