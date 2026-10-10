# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_05.py
import os
import sys
import unittest

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_05 import first_missing_positive  # noqa: E402
# ---- End of generated header ----

import random


class TestFirstMissingPositive(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(first_missing_positive([1, 2, 0]), 3)
        self.assertEqual(first_missing_positive([3, 4, -1, 1]), 2)
        self.assertEqual(first_missing_positive([7, 8, 9, 11, 12]), 1)
        self.assertEqual(first_missing_positive([1]), 2)

    def test_single_element_cases(self) -> None:
        self.assertEqual(first_missing_positive([0]), 1)
        self.assertEqual(first_missing_positive([-5]), 1)
        self.assertEqual(first_missing_positive([2]), 1)
        self.assertEqual(first_missing_positive([1]), 2)

    def test_all_negatives_and_zeros(self) -> None:
        self.assertEqual(first_missing_positive([-1, -2, -3, 0]), 1)
        self.assertEqual(first_missing_positive([0, 0, 0]), 1)

    def test_consecutive_sequence(self) -> None:
        self.assertEqual(first_missing_positive([1, 2, 3, 4, 5]), 6)
        self.assertEqual(first_missing_positive([5, 4, 3, 2, 1]), 6)

    def test_duplicates(self) -> None:
        self.assertEqual(first_missing_positive([1, 1, 1, 1]), 2)
        self.assertEqual(first_missing_positive([2, 2, 2, 2]), 1)
        self.assertEqual(first_missing_positive([3, 3, 1, 4, 1]), 2)

    def test_large_values_outside_range(self) -> None:
        self.assertEqual(first_missing_positive([1000000, 2000000, 3000000]), 1)
        self.assertEqual(first_missing_positive([-2**31, 2**31 - 1, 1]), 2)

    def test_large_random_input(self) -> None:
        rng = random.Random(42)
        n = 50_000
        missing = 25_000
        # Create a permutation of 1..n+1 omitting `missing`
        nums = [x for x in range(1, n + 2) if x != missing]
        rng.shuffle(nums)
        # Replace some values with negative or large numbers
        nums[0] = -100
        nums[1] = 10**9
        # Now find the true expected missing number using a set
        present = set(nums)
        expected = 1
        while expected in present:
            expected += 1

        self.assertEqual(first_missing_positive(nums), expected)
