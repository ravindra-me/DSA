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
from problem_02 import ListNode, swap_pairs  # noqa: E402
# ---- End of generated header ----

from typing import Optional


def to_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list[int]:
    res = []
    curr = head
    while curr is not None:
        res.append(curr.val)
        curr = curr.next
    return res


class TestSwapPairs(TestCase):
    def test_example_even_nodes(self):
        head = to_linked_list([1, 2, 3, 4])
        result = swap_pairs(head)
        self.assertEqual(to_list(result), [2, 1, 4, 3])

    def test_example_odd_nodes(self):
        head = to_linked_list([1, 2, 3])
        result = swap_pairs(head)
        self.assertEqual(to_list(result), [2, 1, 3])

    def test_empty_list(self):
        head = to_linked_list([])
        result = swap_pairs(head)
        self.assertEqual(to_list(result), [])

    def test_single_node(self):
        head = to_linked_list([42])
        result = swap_pairs(head)
        self.assertEqual(to_list(result), [42])

    def test_duplicates_and_negatives(self):
        head = to_linked_list([-5, -5, 0, 7, -1])
        result = swap_pairs(head)
        self.assertEqual(to_list(result), [-5, -5, 7, 0, -1])

    def test_two_nodes(self):
        head = to_linked_list([10, 20])
        result = swap_pairs(head)
        self.assertEqual(to_list(result), [20, 10])

    def test_large_input_1000_nodes(self):
        values = list(range(1000))
        expected = []
        for i in range(0, len(values), 2):
            if i + 1 < len(values):
                expected.extend([values[i + 1], values[i]])
            else:
                expected.append(values[i])
        head = to_linked_list(values)
        result = swap_pairs(head)
        self.assertEqual(to_list(result), expected)
