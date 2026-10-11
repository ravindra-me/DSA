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
from problem_05 import first_missing_positive  # noqa: E402
# ---- End of generated header ----

import random

class TestFirstMissingPositive(TestCase):
    def test_examples(self):
        self.assertEqual(first_missing_positive([1, 2, 0]), 3)
        self.assertEqual(first_missing_positive([3, 4, -1, 1]), 2)
        self.assertEqual(first_missing_positive([7, 8, 9, 11, 12]), 1)

    def test_single_element(self):
        self.assertEqual(first_missing_positive([1]), 2)
        self.assertEqual(first_missing_positive([2]), 1)
        self.assertEqual(first_missing_positive([0]), 1)
        self.assertEqual(first_missing_positive([-5]), 1)

    def test_negatives_and_zeros(self):
        self.assertEqual(first_missing_positive([-1, -2, -3, 0]), 1)
        self.assertEqual(first_missing_positive([0, 0, 0]), 1)

    def test_duplicates(self):
        self.assertEqual(first_missing_positive([1, 1]), 2)
        self.assertEqual(first_missing_positive([2, 2, 1, 1]), 3)

    def test_consecutive_sequence(self):
        self.assertEqual(first_missing_positive([1, 2, 3, 4, 5]), 6)
        self.assertEqual(first_missing_positive([2, 3, 4, 5]), 1)

    def test_large_input(self):
        rng = random.Random(42)
        n = 50000
        missing_target = 34567
        # Create list containing numbers 1..n except missing_target
        nums = [i for i in range(1, n + 2) if i != missing_target]
        rng.shuffle(nums)
        self.assertEqual(first_missing_positive(nums), missing_target)
