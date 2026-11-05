# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_04.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_04 import find_peak_element  # noqa: E402
# ---- End of generated header ----

class TestFindPeakElement(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 2, 3, 1]
        # Peak is at index 2 (value 3)
        self.assertEqual(find_peak_element(nums), 2)

    def test_example_2(self):
        nums = [1, 2, 1, 3, 5, 6, 4]
        peak_index = find_peak_element(nums)
        # Peak can be 1 (val 2) or 5 (val 6)
        self.assertIn(peak_index, [1, 5])

    def test_single_element(self):
        self.assertEqual(find_peak_element([1]), 0)

    def test_strictly_increasing(self):
        self.assertEqual(find_peak_element([1, 2, 3, 4, 5]), 4)

    def test_strictly_decreasing(self):
        self.assertEqual(find_peak_element([5, 4, 3, 2, 1]), 0)

    def test_large_input(self):
        # Large array: 1, 2, 3, ..., 50000, 49999, ..., 0
        # Peak is at index 49999
        nums = list(range(50000)) + list(range(49998, -1, -1))
        peak_index = find_peak_element(nums)
        self.assertEqual(nums[peak_index], 49999)

    def test_negative_numbers(self):
        nums = [-5, -2, -10, -1]
        peak_index = find_peak_element(nums)
        # -2 (index 1) and -1 (index 3) are peaks
        self.assertIn(peak_index, [1, 3])
