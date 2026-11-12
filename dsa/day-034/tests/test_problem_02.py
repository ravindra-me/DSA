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
from problem_02 import find_kth_smallest  # noqa: E402
# ---- End of generated header ----

import random

class TestKthSmallest(TestCase):
    def test_example_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(find_kth_smallest(nums, 2), 2)

    def test_example_2(self):
        nums = [7, 10, 4, 3, 20, 15]
        self.assertEqual(find_kth_smallest(nums, 4), 10)

    def test_single_element(self):
        nums = [42]
        self.assertEqual(find_kth_smallest(nums, 1), 42)

    def test_duplicates(self):
        nums = [5, 5, 5, 5, 5]
        self.assertEqual(find_kth_smallest(nums, 3), 5)

    def test_negatives_and_zeros(self):
        nums = [0, -1, -5, 3, 2, -1]
        # Sorted: [-5, -1, -1, 0, 2, 3]
        self.assertEqual(find_kth_smallest(nums, 1), -5)
        self.assertEqual(find_kth_smallest(nums, 3), -1)
        self.assertEqual(find_kth_smallest(nums, 6), 3)

    def test_large_input(self):
        rng = random.Random(42)
        nums = [rng.randint(-10**6, 10**6) for _ in range(50000)]
        sorted_nums = sorted(nums)
        
        k = 25000
        expected = sorted_nums[k - 1]
        self.assertEqual(find_kth_smallest(nums, k), expected)
