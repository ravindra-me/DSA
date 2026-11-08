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
from problem_02 import max_distance  # noqa: E402
# ---- End of generated header ----

import random


class TestMagneticForce(TestCase):
    def test_example_1(self):
        position = [1, 2, 3, 4, 7]
        m = 3
        self.assertEqual(max_distance(position, m), 3)

    def test_example_2(self):
        position = [5, 4, 3, 2, 1, 1000000000]
        m = 2
        self.assertEqual(max_distance(position, m), 999999999)

    def test_minimum_m_two_balls(self):
        position = [10, 100]
        m = 2
        self.assertEqual(max_distance(position, m), 90)

    def test_all_baskets_occupied(self):
        # m == len(position): answer is the min distance between consecutive sorted items
        position = [1, 5, 8, 12, 20]
        m = 5
        # Differences: 5-1=4, 8-5=3, 12-8=4, 20-12=8 -> min is 3
        self.assertEqual(max_distance(position, m), 3)

    def test_equally_spaced_baskets(self):
        position = [2, 4, 6, 8, 10, 12]
        m = 3
        # Best placement: 2, 6, 10 or 2, 6, 12 etc. Min distance 4 is possible (2, 6, 10).
        # Can we do 5? 2, 8, ... distance >= 5: 2, 8 (diff 6), next would be >= 13 (none). Max = 4.
        # Wait: 2, 7 -> not there. If d = 5: 2 -> next is >= 7: 8. next >= 13: None -> only 2 balls.
        # So max distance is indeed 4.
        self.assertEqual(max_distance(position, m), 4)

    def test_large_input_performance(self):
        # 100,000 positions with arithmetic sequence spaced by 10
        # max distance for m = 10000 should be exactly 10 * floor((n - 1) / (m - 1))
        n = 100000
        step = 10
        rng = random.Random(42)
        position = [i * step for i in range(n)]
        rng.shuffle(position)
        m = 10000
        expected = ((n - 1) // (m - 1)) * step
        self.assertEqual(max_distance(position, m), expected)
