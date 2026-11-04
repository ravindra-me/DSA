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
from problem_04 import ListNode, add_two_numbers_ii  # noqa: E402
# ---- End of generated header ----

import unittest
import random

def build_list(vals: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(head: ListNode | None) -> list[int]:
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

class TestAddTwoNumbersII(unittest.TestCase):
    def test_example_1(self):
        l1 = build_list([7, 2, 4, 3])
        l2 = build_list([5, 6, 4])
        res = add_two_numbers_ii(l1, l2)
        self.assertEqual(to_list(res), [7, 8, 0, 7])

    def test_example_2(self):
        l1 = build_list([0])
        l2 = build_list([0])
        res = add_two_numbers_ii(l1, l2)
        self.assertEqual(to_list(res), [0])

    def test_different_lengths_with_carry(self):
        l1 = build_list([9, 9])
        l2 = build_list([1])
        res = add_two_numbers_ii(l1, l2)
        self.assertEqual(to_list(res), [1, 0, 0])

    def test_single_element_carry(self):
        l1 = build_list([5])
        l2 = build_list([5])
        res = add_two_numbers_ii(l1, l2)
        self.assertEqual(to_list(res), [1, 0])

    def test_input_lists_not_modified(self):
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        l1 = build_list(v1)
        l2 = build_list(v2)
        add_two_numbers_ii(l1, l2)
        self.assertEqual(to_list(l1), v1)
        self.assertEqual(to_list(l2), v2)

    def test_large_random_input(self):
        rng = random.Random(42)
        digits1 = [rng.randint(1, 9)] + [rng.randint(0, 9) for _ in range(99)]
        digits2 = [rng.randint(1, 9)] + [rng.randint(0, 9) for _ in range(80)]
        
        num1 = int("".join(map(str, digits1)))
        num2 = int("".join(map(str, digits2)))
        expected_sum = num1 + num2
        expected_digits = [int(d) for d in str(expected_sum)]
        
        l1 = build_list(digits1)
        l2 = build_list(digits2)
        res = add_two_numbers_ii(l1, l2)
        self.assertEqual(to_list(res), expected_digits)
