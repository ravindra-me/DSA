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
from problem_04 import bucket_sort  # noqa: E402
# ---- End of generated header ----

import random


class TestBucketSort(TestCase):
    def test_empty_list(self):
        self.assertEqual(bucket_sort([]), [])

    def test_single_element(self):
        self.assertEqual(bucket_sort([0.42]), [0.42])

    def test_example_case(self):
        nums = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
        expected = [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]
        self.assertEqual(bucket_sort(nums), expected)

    def test_already_sorted_and_reversed(self):
        sorted_nums = [0.1, 0.2, 0.3, 0.4, 0.5]
        self.assertEqual(bucket_sort(sorted_nums), sorted_nums)
        reversed_nums = [0.5, 0.4, 0.3, 0.2, 0.1]
        self.assertEqual(bucket_sort(reversed_nums), sorted_nums)

    def test_duplicates_and_boundary_zero(self):
        nums = [0.0, 0.5, 0.0, 0.75, 0.5, 0.25, 0.0]
        expected = sorted(nums)
        self.assertEqual(bucket_sort(nums), expected)

    def test_all_identical_elements(self):
        nums = [0.73] * 10
        self.assertEqual(bucket_sort(nums), [0.73] * 10)

    def test_large_uniform_distribution(self):
        rng = random.Random(42)
        n = 10000
        nums = [rng.random() for _ in range(n)]
        expected = sorted(nums)
        result = bucket_sort(nums)
        self.assertEqual(result, expected)
