# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_03.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_03 import search_range  # noqa: E402
# ---- End of generated header ----

class TestSearchRange(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(search_range([5, 7, 7, 8, 8, 10], 6), [-1, -1])
        self.assertEqual(search_range([], 0), [-1, -1])

    def test_single_element(self):
        self.assertEqual(search_range([5], 5), [0, 0])
        self.assertEqual(search_range([5], 2), [-1, -1])

    def test_duplicates_entire_array(self):
        self.assertEqual(search_range([2, 2, 2, 2, 2], 2), [0, 4])

    def test_target_at_boundaries(self):
        self.assertEqual(search_range([1, 1, 2, 3, 4], 1), [0, 1])
        self.assertEqual(search_range([1, 2, 3, 4, 4], 4), [3, 4])

    def test_target_negative_numbers(self):
        self.assertEqual(search_range([-5, -5, -2, -2, 0, 1], -2), [2, 3])

    def test_large_input(self):
        # 100,000 elements, target is in the middle
        nums = [1] * 50000 + [2] * 50000
        self.assertEqual(search_range(nums, 2), [50000, 99999])
