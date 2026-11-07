# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_03.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_03 import ListNode, sort_list  # noqa: E402
# ---- End of generated header ----

import random
from typing import Optional


def list_to_linked(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_to_list(head: Optional[ListNode]) -> list[int]:
    res = []
    curr = head
    while curr is not None:
        res.append(curr.val)
        curr = curr.next
    return res


class TestSortList(TestCase):
    def test_example_1(self) -> None:
        head = list_to_linked([4, 2, 1, 3])
        sorted_head = sort_list(head)
        self.assertEqual(linked_to_list(sorted_head), [1, 2, 3, 4])

    def test_example_2_negatives_and_zero(self) -> None:
        head = list_to_linked([-1, 5, 3, 4, 0])
        sorted_head = sort_list(head)
        self.assertEqual(linked_to_list(sorted_head), [-1, 0, 3, 4, 5])

    def test_empty_list(self) -> None:
        head = list_to_linked([])
        sorted_head = sort_list(head)
        self.assertIsNone(sorted_head)

    def test_single_element(self) -> None:
        head = list_to_linked([42])
        sorted_head = sort_list(head)
        self.assertEqual(linked_to_list(sorted_head), [42])

    def test_two_elements_reversed(self) -> None:
        head = list_to_linked([2, 1])
        sorted_head = sort_list(head)
        self.assertEqual(linked_to_list(sorted_head), [1, 2])

    def test_duplicates(self) -> None:
        nums = [3, 1, 2, 3, 1, 2, 3]
        head = list_to_linked(nums)
        sorted_head = sort_list(head)
        self.assertEqual(linked_to_list(sorted_head), sorted(nums))

    def test_already_sorted_and_reversed(self) -> None:
        nums_sorted = [-10, -5, 0, 5, 10]
        head = list_to_linked(nums_sorted)
        self.assertEqual(linked_to_list(sort_list(head)), nums_sorted)

        nums_reversed = [10, 5, 0, -5, -10]
        head_rev = list_to_linked(nums_reversed)
        self.assertEqual(linked_to_list(sort_list(head_rev)), nums_sorted)

    def test_large_input_performance(self) -> None:
        rng = random.Random(42)
        values = [rng.randint(-100_000, 100_000) for _ in range(10_000)]
        head = list_to_linked(values)
        sorted_head = sort_list(head)
        self.assertEqual(linked_to_list(sorted_head), sorted(values))
