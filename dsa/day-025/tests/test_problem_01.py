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
from problem_01 import find_first_occurrence  # noqa: E402
# ---- End of generated header ----

import random
import unittest

class TestFindFirstOccurrence(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(find_first_occurrence([4, 2, 7, 2, 5], 2), 1)

    def test_example_2(self):
        self.assertEqual(find_first_occurrence([1, 3, 5], 4), -1)

    def test_empty_list(self):
        self.assertEqual(find_first_occurrence([], 10), -1)

    def test_single_element_found(self):
        self.assertEqual(find_first_occurrence([42], 42), 0)

    def test_single_element_not_found(self):
        self.assertEqual(find_first_occurrence([42], 7), -1)

    def test_multiple_duplicates(self):
        self.assertEqual(find_first_occurrence([5, 5, 5, 5], 5), 0)

    def test_negative_numbers_and_zero(self):
        self.assertEqual(find_first_occurrence([-10, -5, 0, 5, 10], -5), 1)
        self.assertEqual(find_first_occurrence([-10, -5, 0, 5, 10], 0), 2)

    def test_large_input(self):
        rng = random.Random(42)
        nums = [rng.randint(-10**9, 10**9) for _ in range(10**5)]
        target = 999999
        nums[75000] = target
        self.assertEqual(find_first_occurrence(nums, target), 75000)
