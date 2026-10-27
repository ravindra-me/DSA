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
from problem_05 import min_mutation  # noqa: E402
# ---- End of generated header ----

import unittest
import random

class TestMinMutation(unittest.TestCase):
    def test_example_1(self):
        start = "AACCGGTT"
        end = "AACCGGTA"
        bank = ["AACCGGTA"]
        self.assertEqual(min_mutation(start, end, bank), 1)

    def test_example_2(self):
        start = "AACCGGTT"
        end = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        self.assertEqual(min_mutation(start, end, bank), 2)

    def test_example_3(self):
        start = "AAAAACCC"
        end = "AACCCCCC"
        bank = ["AAAACCCC", "AAACCCCC"]
        self.assertEqual(min_mutation(start, end, bank), -1)

    def test_same_start_and_end(self):
        start = "AACCGGTT"
        end = "AACCGGTT"
        bank = ["AACCGGTT"]
        self.assertEqual(min_mutation(start, end, bank), 0)

    def test_empty_bank(self):
        start = "AACCGGTT"
        end = "AACCGGTA"
        bank = []
        self.assertEqual(min_mutation(start, end, bank), -1)

    def test_unreachable_path(self):
        start = "AACCGGTT"
        end = "TTGGCCAA"
        bank = ["AACCGGTA", "AACCGGAA", "TTGGCCAA"]
        self.assertEqual(min_mutation(start, end, bank), -1)

    def test_long_chain_max_bank(self):
        # Construct a clear linear path of 8 mutations
        chars = ['A', 'C', 'G', 'T']
        start = "AAAAAAAA"
        end = "CCCCCCCC"
        
        # Create a linear path from AAAAAAAA to CCCCCCCC
        path = []
        curr = list(start)
        for i in range(8):
            curr[i] = 'C'
            path.append("".join(curr))
        
        # Add random noise to bank up to 100 entries
        rng = random.Random(42)
        bank_set = set(path)
        while len(bank_set) < 100:
            random_gene = "".join(rng.choices(chars, k=8))
            if random_gene != start:
                bank_set.add(random_gene)
                
        bank = list(bank_set)
        self.assertEqual(min_mutation(start, end, bank), 8)
