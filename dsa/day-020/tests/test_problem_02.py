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
from problem_02 import kth_digit_geometric_product  # noqa: E402
# ---- End of generated header ----

class TestKthDigitGeometricProduct(TestCase):
    def test_example_1(self) -> None:
        # a = 2, r = 3, n = 3, k = 4 -> 2 * 6 * 18 = 216
        self.assertEqual(kth_digit_geometric_product(2, 3, 3, 4), 216)

    def test_example_2(self) -> None:
        # a = 10, r = 10, n = 1, k = 2 -> 10 % 100 = 10
        self.assertEqual(kth_digit_geometric_product(10, 10, 1, 2), 10)

    def test_single_term(self) -> None:
        # n = 1: product is just a
        a = 1234567
        r = 89
        k = 3
        self.assertEqual(kth_digit_geometric_product(a, r, 1, k), 1234567 % 1000)

    def test_two_terms(self) -> None:
        # n = 2: product is a * (a * r) = a^2 * r
        a = 7
        r = 5
        k = 3
        expected = (7 * 35) % 1000
        self.assertEqual(kth_digit_geometric_product(a, r, 2, k), expected)

    def test_ratio_is_one(self) -> None:
        # r = 1: terms are all a, product is a^n
        a = 3
        r = 1
        n = 5
        k = 4
        expected = (3**5) % 10000
        self.assertEqual(kth_digit_geometric_product(a, r, n, k), expected)

    def test_small_loop_verification(self) -> None:
        # Compare directly against iterative product for small n
        a = 13
        r = 7
        n = 6
        k = 5
        mod = 10**k
        curr = a
        prod = 1
        for _ in range(n):
            prod = (prod * curr) % mod
            curr = (curr * r) % mod
        self.assertEqual(kth_digit_geometric_product(a, r, n, k), prod)

    def test_large_n_performance(self) -> None:
        # Large n where naive O(n) would time out
        a = 10**9
        r = 10**9
        n = 10**9
        k = 9
        # a^n has factor 10^(9 * 10^9), so a^n % 10^9 == 0
        self.assertEqual(kth_digit_geometric_product(a, r, n, k), 0)

    def test_large_values_coprime_to_ten(self) -> None:
        # Using odd numbers not divisible by 5
        a = 987654321
        r = 123456789
        n = 1000000000
        k = 4
        mod = 10**4
        exp_r = n * (n - 1) // 2
        expected = (pow(a, n, mod) * pow(r, exp_r, mod)) % mod
        self.assertEqual(kth_digit_geometric_product(a, r, n, k), expected)
