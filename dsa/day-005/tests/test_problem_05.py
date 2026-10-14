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
from problem_05 import count_primes_in_range  # noqa: E402
# ---- End of generated header ----

class TestSegmentedSieve(TestCase):
    def test_example_1(self):
        self.assertEqual(count_primes_in_range(10, 20), 4)

    def test_example_2_single_composite_one(self):
        self.assertEqual(count_primes_in_range(1, 1), 0)

    def test_example_3_large_range(self):
        # There are 2,401 primes in [1000000000, 1000050000]
        self.assertEqual(count_primes_in_range(1000000000, 1000050000), 2401)

    def test_low_boundary_small_primes(self):
        # 1 to 10: primes are 2, 3, 5, 7 -> count = 4
        self.assertEqual(count_primes_in_range(1, 10), 4)
        # 2 to 2: prime 2 -> count = 1
        self.assertEqual(count_primes_in_range(2, 2), 1)
        # 4 to 4: composite -> count = 0
        self.assertEqual(count_primes_in_range(4, 4), 0)

    def test_range_with_no_primes(self):
        # [14, 16] contains 14, 15, 16; none are prime
        self.assertEqual(count_primes_in_range(14, 16), 0)

    def test_range_starting_at_prime(self):
        # [3, 7] -> 3, 5, 7 -> count = 3
        self.assertEqual(count_primes_in_range(3, 7), 3)

    def test_comparison_with_trial_division(self):
        def is_prime_ref(n: int) -> bool:
            if n < 2:
                return False
            if n in (2, 3):
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        low, high = 10000, 11000
        expected = sum(1 for x in range(low, high + 1) if is_prime_ref(x))
        self.assertEqual(count_primes_in_range(low, high), expected)

    def test_max_span_at_limit(self):
        # Maximum allowed span high - low = 10^5 near 10^9
        low = 999900000
        high = 1000000000
        res = count_primes_in_range(low, high)
        self.assertIsInstance(res, int)
        self.assertGreater(res, 0)
