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
from problem_02 import remove_duplicates_at_most_two  # noqa: E402
# ---- End of generated header ----

import random
from collections import Counter


class TestRemoveDuplicatesAtMostTwo(TestCase):
    def test_example_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = remove_duplicates_at_most_two(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 1, 2, 2, 3])

    def test_example_2(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        k = remove_duplicates_at_most_two(nums)
        self.assertEqual(k, 7)
        self.assertEqual(nums[:k], [0, 0, 1, 1, 2, 3, 3])

    def test_single_element_and_pairs(self):
        nums = [1]
        k = remove_duplicates_at_most_two(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])

        nums = [1, 1]
        k = remove_duplicates_at_most_two(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 1])

    def test_all_identical_elements(self):
        nums = [5, 5, 5, 5, 5, 5]
        k = remove_duplicates_at_most_two(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [5, 5])

    def test_no_duplicates(self):
        nums = [-5, -2, 0, 3, 7]
        k = remove_duplicates_at_most_two(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [-5, -2, 0, 3, 7])

    def test_negative_and_zero_values(self):
        nums = [-10, -10, -10, -5, 0, 0, 0, 2]
        k = remove_duplicates_at_most_two(nums)
        self.assertEqual(k, 6)
        self.assertEqual(nums[:k], [-10, -10, -5, 0, 0, 2])

    def test_large_input(self):
        rng = random.Random(42)
        raw = sorted(rng.choices(range(-500, 501), k=30000))
        nums = list(raw)

        expected = []
        counts = Counter()
        for val in raw:
            if counts[val] < 2:
                expected.append(val)
                counts[val] += 1

        k = remove_duplicates_at_most_two(nums)
        self.assertEqual(k, len(expected))
        self.assertEqual(nums[:k], expected)
