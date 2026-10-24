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
from problem_03 import max_sliding_window  # noqa: E402
# ---- End of generated header ----

import random


class TestSlidingWindowMaximum(TestCase):
    def test_examples(self) -> None:
        self.assertEqual(
            max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3),
            [3, 3, 5, 5, 6, 7],
        )
        self.assertEqual(max_sliding_window([1], 1), [1])
        self.assertEqual(max_sliding_window([9, 8, 7, 6], 2), [9, 8, 7])

    def test_k_equals_one(self) -> None:
        nums = [5, -2, 7, 0, -8, 12]
        self.assertEqual(max_sliding_window(nums, 1), nums)

    def test_k_equals_length(self) -> None:
        nums = [4, 2, 8, 1, 9, 3]
        self.assertEqual(max_sliding_window(nums, len(nums)), [9])

    def test_identical_elements(self) -> None:
        nums = [7] * 5
        self.assertEqual(max_sliding_window(nums, 3), [7, 7, 7])

    def test_strictly_increasing_and_decreasing(self) -> None:
        inc = [1, 2, 3, 4, 5]
        self.assertEqual(max_sliding_window(inc, 3), [3, 4, 5])

        dec = [5, 4, 3, 2, 1]
        self.assertEqual(max_sliding_window(dec, 3), [5, 4, 3])

    def test_all_negative_numbers(self) -> None:
        nums = [-10, -50, -5, -20, -1, -30]
        self.assertEqual(max_sliding_window(nums, 3), [-5, -5, -1, -1])

    def test_large_input_performance(self) -> None:
        rng = random.Random(1337)
        n = 50_000
        k = 500
        nums = [rng.randint(-10_000, 10_000) for _ in range(n)]

        result = max_sliding_window(nums, k)
        self.assertEqual(len(result), n - k + 1)

        # Spot check specific windows against brute force
        check_indices = [0, 100, 1_000, 10_000, 25_000, n - k]
        for idx in check_indices:
            expected = max(nums[idx : idx + k])
            self.assertEqual(result[idx], expected)
