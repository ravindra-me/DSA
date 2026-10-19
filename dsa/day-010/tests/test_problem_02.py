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
from problem_02 import eval_rpn  # noqa: E402
# ---- End of generated header ----

class TestEvalRPN(TestCase):
    def test_example_1(self):
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(eval_rpn(tokens), 9)

    def test_example_2(self):
        tokens = ["4", "13", "5", "/", "+"]
        self.assertEqual(eval_rpn(tokens), 6)

    def test_example_3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(eval_rpn(tokens), 22)

    def test_single_element_positive(self):
        self.assertEqual(eval_rpn(["42"]), 42)

    def test_single_element_negative(self):
        self.assertEqual(eval_rpn(["-200"]), -200)

    def test_negative_division_truncation(self):
        # 6 / -132 should truncate to 0, not -1
        self.assertEqual(eval_rpn(["6", "-132", "/"]), 0)
        # -7 / 2 should truncate to -3, not -4
        self.assertEqual(eval_rpn(["-7", "2", "/"]), -3)

    def test_subtraction_order(self):
        # 5 - 3 = 2, not 3 - 5 = -2
        self.assertEqual(eval_rpn(["5", "3", "-"]), 2)

    def test_large_input_summation(self):
        n = 5000
        tokens = ["1"] * n + ["+"] * (n - 1)
        self.assertEqual(eval_rpn(tokens), n)
