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
from problem_02 import calculate_basic_expression  # noqa: E402
# ---- End of generated header ----

class TestCalculateBasicExpression(TestCase):
    def test_simple_addition(self):
        self.assertEqual(calculate_basic_expression("1 + 1"), 2)

    def test_nested_parentheses(self):
        self.assertEqual(calculate_basic_expression("(1+(4+5+2)-3)+(6+8)"), 23)

    def test_spaces_and_subtraction(self):
        self.assertEqual(calculate_basic_expression(" 2-1 + 2 "), 3)

    def test_unary_minus_and_nested(self):
        self.assertEqual(calculate_basic_expression("- (3 + (2 - 1))"), -4)

    def test_zero_and_multiple_digits(self):
        self.assertEqual(calculate_basic_expression("100 - (20 + 30)"), 50)

    def test_deeply_nested(self):
        # Constructs (((...((1)...))) + 1)
        depth = 500
        expr = "(" * depth + "1" + ")" * depth + " + 2"
        self.assertEqual(calculate_basic_expression(expr), 3)

    def test_large_input_performance(self):
        # Creates a long linear expression: 1 + 2 - 1 + 2 ...
        parts = []
        expected = 0
        for i in range(100000):
            if i % 2 == 0:
                parts.append(" + 5")
                expected += 5
            else:
                parts.append(" - 3")
                expected -= 3
        expr = "0" + "".join(parts)
        self.assertEqual(calculate_basic_expression(expr), expected)
