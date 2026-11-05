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
from problem_02 import search_insert  # noqa: E402
# ---- End of generated header ----

import random
import bisect

class TestSearchInsert(TestCase):
    def test_example_1_target_exists(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 5), 2)

    def test_example_2_target_missing_middle(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 2), 1)

    def test_example_3_target_missing_end(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 7), 4)

    def test_target_missing_beginning(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 0), 0)

    def test_single_element_found(self):
        self.assertEqual(search_insert([10], 10), 0)

    def test_single_element_insert_left(self):
        self.assertEqual(search_insert([10], 5), 0)

    def test_single_element_insert_right(self):
        self.assertEqual(search_insert([10], 15), 1)

    def test_negative_numbers_and_zero(self):
        nums = [-10, -5, -2, 0, 3, 8]
        self.assertEqual(search_insert(nums, -5), 1)
        self.assertEqual(search_insert(nums, -4), 2)
        self.assertEqual(search_insert(nums, 0), 3)
        self.assertEqual(search_insert(nums, 10), 6)

    def test_large_input_performance(self):
        rng = random.Random(42)
        size = 100_000
        nums = sorted(rng.sample(range(-1_000_000, 1_000_000), size))
        target = nums[size // 2]
        expected = bisect.bisect_left(nums, target)
        self.assertEqual(search_insert(nums, target), expected)

        # Choose a target guaranteed not to be in the list for a generic case
        missing_target = 2_000_000
        expected_missing = bisect.bisect_left(nums, missing_target)
        self.assertEqual(search_insert(nums, missing_target), expected_missing)
