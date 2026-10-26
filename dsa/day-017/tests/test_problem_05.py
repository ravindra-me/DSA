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
from problem_05 import parse_bool_expr  # noqa: E402
# ---- End of generated header ----

import unittest
import random

class TestParseBoolExpr(unittest.TestCase):
    def test_examples(self):
        self.assertFalse(parse_bool_expr("&(|(f))"))
        self.assertTrue(parse_bool_expr("|(f,f,f,t)"))
        self.assertTrue(parse_bool_expr("!(&(f,t))"))

    def test_literals(self):
        self.assertTrue(parse_bool_expr("t"))
        self.assertFalse(parse_bool_expr("f"))

    def test_simple_operators(self):
        self.assertFalse(parse_bool_expr("!(t)"))
        self.assertTrue(parse_bool_expr("!(f)"))
        self.assertTrue(parse_bool_expr("&(t,t,t)"))
        self.assertFalse(parse_bool_expr("&(t,f,t)"))
        self.assertTrue(parse_bool_expr("|(f,t,f)"))
        self.assertFalse(parse_bool_expr("|(f,f,f)"))

    def test_nested_complex(self):
        expr = "|(&(t,!(f)),!(|(t,f)))"
        self.assertTrue(parse_bool_expr(expr))

    def test_deep_nesting(self):
        # Construct !(!(!(...(t)...)))
        depth = 500
        expr = "!(" * depth + "t" + ")" * depth
        expected = True if depth % 2 == 0 else False
        self.assertEqual(parse_bool_expr(expr), expected)

    def test_large_expression(self):
        # Large OR expression containing 1000 sub-expressions
        rng = random.Random(42)
        operands = ["t" if rng.random() > 0.5 else "f" for _ in range(1000)]
        operands[500] = "t"
        expr = f"|({','.join(operands)})"
        self.assertTrue(parse_bool_expr(expr))
