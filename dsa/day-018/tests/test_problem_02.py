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
from problem_02 import intersection  # noqa: E402
# ---- End of generated header ----

import random


class TestIntersection(TestCase):
    def test_examples(self):
        self.assertEqual(intersection([1, 2, 2, 1], [2, 2]), [2])
        self.assertEqual(intersection([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
        self.assertEqual(intersection([1, 3, 5], [2, 4, 6]), [])

    def test_single_element_cases(self):
        self.assertEqual(intersection([1], [1]), [1])
        self.assertEqual(intersection([1], [2]), [])

    def test_boundary_values(self):
        self.assertEqual(intersection([0, 1000], [1000, 0]), [0, 1000])
        self.assertEqual(intersection([0], [1000]), [])

    def test_identical_large_repetition(self):
        self.assertEqual(intersection([7] * 100, [7] * 50), [7])

    def test_disjoint_lists(self):
        nums1 = list(range(0, 500))
        nums2 = list(range(500, 1000))
        self.assertEqual(intersection(nums1, nums2), [])

    def test_subsets(self):
        nums1 = [1, 2, 3, 4, 5, 6]
        nums2 = [2, 4, 6]
        self.assertEqual(intersection(nums1, nums2), [2, 4, 6])

    def test_large_random_input(self):
        rng = random.Random(42)
        nums1 = [rng.randint(0, 1000) for _ in range(10000)]
        nums2 = [rng.randint(0, 1000) for _ in range(10000)]
        
        expected = sorted(list(set(nums1) & set(nums2)))
        self.assertEqual(intersection(nums1, nums2), expected)
