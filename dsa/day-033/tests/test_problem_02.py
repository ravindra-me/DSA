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
from problem_02 import stable_merge_sort  # noqa: E402
# ---- End of generated header ----

import random

class TestStableMergeSort(TestCase):
    def test_example_1(self):
        records = [(4, 0), (2, 1), (2, 2), (1, 3)]
        expected = [(1, 3), (2, 1), (2, 2), (4, 0)]
        self.assertEqual(stable_merge_sort(records), expected)

    def test_example_empty(self):
        self.assertEqual(stable_merge_sort([]), [])

    def test_example_all_identical_keys(self):
        records = [(5, 0), (5, 1), (5, 2)]
        expected = [(5, 0), (5, 1), (5, 2)]
        self.assertEqual(stable_merge_sort(records), expected)

    def test_single_element(self):
        records = [(42, 0)]
        self.assertEqual(stable_merge_sort(records), [(42, 0)])

    def test_negative_and_zero_keys(self):
        records = [(0, 0), (-5, 1), (3, 2), (-5, 3), (0, 4)]
        expected = [(-5, 1), (-5, 3), (0, 0), (0, 4), (3, 2)]
        self.assertEqual(stable_merge_sort(records), expected)

    def test_already_sorted_and_reverse_sorted(self):
        sorted_records = [(1, 0), (2, 1), (3, 2), (4, 3)]
        self.assertEqual(stable_merge_sort(sorted_records), sorted_records)

        reversed_records = [(4, 0), (3, 1), (2, 2), (1, 3)]
        expected = [(1, 3), (2, 2), (3, 1), (4, 0)]
        self.assertEqual(stable_merge_sort(reversed_records), expected)

    def test_large_random_input_stability(self):
        rng = random.Random(1337)
        n = 5000
        # Generate keys in a small range [1, 20] to force abundant duplicates and ties
        records = [(rng.randint(1, 20), i) for i in range(n)]

        # Built-in sorted with key=lambda x: x[0] is guaranteed stable by Python specification
        expected = sorted(records, key=lambda item: item[0])
        result = stable_merge_sort(records)

        self.assertEqual(result, expected)
