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
from problem_01 import is_valid_max_heap  # noqa: E402
# ---- End of generated header ----

import random


class TestIsValidMaxHeap(TestCase):
    def test_examples(self):
        self.assertTrue(is_valid_max_heap([10, 5, 8, 2, 4, 6, 7]))
        self.assertFalse(is_valid_max_heap([10, 5, 8, 2, 9]))
        self.assertTrue(is_valid_max_heap([]))

    def test_empty_and_single_element(self):
        self.assertTrue(is_valid_max_heap([]))
        self.assertTrue(is_valid_max_heap([42]))
        self.assertTrue(is_valid_max_heap([-999]))

    def test_two_and_three_elements(self):
        self.assertTrue(is_valid_max_heap([10, 5]))
        self.assertFalse(is_valid_max_heap([5, 10]))
        self.assertTrue(is_valid_max_heap([10, 5, 8]))
        self.assertFalse(is_valid_max_heap([10, 5, 12]))

    def test_duplicates_and_all_equal(self):
        self.assertTrue(is_valid_max_heap([5, 5, 5, 5, 5]))
        self.assertTrue(is_valid_max_heap([10, 10, 8, 7, 10]))
        self.assertFalse(is_valid_max_heap([10, 10, 8, 7, 11]))

    def test_negative_values(self):
        self.assertTrue(is_valid_max_heap([-2, -5, -3, -10, -6]))
        self.assertFalse(is_valid_max_heap([-2, -5, -1, -10, -6]))

    def test_violation_at_leaves(self):
        # Violation only at the very last element
        valid_prefix = [100, 50, 40, 25, 20, 15, 10]
        self.assertTrue(is_valid_max_heap(valid_prefix))
        invalid = valid_prefix + [200]
        self.assertFalse(is_valid_max_heap(invalid))

    def test_large_valid_and_invalid_heap(self):
        rng = random.Random(42)
        n = 100_000
        # Generate a strictly decreasing array (or values derived such that parent >= child)
        # For each index i, we can set nums[i] = n - i, which guarantees parent >= child
        large_valid = [n - i for i in range(n)]
        self.assertTrue(is_valid_max_heap(large_valid))

        # Invalidate a single node near the end
        large_invalid = list(large_valid)
        large_invalid[-1] = large_invalid[0] + 1
        self.assertFalse(is_valid_max_heap(large_invalid))
