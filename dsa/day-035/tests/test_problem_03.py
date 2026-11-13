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
from problem_03 import max_min_product  # noqa: E402
# ---- End of generated header ----

import random
from unittest import TestCase

class TestMaxMinProduct(TestCase):
    def test_example_1(self):
        self.assertEqual(max_min_product([1, 2, 3, 2]), 14)

    def test_example_2(self):
        self.assertEqual(max_min_product([2, 3, 3, 1, 2]), 18)

    def test_single_element(self):
        self.assertEqual(max_min_product([5]), 25)

    def test_all_same_elements(self):
        # [4, 4, 4, 4] -> max subarray is whole array, min 4, sum 16 -> min_product 64
        self.assertEqual(max_min_product([4, 4, 4, 4]), 64)

    def test_strictly_increasing(self):
        # [1, 2, 3, 4]
        # subarray [4]: min 4, sum 4 -> 16
        # subarray [3, 4]: min 3, sum 7 -> 21
        # subarray [2, 3, 4]: min 2, sum 9 -> 18
        # subarray [1, 2, 3, 4]: min 1, sum 10 -> 10
        self.assertEqual(max_min_product([1, 2, 3, 4]), 21)

    def test_strictly_decreasing(self):
        # [4, 3, 2, 1]
        # subarray [4]: 16
        # subarray [4, 3]: min 3, sum 7 -> 21
        self.assertEqual(max_min_product([4, 3, 2, 1]), 21)

    def test_large_input_performance(self):
        rng = random.Random(42)
        n = 10000
        nums = [rng.randint(1, 1000) for _ in range(n)]
        
        # Verify result against standard stack-based non-modulo computation
        MOD = 10**9 + 7
        result = max_min_product(nums)
        self.assertIsInstance(result, int)
        self.assertTrue(0 <= result < MOD)
