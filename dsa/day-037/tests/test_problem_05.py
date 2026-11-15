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
from problem_05 import maximum_gap  # noqa: E402
# ---- End of generated header ----

import random

class TestMaximumGap(TestCase):
    def test_examples(self) -> None:
        self.assertEqual(maximum_gap([3, 6, 9, 1]), 3)
        self.assertEqual(maximum_gap([10]), 0)
        self.assertEqual(maximum_gap([1, 1, 1, 1]), 0)

    def test_empty_and_single_element(self) -> None:
        self.assertEqual(maximum_gap([]), 0)
        self.assertEqual(maximum_gap([42]), 0)

    def test_two_elements(self) -> None:
        self.assertEqual(maximum_gap([1, 100]), 99)
        self.assertEqual(maximum_gap([5, 5]), 0)
        self.assertEqual(maximum_gap([1000, 2]), 998)

    def test_all_identical_or_duplicates(self) -> None:
        self.assertEqual(maximum_gap([7, 7, 7, 7, 7]), 0)
        self.assertEqual(maximum_gap([2, 2, 8, 8, 2]), 6)
        self.assertEqual(maximum_gap([1, 3, 3, 3, 5]), 2)

    def test_consecutive_integers(self) -> None:
        nums = list(range(100))
        random.Random(1337).shuffle(nums)
        self.assertEqual(maximum_gap(nums), 1)

    def test_boundary_values(self) -> None:
        self.assertEqual(maximum_gap([0, 10**9]), 10**9)
        self.assertEqual(maximum_gap([0, 10**9, 5 * 10**8]), 5 * 10**8)

    def test_large_random_input(self) -> None:
        rng = random.Random(42)
        nums = [rng.randint(0, 10**9) for _ in range(50000)]
        # Compute ground truth via sorted differences
        sorted_nums = sorted(nums)
        expected = max(b - a for a, b in zip(sorted_nums, sorted_nums[1:]))
        self.assertEqual(maximum_gap(nums), expected)
