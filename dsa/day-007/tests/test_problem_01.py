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
from problem_01 import ListNode, reverse_list  # noqa: E402
# ---- End of generated header ----

from typing import Optional


def list_to_array(head: Optional[ListNode]) -> list[int]:
    result = []
    curr = head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    return result


def array_to_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


class TestReverseList(TestCase):
    def test_example_1_standard_list(self):
        head = array_to_list([1, 2, 3, 4, 5])
        reversed_head = reverse_list(head)
        self.assertEqual(list_to_array(reversed_head), [5, 4, 3, 2, 1])

    def test_example_2_empty_list(self):
        head = array_to_list([])
        reversed_head = reverse_list(head)
        self.assertIsNone(reversed_head)

    def test_single_element(self):
        head = array_to_list([42])
        reversed_head = reverse_list(head)
        self.assertEqual(list_to_array(reversed_head), [42])

    def test_two_elements(self):
        head = array_to_list([1, 2])
        reversed_head = reverse_list(head)
        self.assertEqual(list_to_array(reversed_head), [2, 1])

    def test_duplicate_and_negative_values(self):
        values = [-5, 0, 3, -5, 0, 7]
        head = array_to_list(values)
        reversed_head = reverse_list(head)
        self.assertEqual(list_to_array(reversed_head), values[::-1])

    def test_large_input_5000_nodes(self):
        values = [(i * 37) % 10001 - 5000 for i in range(5000)]
        head = array_to_list(values)
        reversed_head = reverse_list(head)
        expected = list(reversed(values))
        self.assertEqual(list_to_array(reversed_head), expected)
