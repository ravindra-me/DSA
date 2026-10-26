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
from problem_04 import kth_grammar  # noqa: E402
# ---- End of generated header ----

class TestKthGrammar(TestCase):
    def test_base_case(self):
        self.assertEqual(kth_grammar(1, 1), 0)

    def test_row_two(self):
        self.assertEqual(kth_grammar(2, 1), 0)
        self.assertEqual(kth_grammar(2, 2), 1)

    def test_row_three(self):
        # Row 3 is 0110
        expected = [0, 1, 1, 0]
        for k in range(1, 5):
            self.assertEqual(kth_grammar(3, k), expected[k - 1])

    def test_row_four_example(self):
        # Row 4 is 01101001
        self.assertEqual(kth_grammar(4, 5), 1)

    def test_first_element_any_row(self):
        # The first element of any row is always 0
        for n in range(1, 20):
            self.assertEqual(kth_grammar(n, 1), 0)

    def test_last_element_boundary(self):
        # Last element of row 4 (k = 8) is 1
        self.assertEqual(kth_grammar(4, 8), 1)
        # Last element of row 5 (k = 16) is 0
        self.assertEqual(kth_grammar(5, 16), 0)

    def test_maximum_n(self):
        # n = 30, k = 2^29
        n = 30
        k = 1 << 29
        # Mathematical property: kth_grammar(n, 2^(n-1)) depends on parity of (n-1)
        # Row 1 end: 0 (count of 1s in index-1 = 0 -> 0)
        # Bit-count property: symbol at index k-1 (0-based) is popcount(k-1) % 2
        expected = bin(k - 1).count('1') % 2
        self.assertEqual(kth_grammar(n, k), expected)
