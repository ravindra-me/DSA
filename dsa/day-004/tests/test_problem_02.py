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
from problem_02 import power  # noqa: E402
# ---- End of generated header ----

class TestPowerFunction(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(power(2, 10), 1024)

    def test_example_2(self):
        self.assertEqual(power(5, 0), 1)

    def test_base_zero(self):
        # 0^5 = 0
        self.assertEqual(power(0, 5), 0)

    def test_base_one(self):
        # 1^100 = 1
        self.assertEqual(power(1, 100), 1)

    def test_negative_base(self):
        # (-2)^3 = -8
        self.assertEqual(power(-2, 3), -8)
        # (-2)^4 = 16
        self.assertEqual(power(-2, 4), 16)

    def test_large_input(self):
        # 3^12 is 531441
        self.assertEqual(power(3, 12), 531441)

    def test_odd_exponent(self):
        # 2^5 = 32
        self.assertEqual(power(2, 5), 32)
