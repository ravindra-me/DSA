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
from problem_01 import ListNode, find_middle_value  # noqa: E402
# ---- End of generated header ----

def build_linked_list(values: list[int]) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


class TestFindMiddleValue(TestCase):
    def test_example_1_odd_length(self):
        head = build_linked_list([1, 2, 3, 4, 5])
        self.assertEqual(find_middle_value(head), 3)

    def test_example_2_even_length(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(find_middle_value(head), 4)

    def test_single_element(self):
        head = build_linked_list([42])
        self.assertEqual(find_middle_value(head), 42)

    def test_two_elements(self):
        head = build_linked_list([10, 20])
        self.assertEqual(find_middle_value(head), 20)

    def test_duplicate_and_negative_values(self):
        values = [-5, -10, 0, -10, 7]
        head = build_linked_list(values)
        # Length is 5, index 2 is value 0
        self.assertEqual(find_middle_value(head), 0)

    def test_all_identical_values(self):
        head = build_linked_list([7, 7, 7, 7])
        self.assertEqual(find_middle_value(head), 7)

    def test_large_input_odd(self):
        n = 10001
        values = list(range(n))
        head = build_linked_list(values)
        expected = values[n // 2]
        self.assertEqual(find_middle_value(head), expected)

    def test_large_input_even(self):
        n = 10000
        values = [i * 3 for i in range(n)]
        head = build_linked_list(values)
        expected = values[n // 2]
        self.assertEqual(find_middle_value(head), expected)
