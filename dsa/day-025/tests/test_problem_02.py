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
from problem_02 import sentinel_search  # noqa: E402
# ---- End of generated header ----

import random


class TestSentinelSearch(unittest.TestCase):
    def test_example_1(self):
        nums = [10, 20, 30]
        target = 20
        self.assertTrue(sentinel_search(nums, target))
        self.assertEqual(nums, [10, 20, 30])

    def test_example_2(self):
        nums = []
        target = 5
        self.assertFalse(sentinel_search(nums, target))
        self.assertEqual(nums, [])

    def test_single_element_found(self):
        nums = [42]
        target = 42
        self.assertTrue(sentinel_search(nums, target))
        self.assertEqual(nums, [42])

    def test_single_element_not_found(self):
        nums = [42]
        target = 7
        self.assertFalse(sentinel_search(nums, target))
        self.assertEqual(nums, [42])

    def test_target_at_ends(self):
        nums = [5, 1, 2, 3, 10]
        self.assertTrue(sentinel_search(nums, 5))
        self.assertTrue(sentinel_search(nums, 10))
        self.assertEqual(nums, [5, 1, 2, 3, 10])

    def test_duplicates_and_negatives(self):
        nums = [-10, 0, -10, 20, -5]
        self.assertTrue(sentinel_search(nums, -10))
        self.assertTrue(sentinel_search(nums, -5))
        self.assertFalse(sentinel_search(nums, 15))
        self.assertEqual(nums, [-10, 0, -10, 20, -5])

    def test_large_input_restoration(self):
        rng = random.Random(42)
        nums = [rng.randint(-10**9, 10**9) for _ in range(100_000)]
        target = 999_999_999  # very unlikely to exist randomly
        nums_copy = list(nums)
        
        result = sentinel_search(nums, target)
        expected = target in nums_copy
        
        self.assertEqual(result, expected)
        self.assertEqual(nums, nums_copy)
