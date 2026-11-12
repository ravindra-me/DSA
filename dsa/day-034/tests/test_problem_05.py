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
from problem_05 import wiggle_sort  # noqa: E402
# ---- End of generated header ----

import random
import unittest

class TestWiggleSort(unittest.TestCase):
    def _is_wiggle_valid(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 1):
            if i % 2 == 0:
                if nums[i] >= nums[i + 1]:
                    return False
            else:
                if nums[i] <= nums[i + 1]:
                    return False
        return True

    def test_example_1(self):
        nums = [1, 5, 1, 1, 6, 4]
        wiggle_sort(nums)
        self.assertTrue(self._is_wiggle_valid(nums), f"Invalid wiggle ordering: {nums}")

    def test_example_2(self):
        nums = [1, 3, 2, 2, 3, 1]
        wiggle_sort(nums)
        self.assertTrue(self._is_wiggle_valid(nums), f"Invalid wiggle ordering: {nums}")

    def test_single_element(self):
        nums = [1]
        wiggle_sort(nums)
        self.assertEqual(nums, [1])

    def test_two_elements(self):
        nums = [1, 2]
        wiggle_sort(nums)
        self.assertTrue(self._is_wiggle_valid(nums))

    def test_duplicates(self):
        nums = [4, 5, 5, 6]
        wiggle_sort(nums)
        self.assertTrue(self._is_wiggle_valid(nums))

    def test_large_input(self):
        rng = random.Random(42)
        # Construct a large valid input dataset
        # Generating numbers where a wiggle sort solution exists
        base = [1, 2, 3, 4, 5] * 2000
        rng.shuffle(base)
        wiggle_sort(base)
        self.assertTrue(self._is_wiggle_valid(base))
