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
from problem_02 import search_rotated  # noqa: E402
# ---- End of generated header ----

import random
import unittest

class TestSearchRotated(unittest.TestCase):
    def test_example_1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(search_rotated(nums, target), 4)

    def test_example_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(search_rotated(nums, target), -1)

    def test_example_3(self):
        nums = [1]
        target = 0
        self.assertEqual(search_rotated(nums, target), -1)

    def test_single_element_found(self):
        nums = [5]
        target = 5
        self.assertEqual(search_rotated(nums, target), 0)

    def test_unrotated_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(search_rotated(nums, 1), 0)
        self.assertEqual(search_rotated(nums, 4), 3)
        self.assertEqual(search_rotated(nums, 7), 6)
        self.assertEqual(search_rotated(nums, 8), -1)

    def test_negative_numbers(self):
        nums = [6, 8, -5, -3, -1, 0, 2, 4]
        self.assertEqual(search_rotated(nums, -3), 3)
        self.assertEqual(search_rotated(nums, 6), 0)
        self.assertEqual(search_rotated(nums, 4), 7)
        self.assertEqual(search_rotated(nums, -4), -1)

    def test_large_input(self):
        rng = random.Random(42)
        n = 50000
        sorted_arr = list(range(-25000, 25000))
        pivot = rng.randint(1, n - 1)
        rotated_arr = sorted_arr[pivot:] + sorted_arr[:pivot]
        
        target = 12345
        expected_idx = rotated_arr.index(target)
        self.assertEqual(search_rotated(rotated_arr, target), expected_idx)
        
        absent_target = 99999
        self.assertEqual(search_rotated(rotated_arr, absent_target), -1)
