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
from problem_05 import batch_combinations_modulo  # noqa: E402
# ---- End of generated header ----

import math
import random

class TestBatchCombinationsModulo(TestCase):
    def test_examples(self):
        self.assertEqual(batch_combinations_modulo([5, 3, 10], [2, 5, 0]), [10, 0, 1])
        self.assertEqual(batch_combinations_modulo([0], [0]), [1])

    def test_single_element_cases(self):
        self.assertEqual(batch_combinations_modulo([10], [10]), [1])
        self.assertEqual(batch_combinations_modulo([10], [1]), [10])
        self.assertEqual(batch_combinations_modulo([10], [11]), [0])

    def test_symmetry_property(self):
        n_vals = [20, 20, 50, 50]
        k_vals = [6, 14, 15, 35]
        res = batch_combinations_modulo(n_vals, k_vals)
        self.assertEqual(res[0], res[1])
        self.assertEqual(res[2], res[3])

    def test_pascal_recurrence(self):
        # C(n, k) = C(n-1, k-1) + C(n-1, k) mod P
        mod = 10**9 + 7
        queries_n = [100, 99, 99]
        queries_k = [40, 39, 40]
        ans = batch_combinations_modulo(queries_n, queries_k)
        self.assertEqual(ans[0], (ans[1] + ans[2]) % mod)

    def test_exact_values_against_math_comb(self):
        mod = 10**9 + 7
        n_list = [10, 15, 20, 25, 30]
        k_list = [3, 7, 10, 12, 15]
        expected = [math.comb(n, k) % mod for n, k in zip(n_list, k_list)]
        self.assertEqual(batch_combinations_modulo(n_list, k_list), expected)

    def test_large_input_performance(self):
        rng = random.Random(42)
        q = 100_000
        # Generate 100k queries with n up to 200,000
        n_vals = [rng.randint(0, 200_000) for _ in range(q)]
        k_vals = [rng.randint(0, n_vals[i] + 5) for i in range(q)]

        res = batch_combinations_modulo(n_vals, k_vals)
        self.assertEqual(len(res), q)
        for i in range(10):
            idx = rng.randint(0, q - 1)
            n, k = n_vals[idx], k_vals[idx]
            if k < 0 or k > n:
                self.assertEqual(res[idx], 0)
            else:
                self.assertEqual(res[idx], math.comb(n, k) % (10**9 + 7))
