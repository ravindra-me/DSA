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
from problem_04 import find_nth_root  # noqa: E402
# ---- End of generated header ----

import math
import random


class TestFindNthRoot(TestCase):
    def test_examples(self):
        res1 = find_nth_root(27.0, 3)
        self.assertAlmostEqual(res1, 3.0, places=6)
        self.assertAlmostEqual(res1**3, 27.0, places=5)

        res2 = find_nth_root(0.25, 2)
        self.assertAlmostEqual(res2, 0.5, places=6)
        self.assertAlmostEqual(res2**2, 0.25, places=5)

    def test_p_equals_one(self):
        for val in [0.001, 1.0, 42.5, 100000.0]:
            self.assertAlmostEqual(find_nth_root(val, 1), val, places=6)

    def test_small_n_less_than_one(self):
        n = 1e-6
        p = 2
        expected = math.sqrt(n)
        res = find_nth_root(n, p)
        self.assertAlmostEqual(res, expected, places=6)
        self.assertAlmostEqual(res**p, n, places=6)

    def test_large_n_and_large_p(self):
        n = 1e9
        p = 30
        expected = n ** (1.0 / 30)
        res = find_nth_root(n, p)
        self.assertAlmostEqual(res, expected, places=6)

    def test_unit_value(self):
        for p in [1, 2, 5, 20]:
            res = find_nth_root(1.0, p)
            self.assertAlmostEqual(res, 1.0, places=6)

    def test_deterministic_random_cases(self):
        rng = random.Random(42)
        for _ in range(50):
            p = rng.randint(1, 20)
            # Test both < 1 and > 1 ranges
            if rng.random() < 0.5:
                n = rng.uniform(1e-5, 0.999)
            else:
                n = rng.uniform(1.001, 1e6)
            expected = n ** (1.0 / p)
            res = find_nth_root(n, p)
            self.assertTrue(
                abs(res - expected) < 1e-6 or abs(res**p - n) < 1e-5,
                f"Failed for n={n}, p={p}: got {res}, expected {expected}"
            )
