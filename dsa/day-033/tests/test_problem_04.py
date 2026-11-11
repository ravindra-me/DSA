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
from problem_04 import count_inversions  # noqa: E402
# ---- End of generated header ----

import random


class TestCountInversions(TestCase):
    def test_examples(self):
        self.assertEqual(count_inversions([8, 4, 2, 1]), 6)
        self.assertEqual(count_inversions([1, 2, 3, 4, 5]), 0)
        self.assertEqual(count_inversions([]), 0)

    def test_empty_and_single_element(self):
        self.assertEqual(count_inversions([]), 0)
        self.assertEqual(count_inversions([42]), 0)

    def test_two_elements(self):
        self.assertEqual(count_inversions([1, 2]), 0)
        self.assertEqual(count_inversions([2, 1]), 1)

    def test_duplicates(self):
        self.assertEqual(count_inversions([2, 2, 2, 2]), 0)
        self.assertEqual(count_inversions([3, 1, 2, 2, 1]), 6)

    def test_negative_numbers_and_zeros(self):
        self.assertEqual(count_inversions([-5, -1, 0, 2, -3]), 3)
        self.assertEqual(count_inversions([0, -1, 0, -2]), 4)

    def test_strictly_descending(self):
        n = 100
        descending = list(range(n, 0, -1))
        expected = n * (n - 1) // 2
        self.assertEqual(count_inversions(descending), expected)

    def test_large_random_input(self):
        rng = random.Random(42)
        n = 20000
        nums = [rng.randint(-10**9, 10**9) for _ in range(n)]
        result = count_inversions(nums)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)

    def test_matches_brute_force_on_random_slices(self):
        rng = random.Random(1337)
        for _ in range(10):
            nums = [rng.randint(-100, 100) for _ in range(60)]
            brute_force_count = sum(
                1 for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] > nums[j]
            )
            self.assertEqual(count_inversions(nums), brute_force_count)

    def test_immutability_of_input(self):
        original = [5, 4, 3, 2, 1]
        input_copy = list(original)
        count_inversions(original)
        self.assertEqual(original, input_copy)
