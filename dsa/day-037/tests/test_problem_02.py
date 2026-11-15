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
from problem_02 import stable_sort_scores  # noqa: E402
# ---- End of generated header ----

import random

class TestStableSortScores(TestCase):
    def test_example_1(self):
        records = [("Alice", 85), ("Bob", 70), ("Charlie", 85), ("Dave", 90)]
        expected = [("Bob", 70), ("Alice", 85), ("Charlie", 85), ("Dave", 90)]
        self.assertEqual(stable_sort_scores(records), expected)

    def test_empty(self):
        self.assertEqual(stable_sort_scores([]), [])

    def test_single_element(self):
        records = [("Solo", 42)]
        self.assertEqual(stable_sort_scores(records), [("Solo", 42)])

    def test_boundary_scores_min_and_max(self):
        records = [("Max", 100), ("Min1", 0), ("Mid", 50), ("Min2", 0)]
        expected = [("Min1", 0), ("Min2", 0), ("Mid", 50), ("Max", 100)]
        self.assertEqual(stable_sort_scores(records), expected)

    def test_all_identical_scores_preserves_order(self):
        records = [(f"id_{i}", 80) for i in range(10)]
        self.assertEqual(stable_sort_scores(records), records)

    def test_already_sorted_and_reversed(self):
        sorted_records = [("a", 10), ("b", 20), ("c", 30)]
        self.assertEqual(stable_sort_scores(sorted_records), sorted_records)

        reversed_records = [("c", 30), ("b", 20), ("a", 10)]
        self.assertEqual(stable_sort_scores(reversed_records), [("a", 10), ("b", 20), ("c", 30)])

    def test_large_input_stability(self):
        rng = random.Random(42)
        n = 50_000
        records = [(f"usr_{i}", rng.randint(0, 100)) for i in range(n)]
        # Python's built-in sort is guaranteed stable Timsort, serving as ground truth reference
        expected = sorted(records, key=lambda item: item[1])
        result = stable_sort_scores(records)
        self.assertEqual(result, expected)
