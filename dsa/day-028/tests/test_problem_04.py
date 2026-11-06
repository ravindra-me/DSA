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

import random

class TestFindPeakElement(TestCase):
    def _is_valid_peak(self, nums: list[int], idx: int) -> bool:
        n = len(nums)
        if not (0 <= idx < n):
            return False
        left_val = nums[idx - 1] if idx > 0 else float('-inf')
        right_val = nums[idx + 1] if idx < n - 1 else float('-inf')
        return nums[idx] > left_val and nums[idx] > right_val

    def test_example_1(self):
        nums = [1, 2, 3, 1]
        idx = find_peak_element(nums)
        self.assertTrue(self._is_valid_peak(nums, idx))

    def test_example_2(self):
        nums = [1, 2, 1, 3, 5, 6, 4]
        idx = find_peak_element(nums)
        self.assertTrue(self._is_valid_peak(nums, idx))

    def test_single_element(self):
        nums = [1]
        idx = find_peak_element(nums)
        self.assertEqual(idx, 0)
        self.assertTrue(self._is_valid_peak(nums, idx))

    def test_strictly_increasing(self):
        nums = [1, 2, 3, 4, 5]
        idx = find_peak_element(nums)
        self.assertEqual(idx, 4)
        self.assertTrue(self._is_valid_peak(nums, idx))

    def test_strictly_decreasing(self):
        nums = [5, 4, 3, 2, 1]
        idx = find_peak_element(nums)
        self.assertEqual(idx, 0)
        self.assertTrue(self._is_valid_peak(nums, idx))

    def test_negative_numbers_and_zeros(self):
        nums = [-10, -5, -2, -8, 0, -1]
        idx = find_peak_element(nums)
        self.assertTrue(self._is_valid_peak(nums, idx))

    def test_large_input_efficiency(self):
        rng = random.Random(42)
        n = 100000
        nums = [0] * n
        val = 0
        for i in range(n):
            val += rng.choice([-1, 1]) * rng.randint(1, 10)
            nums[i] = val
        
        idx = find_peak_element(nums)
        self.assertTrue(self._is_valid_peak(nums, idx))
