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
from problem_01 import count_subarrays_divisible  # noqa: E402
# ---- End of generated header ----

import random

class TestSubarraySumDivisibilityCounter(TestCase):
    def test_example_1(self):
        nums = [4, 5, 0, -2, -3, 1]
        k = 5
        self.assertEqual(count_subarrays_divisible(nums, k), 7)

    def test_example_2(self):
        nums = [5]
        k = 9
        self.assertEqual(count_subarrays_divisible(nums, k), 0)

    def test_single_element_divisible(self):
        nums = [10]
        k = 5
        self.assertEqual(count_subarrays_divisible(nums, k), 1)

    def test_all_zeros(self):
        # For 5 zeros, any non-empty subarray sum is 0 (divisible by 3).
        # Total subarrays: 5 * 6 // 2 = 15.
        nums = [0, 0, 0, 0, 0]
        k = 3
        self.assertEqual(count_subarrays_divisible(nums, k), 15)

    def test_negative_numbers_only(self):
        # [-5, -10, -15], k = 5
        # Subarrays: [-5], [-10], [-15], [-5, -10], [-10, -15], [-5, -10, -15]
        # All 6 are divisible by 5.
        nums = [-5, -10, -15]
        k = 5
        self.assertEqual(count_subarrays_divisible(nums, k), 6)

    def test_mixed_remainders_with_negatives(self):
        # Subarrays: [-1, 2, 9] with k = 2
        # Sums:
        # [-1] -> -1 (not div)
        # [-1, 2] -> 1 (not div)
        # [-1, 2, 9] -> 10 (div)
        # [2] -> 2 (div)
        # [2, 9] -> 11 (not div)
        # [9] -> 9 (not div)
        # Total = 2
        nums = [-1, 2, 9]
        k = 2
        self.assertEqual(count_subarrays_divisible(nums, k), 2)

    def test_large_input_efficiency(self):
        # 30000 elements, ensuring an O(n) solution runs under 100ms and doesn't timeout
        rng = random.Random(1337)
        nums = [rng.randint(-1000, 1000) for _ in range(30000)]
        k = 137
        
        # Just assert it finishes execution and produces an integer >= 0
        result = count_subarrays_divisible(nums, k)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)

    def test_correctness_against_brute_force_slice(self):
        # Verify against ground-truth brute force on a modest deterministic array
        rng = random.Random(42)
        nums = [rng.randint(-50, 50) for _ in range(200)]
        k = 7
        
        # Ground-truth O(n^2) brute force
        expected = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum % k == 0:
                    expected += 1
                    
        self.assertEqual(count_subarrays_divisible(nums, k), expected)
