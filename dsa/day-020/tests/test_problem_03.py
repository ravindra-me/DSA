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
from problem_03 import largest_coprime_component  # noqa: E402
# ---- End of generated header ----

import random
from collections import Counter
import unittest


class TestLargestCoprimeComponent(unittest.TestCase):
    def test_example_1(self) -> None:
        nums = [4, 6, 15, 35]
        self.assertEqual(largest_coprime_component(nums), 4)

    def test_example_2(self) -> None:
        nums = [2, 3, 5, 7, 11]
        self.assertEqual(largest_coprime_component(nums), 1)

    def test_single_element(self) -> None:
        self.assertEqual(largest_coprime_component([1]), 1)
        self.assertEqual(largest_coprime_component([42]), 1)

    def test_all_ones(self) -> None:
        self.assertEqual(largest_coprime_component([1, 1, 1, 1]), 1)

    def test_duplicates(self) -> None:
        nums = [2, 2, 2, 3, 3, 5]
        # 2s form a component of size 3, 3s form size 2, 5 is 1
        self.assertEqual(largest_coprime_component(nums), 3)

    def test_mixed_components_and_ones(self) -> None:
        # [1, 1, 6, 10, 15, 7, 14]
        # 6 (2,3), 10 (2,5), 15 (3,5) -> {6, 10, 15} size 3
        # 7 (7), 14 (2,7) -> 14 shares 2 with 6/10, so {6, 10, 15, 7, 14} size 5
        # 1s remain isolated size 1
        nums = [1, 1, 6, 10, 15, 7, 14]
        self.assertEqual(largest_coprime_component(nums), 5)

    def test_large_input(self) -> None:
        # Deterministic generation: 20000 elements
        # Multiples of 2 and 3 connected, plus distinct primes
        rng = random.Random(42)
        # 10000 even numbers between 2 and 100000
        evens = [rng.randrange(2, 100001, 2) for _ in range(10000)]
        # 5000 odd multiples of 3
        mult3 = [rng.randrange(3, 100001, 6) for _ in range(5000)]
        # 1000 odd multiples of 6 (these connect evens and mult3)
        mult6 = [6 * rng.randint(1, 16666) for _ in range(1000)]
        # 4000 isolated 1s
        ones = [1] * 4000

        nums = evens + mult3 + mult6 + ones
        # evens + mult3 + mult6 are all connected via 2 and 3
        expected = 10000 + 5000 + 1000
        self.assertEqual(largest_coprime_component(nums), expected)
