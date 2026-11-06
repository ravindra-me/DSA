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
from problem_03 import find_min  # noqa: E402
# ---- End of generated header ----

import random

class TestFindMin(TestCase):
    def test_example_1(self):
        self.assertEqual(find_min([3, 4, 5, 1, 2]), 1)

    def test_example_2(self):
        self.assertEqual(find_min([4, 5, 6, 7, 0, 1, 2]), 0)

    def test_example_3(self):
        self.assertEqual(find_min([11, 13, 15, 17]), 11)

    def test_single_element(self):
        self.assertEqual(find_min([42]), 42)

    def test_two_elements_rotated(self):
        self.assertEqual(find_min([2, 1]), 1)

    def test_two_elements_sorted(self):
        self.assertEqual(find_min([1, 2]), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_min([-1, 0, 1, 2, -5, -4, -3, -2]), -5)

    def test_large_array(self):
        rng = random.Random(42)
        n = 50000
        sorted_arr = list(range(-25000, 25000))
        k = rng.randint(1, n - 1)
        rotated_arr = sorted_arr[k:] + sorted_arr[:k]
        expected = min(rotated_arr)
        self.assertEqual(find_min(rotated_arr), expected)
