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
from problem_01 import search  # noqa: E402
# ---- End of generated header ----

class TestBinarySearch(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(search([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_example_2(self):
        self.assertEqual(search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_single_element_found(self):
        self.assertEqual(search([5], 5), 0)

    def test_single_element_not_found(self):
        self.assertEqual(search([5], 1), -1)

    def test_target_at_left_bound(self):
        self.assertEqual(search([1, 3, 5, 7, 9], 1), 0)

    def test_target_at_right_bound(self):
        self.assertEqual(search([1, 3, 5, 7, 9], 9), 4)

    def test_negative_numbers_and_zero(self):
        self.assertEqual(search([-10, -5, -2, 0, 4, 8], -5), 1)
        self.assertEqual(search([-10, -5, -2, 0, 4, 8], 0), 3)

    def test_large_input_performance(self):
        import random
        rng = random.Random(42)
        n = 100_000
        nums = sorted(rng.sample(range(-500_000, 500_000), n))
        
        target_present = nums[75_000]
        self.assertEqual(search(nums, target_present), 75_000)
        
        target_absent = 999_999
        self.assertEqual(search(nums, target_absent), -1)
