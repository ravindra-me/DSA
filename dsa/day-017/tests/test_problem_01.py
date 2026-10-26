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
from problem_01 import ListNode, swap_pairs  # noqa: E402
# ---- End of generated header ----

from typing import Optional


def list_to_nodes(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def nodes_to_list(head: Optional[ListNode]) -> list[int]:
    res = []
    curr = head
    while curr is not None:
        res.append(curr.val)
        curr = curr.next
    return res


class TestSwapPairs(TestCase):
    def test_example_even_length(self):
        head = list_to_nodes([1, 2, 3, 4])
        result = swap_pairs(head)
        self.assertEqual(nodes_to_list(result), [2, 1, 4, 3])

    def test_example_empty_list(self):
        head = list_to_nodes([])
        result = swap_pairs(head)
        self.assertIsNone(result)

    def test_example_single_node(self):
        head = list_to_nodes([1])
        result = swap_pairs(head)
        self.assertEqual(nodes_to_list(result), [1])

    def test_odd_length_list(self):
        head = list_to_nodes([1, 2, 3, 4, 5])
        result = swap_pairs(head)
        self.assertEqual(nodes_to_list(result), [2, 1, 4, 3, 5])

    def test_two_nodes(self):
        head = list_to_nodes([10, 20])
        result = swap_pairs(head)
        self.assertEqual(nodes_to_list(result), [20, 10])

    def test_duplicate_values(self):
        head = list_to_nodes([2, 2, 3, 3, 4, 4])
        result = swap_pairs(head)
        self.assertEqual(nodes_to_list(result), [2, 2, 3, 3, 4, 4])

    def test_nodes_are_reordered_by_reference(self):
        # Verify that node identities, not just values, are swapped
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        result = swap_pairs(node1)
        self.assertIs(result, node2)
        self.assertIs(result.next, node1)
        self.assertIsNone(node1.next)

    def test_max_constraint_list(self):
        values = list(range(100))
        # Expected: swap each adjacent pair
        expected = []
        for i in range(0, 100, 2):
            expected.extend([i + 1, i])
        head = list_to_nodes(values)
        result = swap_pairs(head)
        self.assertEqual(nodes_to_list(result), expected)
