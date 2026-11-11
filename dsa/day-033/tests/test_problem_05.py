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
from problem_05 import external_k_way_sort  # noqa: E402
# ---- End of generated header ----

import random


class TestExternalKWaySort(TestCase):
    def test_examples(self):
        stream = [7, 1, 5, 2, 9, 3, 8, 4, 6]
        chunk_size = 3
        self.assertEqual(external_k_way_sort(stream, chunk_size), [1, 2, 3, 4, 5, 6, 7, 8, 9])

        self.assertEqual(external_k_way_sort([], 5), [])
        self.assertEqual(external_k_way_sort([42], 10), [42])

    def test_chunk_size_larger_than_stream(self):
        stream = [10, -1, 3, 2, 8]
        self.assertEqual(external_k_way_sort(stream, 100), [-1, 2, 3, 8, 10])

    def test_chunk_size_one(self):
        # Every element forms its own run (k = len(stream))
        stream = [5, 2, 8, 1, 9, 4]
        self.assertEqual(external_k_way_sort(stream, 1), [1, 2, 4, 5, 8, 9])

    def test_negative_numbers_and_duplicates(self):
        stream = [0, -5, 10, -5, 0, 2, -100, 50, 10]
        chunk_size = 4
        expected = sorted(stream)
        self.assertEqual(external_k_way_sort(stream, chunk_size), expected)

    def test_already_sorted_and_reverse_sorted(self):
        sorted_stream = list(range(1, 21))
        self.assertEqual(external_k_way_sort(sorted_stream, 4), sorted_stream)

        reversed_stream = list(range(20, 0, -1))
        self.assertEqual(external_k_way_sort(reversed_stream, 4), sorted_stream)

    def test_all_elements_identical(self):
        stream = [7] * 25
        self.assertEqual(external_k_way_sort(stream, 3), [7] * 25)

    def test_large_random_stream(self):
        rng = random.Random(1337)
        stream = [rng.randint(-10**9, 10**9) for _ in range(50000)]
        chunk_size = 1000
        expected = sorted(stream)
        result = external_k_way_sort(stream, chunk_size)
        self.assertEqual(result, expected)
