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
from problem_04 import geometric_sum_mod  # noqa: E402
# ---- End of generated header ----

class TestGeometricSumMod(TestCase):
    def test_examples(self):
        self.assertEqual(geometric_sum_mod(2, 3, 1000), 15)
        self.assertEqual(geometric_sum_mod(3, 0, 7), 1)
        # 1 + 5 + 25 + 125 + 625 = 781; 781 % 6 = 1
        self.assertEqual(geometric_sum_mod(5, 4, 6), 1)

    def test_edge_case_k_zero(self):
        for a in [0, 1, 5, 100]:
            for m in [2, 3, 10, 1000000007]:
                self.assertEqual(geometric_sum_mod(a, 0, m), 1 % m)

    def test_edge_case_a_zero(self):
        # 0^0 + 0^1 + ... = 1 + 0 + 0 = 1
        self.assertEqual(geometric_sum_mod(0, 1, 100), 1)
        self.assertEqual(geometric_sum_mod(0, 5, 13), 1)
        self.assertEqual(geometric_sum_mod(0, 10**9, 10**9 + 7), 1)

    def test_edge_case_a_one(self):
        # 1 + 1 + ... (k + 1 times) = (k + 1) % m
        k = 123456
        m = 10007
        self.assertEqual(geometric_sum_mod(1, k, m), (k + 1) % m)

    def test_small_values_against_brute_force(self):
        for a in range(6):
            for k in range(15):
                for m in [2, 3, 7, 11, 16]:
                    expected = sum(pow(a, i) for i in range(k + 1)) % m
                    actual = geometric_sum_mod(a, k, m)
                    self.assertEqual(actual, expected, f"Failed for a={a}, k={k}, m={m}")

    def test_composite_modulus_non_coprime(self):
        # Non-coprime case where modular inverse does not exist
        # a = 6, m = 10. gcd(a - 1, m) = gcd(5, 10) = 5
        expected = (1 + 6 + 36 + 216) % 10  # 259 % 10 = 9
        self.assertEqual(geometric_sum_mod(6, 3, 10), expected)

    def test_large_k_performance(self):
        # Naive O(k) would TLE on k = 10^9
        a = 123456789
        k = 10**9
        m = 10**9 + 7
        res = geometric_sum_mod(a, k, m)
        self.assertTrue(0 <= res < m)
