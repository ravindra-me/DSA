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
from problem_01 import max_min_spread  # noqa: E402
# ---- End of generated header ----

import random


class TestSlidingWindowMaxMinSpread(TestCase):
    def test_example_1(self) -> None:
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [4, 6, 8, 8, 3, 4]
        self.assertEqual(max_min_spread(nums, k), expected)

    def test_example_2_identical_elements(self) -> None:
        nums = [4, 4, 4, 4]
        k = 2
        expected = [0, 0, 0]
        self.assertEqual(max_min_spread(nums, k), expected)

    def test_single_element_array(self) -> None:
        self.assertEqual(max_min_spread([42], 1), [0])

    def test_window_size_one(self) -> None:
        nums = [10, -5, 20, 0, 99]
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(max_min_spread(nums, 1), expected)

    def test_window_size_equals_array_length(self) -> None:
        nums = [7, 2, 9, -4, 5]
        expected = [9 - (-4)]  # 13
        self.assertEqual(max_min_spread(nums, len(nums)), expected)

    def test_monotonic_sequences(self) -> None:
        # Strictly increasing
        inc = [1, 2, 3, 4, 5]
        self.assertEqual(max_min_spread(inc, 3), [2, 2, 2])

        # Strictly decreasing
        dec = [5, 4, 3, 2, 1]
        self.assertEqual(max_min_spread(dec, 3), [2, 2, 2])

    def test_negative_and_extreme_values(self) -> None:
        nums = [-10**9, 10**9, -10**9, 0]
        k = 2
        expected = [2 * 10**9, 2 * 10**9, 10**9]
        self.assertEqual(max_min_spread(nums, k), expected)

    def test_large_input_performance(self) -> None:
        rng = random.Random(1337)
        n = 50_000
        k = 1_000
        nums = [rng.randint(-1_000_000, 1_000_000) for _ in range(n)]
        result = max_min_spread(nums, k)
        self.assertEqual(len(result), n - k + 1)

        # Spot check deterministic windows against naive slices
        sample_indices = [0, 100, 25_000, n - k]
        for idx in sample_indices:
            window = nums[idx : idx + k]
            expected_spread = max(window) - min(window)
            self.assertEqual(result[idx], expected_spread)
