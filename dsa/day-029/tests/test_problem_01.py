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
from problem_01 import ListNode, partition  # noqa: E402
# ---- End of generated header ----

import random
from typing import List, Optional


def to_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def to_python_list(head: Optional[ListNode]) -> List[int]:
    res = []
    curr = head
    seen = set()
    while curr:
        if id(curr) in seen:
            raise RuntimeError("Cycle detected in linked list")
        seen.add(id(curr))
        res.append(curr.val)
        curr = curr.next
    return res


class TestPartitionList(TestCase):
    def test_example_1(self):
        head = to_linked_list([1, 4, 3, 2, 5, 2])
        result = partition(head, 3)
        self.assertEqual(to_python_list(result), [1, 2, 2, 4, 3, 5])

    def test_example_2(self):
        head = to_linked_list([2, 1])
        result = partition(head, 2)
        self.assertEqual(to_python_list(result), [1, 2])

    def test_empty_list(self):
        head = to_linked_list([])
        result = partition(head, 0)
        self.assertIsNone(result)

    def test_single_element(self):
        head1 = to_linked_list([5])
        result1 = partition(head1, 10)
        self.assertEqual(to_python_list(result1), [5])

        head2 = to_linked_list([5])
        result2 = partition(head2, 3)
        self.assertEqual(to_python_list(result2), [5])

    def test_all_elements_less(self):
        values = [1, 2, 0, -1, 3]
        head = to_linked_list(values)
        result = partition(head, 5)
        self.assertEqual(to_python_list(result), values)

    def test_all_elements_greater_or_equal(self):
        values = [5, 6, 7, 5, 8]
        head = to_linked_list(values)
        result = partition(head, 5)
        self.assertEqual(to_python_list(result), values)

    def test_duplicates_and_negative_values(self):
        values = [-5, 0, -5, 2, -10, 5, 0]
        head = to_linked_list(values)
        result = partition(head, 0)
        # < 0: [-5, -5, -10]; >= 0: [0, 2, 5, 0]
        expected = [-5, -5, -10, 0, 2, 5, 0]
        self.assertEqual(to_python_list(result), expected)

    def test_large_input_stability(self):
        rng = random.Random(42)
        values = [rng.randint(-1000, 1000) for _ in range(5000)]
        pivot = 0

        # Expected result by stable partitioning
        less = [v for v in values if v < pivot]
        greater = [v for v in values if v >= pivot]
        expected = less + greater

        head = to_linked_list(values)
        result = partition(head, pivot)
        self.assertEqual(to_python_list(result), expected)
