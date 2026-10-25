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
from problem_04 import subarrays_div_by_k  # noqa: E402
# ---- End of generated header ----

import random
from collections import defaultdict


class TestSubarraysDivByK(TestCase):
    def test_example_1(self):
        nums = [4, 5, 0, -2, -3, 1]
        k = 5
        self.assertEqual(subarrays_div_by_k(nums, k), 7)

    def test_example_2(self):
        nums = [5]
        k = 9
        self.assertEqual(subarrays_div_by_k(nums, k), 0)

    def test_single_element_divisible(self):
        nums = [10]
        k = 5
        self.assertEqual(subarrays_div_by_k(nums, k), 1)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        k = 3
        # Any subarray has sum 0, divisible by 3. Total subarrays: 4 * 5 // 2 = 10
        self.assertEqual(subarrays_div_by_k(nums, k), 10)

    def test_all_negatives(self):
        nums = [-1, -2, -3, -4]
        k = 3
        # Subarrays:
        # [-3] (sum -3)
        # [-1, -2] (sum -3)
        # [-2, -3, -4] (sum -9)
        # [-1, -2, -3] (sum -6)
        self.assertEqual(subarrays_div_by_k(nums, k), 4)

    def test_alternating_values(self):
        nums = [1, -1, 1, -1]
        k = 2
        # Prefix sums: [1, 0, 1, 0]
        # Mods: 1, 0, 1, 0 with initial mod 0
        # mod 0 seen 3 times -> 3*2/2 = 3
        # mod 1 seen 2 times -> 2*1/2 = 1
        # total = 4
        self.assertEqual(subarrays_div_by_k(nums, k), 4)

    def test_large_input_performance(self):
        # Large input of size 10^5 with deterministic values
        rng = random.Random(1337)
        nums = [rng.randint(-100, 100) for _ in range(100000)]
        k = 1000
        
        # Verify with reference accumulator calculation
        ans = subarrays_div_by_k(nums, k)
        
        # Calculate expected via remainder counts
        rem_counts = defaultdict(int)
        rem_counts[0] = 1
        expected = 0
        curr = 0
        for x in nums:
            curr = (curr + x) % k
            expected += rem_counts[curr]
            rem_counts[curr] += 1
            
        self.assertEqual(ans, expected)
