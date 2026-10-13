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
from problem_05 import generate_parentheses  # noqa: E402
# ---- End of generated header ----

class TestGenerateParentheses(unittest.TestCase):
    def test_n_is_1(self):
        self.assertEqual(generate_parentheses(1), ["()"])

    def test_n_is_2(self):
        # Expected: (()), ()(), order doesn't technically matter but usually sorted
        result = generate_parentheses(2)
        self.assertCountEqual(result, ["(())", "()()"])

    def test_n_is_3(self):
        result = generate_parentheses(3)
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertCountEqual(result, expected)

    def test_n_is_0(self):
        # Constraint says 1 <= n <= 8, but robust code handles 0 or negative gracefully
        self.assertEqual(generate_parentheses(0), [])

    def test_n_is_max(self):
        # n=8 is max. Catalan(8) = 1430.
        result = generate_parentheses(8)
        self.assertEqual(len(result), 1430)
        # Verify structure: all must be valid
        for s in result:
            balance = 0
            for char in s:
                if char == '(':
                    balance += 1
                else:
                    balance -= 1
                self.assertGreaterEqual(balance, 0)
            self.assertEqual(balance, 0)

    def test_duplicates(self):
        # Ensure no duplicates in the output
        result = generate_parentheses(3)
        self.assertEqual(len(result), len(set(result)))

    def test_invalid_n(self):
        self.assertEqual(generate_parentheses(-5), [])
