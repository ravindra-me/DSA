# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_01 import min_eating_speed  # noqa: E402
# ---- End of generated header ----

import math
import random

class TestMinEatingSpeed(TestCase):
    def test_example_1(self):
        self.assertEqual(min_eating_speed([3, 6, 7, 11], 8), 4)

    def test_example_2(self):
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 5), 30)

    def test_example_3(self):
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 6), 23)

    def test_single_pile(self):
        self.assertEqual(min_eating_speed([100], 3), 34)
        self.assertEqual(min_eating_speed([100], 100), 1)

    def test_identical_piles(self):
        self.assertEqual(min_eating_speed([10, 10, 10, 10], 4), 10)
        self.assertEqual(min_eating_speed([10, 10, 10, 10], 8), 5)

    def test_minimum_speed_is_one(self):
        # When h is substantially larger than total bananas, speed 1 is enough
        self.assertEqual(min_eating_speed([1, 1, 1], 10), 1)

    def test_large_constraints(self):
        # Max value piles with tight and loose hours
        piles = [10**9] * 5
        self.assertEqual(min_eating_speed(piles, 5), 10**9)
        self.assertEqual(min_eating_speed(piles, 10), 5 * 10**8)

    def test_deterministic_large_array(self):
        rng = random.Random(42)
        piles = [rng.randint(1, 10**6) for _ in range(10000)]
        h = 20000
        res = min_eating_speed(piles, h)
        # Verify that speed `res` finishes within h hours, and `res - 1` does not
        hours_at_res = sum((p + res - 1) // res for p in piles)
        self.assertLessEqual(hours_at_res, h)
        if res > 1:
            hours_below = sum((p + (res - 1) - 1) // (res - 1) for p in piles)
            self.assertGreater(hours_below, h)
