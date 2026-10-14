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
from problem_01 import reverse_integer  # noqa: E402
# ---- End of generated header ----

class TestReverseInteger(TestCase):
    def test_examples(self) -> None:
        self.assertEqual(reverse_integer(123), 321)
        self.assertEqual(reverse_integer(-120), -21)
        self.assertEqual(reverse_integer(1534236469), 0)

    def test_zero(self) -> None:
        self.assertEqual(reverse_integer(0), 0)

    def test_single_digits(self) -> None:
        for d in range(-9, 10):
            self.assertEqual(reverse_integer(d), d)

    def test_negative_cases(self) -> None:
        self.assertEqual(reverse_integer(-123), -321)
        self.assertEqual(reverse_integer(-1), -1)
        self.assertEqual(reverse_integer(-1000), -1)

    def test_boundary_overflow(self) -> None:
        self.assertEqual(reverse_integer(2**31 - 1), 0)
        self.assertEqual(reverse_integer(-(2**31)), 0)
        self.assertEqual(reverse_integer(1000000003), 0)
        self.assertEqual(reverse_integer(-1000000003), 0)

    def test_trailing_zeros(self) -> None:
        self.assertEqual(reverse_integer(12000), 21)
        self.assertEqual(reverse_integer(-900), -9)

    def test_bulk_valid_reversals(self) -> None:
        import random
        rng = random.Random(42)
        for _ in range(500):
            val = rng.randint(10, 100_000)
            expected = int(str(val)[::-1])
            self.assertEqual(reverse_integer(val), expected)
            self.assertEqual(reverse_integer(-val), -expected)
