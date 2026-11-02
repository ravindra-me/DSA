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
from problem_02 import min_sub_array_len  # noqa: E402
# ---- End of generated header ----

import random

class TestMinSubArrayLen(TestCase):
    def test_example_1(self):
        self.assertEqual(min_sub_array_len(7, [2, 3, 1, 2, 4, 3]), 2)

    def test_example_2(self):
        self.assertEqual(min_sub_array_len(100, [1, 2, 3, 4, 5]), 0)

    def test_exact_match_single_element(self):
        self.assertEqual(min_sub_array_len(4, [1, 4, 4]), 1)

    def test_single_element_less_than_target(self):
        self.assertEqual(min_sub_array_len(5, [3]), 0)

    def test_single_element_greater_or_equal_target(self):
        self.assertEqual(min_sub_array_len(3, [5]), 1)

    def test_entire_array_needed(self):
        self.assertEqual(min_sub_array_len(15, [1, 2, 3, 4, 5]), 5)

    def test_all_identical_elements(self):
        self.assertEqual(min_sub_array_len(11, [1, 1, 1, 1, 1, 1, 1, 1]), 0)
        self.assertEqual(min_sub_array_len(5, [2, 2, 2, 2]), 3)

    def test_large_input_linear_performance(self):
        rng = random.Random(42)
        n = 100_000
        nums = [rng.randint(1, 100) for _ in range(n)]
        target = 500
        
        # Expected answer computed by standard reference logic
        min_len = n + 1
        current_sum = 0
        left = 0
        for right in range(n):
            current_sum += nums[right]
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
        expected = min_len if min_len <= n else 0
        
        self.assertEqual(min_sub_array_len(target, nums), expected)
