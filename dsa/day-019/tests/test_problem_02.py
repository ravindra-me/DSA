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
from problem_02 import majority_element  # noqa: E402
# ---- End of generated header ----

import random


class TestMajorityElement(TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(majority_element([3, 2, 3]), 3)

    def test_example_2(self) -> None:
        self.assertEqual(majority_element([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_single_element(self) -> None:
        self.assertEqual(majority_element([1]), 1)
        self.assertEqual(majority_element([-42]), -42)
        self.assertEqual(majority_element([0]), 0)

    def test_all_identical_elements(self) -> None:
        self.assertEqual(majority_element([7, 7, 7, 7]), 7)
        self.assertEqual(majority_element([-5, -5, -5]), -5)

    def test_negative_and_zero_values(self) -> None:
        nums = [-1, 0, -1, -1, 2, -1, -1]
        self.assertEqual(majority_element(nums), -1)

    def test_extreme_values(self) -> None:
        max_val = 10**9
        min_val = -10**9
        self.assertEqual(majority_element([max_val, 1, max_val]), max_val)
        self.assertEqual(majority_element([min_val, min_val, 0]), min_val)

    def test_large_input(self) -> None:
        rng = random.Random(1337)
        n = 50_000
        majority_val = 999_999
        # Ensure majority has strictly more than n // 2 occurrences
        majority_count = n // 2 + 100
        other_count = n - majority_count
        other_vals = [rng.randint(-10**6, 10**6) for _ in range(other_count)]
        nums = [majority_val] * majority_count + other_vals
        rng.shuffle(nums)

        self.assertEqual(majority_element(nums), majority_val)
