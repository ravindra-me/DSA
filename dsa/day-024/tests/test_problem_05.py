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
from problem_05 import subarrays_with_k_distinct  # noqa: E402
# ---- End of generated header ----

import unittest
import random

class TestSubarraysWithKDistinct(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(subarrays_with_k_distinct([1, 2, 1, 2, 3], 2), 7)

    def test_example_2(self):
        self.assertEqual(subarrays_with_k_distinct([1, 2, 1, 3, 4], 3), 3)

    def test_single_element_k1(self):
        self.assertEqual(subarrays_with_k_distinct([1], 1), 1)

    def test_single_element_k_greater(self):
        self.assertEqual(subarrays_with_k_distinct([1], 2), 0)

    def test_all_identical_elements(self):
        # [1, 1, 1, 1] has 4 subarrays of all 1s (k=1)
        # len=1: 4, len=2: 3, len=3: 2, len=4: 1 -> total 10
        self.assertEqual(subarrays_with_k_distinct([1, 1, 1, 1], 1), 10)
        self.assertEqual(subarrays_with_k_distinct([1, 1, 1, 1], 2), 0)

    def test_k_equals_array_length_all_unique(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(subarrays_with_k_distinct(nums, 5), 1)
        self.assertEqual(subarrays_with_k_distinct(nums, 1), 5)

    def test_large_input_performance(self):
        # Deterministic generation of large input
        rng = random.Random(42)
        nums = [rng.randint(1, 10) for _ in range(20000)]
        k = 5
        
        # Simple verifier using the same reduction to verify result deterministic logic
        def reference_at_most(k_val):
            if k_val <= 0:
                return 0
            counts = {}
            left = 0
            res = 0
            for right in range(len(nums)):
                counts[nums[right]] = counts.get(nums[right], 0) + 1
                while len(counts) > k_val:
                    counts[nums[left]] -= 1
                    if counts[nums[left]] == 0:
                        del counts[nums[left]]
                    left += 1
                res += (right - left + 1)
            return res

        expected = reference_at_most(k) - reference_at_most(k - 1)
        self.assertEqual(subarrays_with_k_distinct(nums, k), expected)
