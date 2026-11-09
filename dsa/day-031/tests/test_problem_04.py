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
from problem_04 import ListNode, insertion_sort_list  # noqa: E402
# ---- End of generated header ----

import random


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    result = []
    curr = head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    return result


class TestInsertionSortList(TestCase):
    def test_example_1(self):
        head = build_list([4, 2, 1, 3])
        sorted_head = insertion_sort_list(head)
        self.assertEqual(to_list(sorted_head), [1, 2, 3, 4])

    def test_example_2_with_negatives(self):
        head = build_list([-1, 5, 3, 4, 0])
        sorted_head = insertion_sort_list(head)
        self.assertEqual(to_list(sorted_head), [-1, 0, 3, 4, 5])

    def test_empty_list(self):
        head = build_list([])
        sorted_head = insertion_sort_list(head)
        self.assertIsNone(sorted_head)

    def test_single_element(self):
        head = build_list([42])
        sorted_head = insertion_sort_list(head)
        self.assertEqual(to_list(sorted_head), [42])

    def test_all_duplicates(self):
        head = build_list([7, 7, 7, 7, 7])
        sorted_head = insertion_sort_list(head)
        self.assertEqual(to_list(sorted_head), [7, 7, 7, 7, 7])

    def test_reverse_sorted(self):
        head = build_list([5, 4, 3, 2, 1, 0, -1, -2])
        sorted_head = insertion_sort_list(head)
        self.assertEqual(to_list(sorted_head), [-2, -1, 0, 1, 2, 3, 4, 5])

    def test_already_sorted_large(self):
        values = list(range(1000))
        head = build_list(values)
        sorted_head = insertion_sort_list(head)
        self.assertEqual(to_list(sorted_head), values)

    def test_random_large(self):
        rng = random.Random(42)
        values = [rng.randint(-5000, 5000) for _ in range(1200)]
        expected = sorted(values)
        head = build_list(values)
        sorted_head = insertion_sort_list(head)
        self.assertEqual(to_list(sorted_head), expected)
