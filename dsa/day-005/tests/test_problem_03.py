# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_03.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_03 import count_distinct_prime_factors  # noqa: E402
# ---- End of generated header ----

import random
import unittest


class TestPrimeFactorCountingQueries(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            count_distinct_prime_factors(20, [12, 15, 16, 7]),
            [2, 2, 1, 1],
        )
        self.assertEqual(
            count_distinct_prime_factors(10, [2, 6, 10]),
            [1, 2, 2],
        )

    def test_minimal_n_and_single_query(self):
        self.assertEqual(count_distinct_prime_factors(2, [2]), [1])

    def test_prime_numbers_and_prime_powers(self):
        # 2 is prime -> 1
        # 8 = 2^3 -> 1
        # 27 = 3^3 -> 1
        # 31 is prime -> 1
        # 30 = 2 * 3 * 5 -> 3
        queries = [2, 8, 27, 31, 30]
        expected = [1, 1, 1, 1, 3]
        self.assertEqual(count_distinct_prime_factors(31, queries), expected)

    def test_duplicates(self):
        queries = [12, 12, 12, 18, 18]
        # 12 -> {2, 3} (2), 18 -> {2, 3} (2)
        self.assertEqual(count_distinct_prime_factors(20, queries), [2, 2, 2, 2, 2])

    def test_highly_composite_and_boundary_values(self):
        # Product of first primes: 2*3*5*7 = 210 (4 distinct)
        # 2*3*5*7*11 = 2310 (5 distinct)
        n = 2500
        queries = [210, 2310, n]
        # 2500 = 2^2 * 5^4 (2 distinct)
        self.assertEqual(count_distinct_prime_factors(n, queries), [4, 5, 2])

    def test_large_number_of_queries(self):
        n = 100_000
        rng = random.Random(1337)
        queries = [rng.randint(2, n) for _ in range(20_000)]

        res = count_distinct_prime_factors(n, queries)
        self.assertEqual(len(res), len(queries))

        # Check first 50 results using independent trial division
        def trial_div_distinct(x: int) -> int:
            d = 2
            factors = set()
            while d * d <= x:
                if x % d == 0:
                    factors.add(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                factors.add(x)
            return len(factors)

        for i in range(50):
            self.assertEqual(res[i], trial_div_distinct(queries[i]))
