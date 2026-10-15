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
from problem_02 import single_number  # noqa: E402
# ---- End of generated header ----

import random


class TestSingleNumber(TestCase):
    def test_example_one(self) -> None:
        self.assertEqual(single_number([4, 1, 2, 1, 2]), 4)

    def test_example_two_single_element(self) -> None:
        self.assertEqual(single_number([99]), 99)

    def test_with_negative_numbers(self) -> None:
        nums = [-1, -2, -1, 5, -2]
        self.assertEqual(single_number(nums), 5)

    def test_unique_is_negative(self) -> None:
        nums = [10, -7, 10, 42, 42]
        self.assertEqual(single_number(nums), -7)

    def test_with_zeros(self) -> None:
        # Zero paired with another zero
        self.assertEqual(single_number([0, 7, 0]), 7)
        # Zero is the unique element
        self.assertEqual(single_number([3, 0, 3]), 0)

    def test_extreme_values(self) -> None:
        max_val = (1 << 31) - 1
        min_val = -(1 << 31)
        nums = [max_val, min_val, max_val]
        self.assertEqual(single_number(nums), min_val)

    def test_large_input(self) -> None:
        rng = random.Random(42)
        num_pairs = 50_000
        unique_val = 123456789

        # Generate distinct pairs
        pairs = rng.sample(range(-1_000_000, 1_000_000), num_pairs)
        nums = []
        for p in pairs:
            nums.extend([p, p])
        nums.append(unique_val)

        rng.shuffle(nums)
        self.assertEqual(single_number(nums), unique_val)
