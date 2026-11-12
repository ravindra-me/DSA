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
from problem_04 import k_closest  # noqa: E402
# ---- End of generated header ----

import random
from unittest import TestCase

class TestKClosest(TestCase):
    def assert_points_equal_set(self, actual: list[list[int]], expected: list[list[int]]):
        actual_tuples = [tuple(p) for p in actual]
        expected_tuples = [tuple(p) for p in expected]
        self.assertEqual(sorted(actual_tuples), sorted(expected_tuples))

    def test_example_1(self):
        points = [[1, 3], [-2, 2]]
        k = 1
        expected = [[-2, 2]]
        self.assert_points_equal_set(k_closest(points, k), expected)

    def test_example_2(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        expected = [[3, 3], [-2, 4]]
        self.assert_points_equal_set(k_closest(points, k), expected)

    def test_k_equals_len(self):
        points = [[1, 1], [2, 2], [3, 3]]
        k = 3
        expected = [[1, 1], [2, 2], [3, 3]]
        self.assert_points_equal_set(k_closest(points, k), expected)

    def test_single_element(self):
        points = [[0, 0]]
        k = 1
        expected = [[0, 0]]
        self.assert_points_equal_set(k_closest(points, k), expected)

    def test_duplicate_distances(self):
        points = [[1, 0], [0, 1], [-1, 0], [0, -1], [2, 2]]
        k = 2
        res = k_closest(points, k)
        self.assertEqual(len(res), 2)
        for p in res:
            self.assertEqual(p[0]**2 + p[1]**2, 1)

    def test_large_input_performance(self):
        rng = random.Random(42)
        n = 50000
        k = 5000
        points = [[rng.randint(-10000, 10000), rng.randint(-10000, 10000)] for _ in range(n)]
        
        # Compute expected result using sorted baseline
        sorted_points = sorted(points, key=lambda p: p[0]**2 + p[1]**2)
        expected = sorted_points[:k]
        
        actual = k_closest(points, k)
        self.assert_points_equal_set(actual, expected)
