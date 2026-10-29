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
from problem_04 import count_circular_primes  # noqa: E402
# ---- End of generated header ----

class TestCircularPrimes(TestCase):
    def test_limit_below_or_equal_to_two(self):
        self.assertEqual(count_circular_primes(2), 0)
        self.assertEqual(count_circular_primes(1), 0)
        self.assertEqual(count_circular_primes(0), 0)

    def test_single_digit_primes(self):
        # Strictly less than 3: [2] -> 1
        self.assertEqual(count_circular_primes(3), 1)
        # Strictly less than 10: [2, 3, 5, 7] -> 4
        self.assertEqual(count_circular_primes(10), 4)

    def test_example_limit_100(self):
        # 13 circular primes: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97
        self.assertEqual(count_circular_primes(100), 13)

    def test_boundary_values(self):
        # Primes near 100: 97 is circular. At limit=97, 97 is excluded; at 98, 97 is included.
        self.assertEqual(count_circular_primes(97), 12)
        self.assertEqual(count_circular_primes(98), 13)

    def test_intermediate_limits(self):
        # Known count below 1000 is 25 (Project Euler 35 sub-result)
        # Circular primes under 1000: 13 (under 100) + 12 (100-999: 113, 131, 197, 311, 337, 373, 719, 733, 797, 919, 971, 991)
        self.assertEqual(count_circular_primes(1000), 25)

    def test_large_limit_1000000(self):
        # Standard Project Euler problem 35 solution below 1,000,000 is 55.
        self.assertEqual(count_circular_primes(1000000), 55)
