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
from problem_01 import ListNode, partition_list  # noqa: E402
# ---- End of generated header ----

import random
import unittest


def to_ll(arr: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def to_arr(head: ListNode | None) -> list[int]:
    result = []
    curr = head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    return result


class TestPartitionList(unittest.TestCase):
    def test_example_1(self):
        head = to_ll([1, 4, 3, 2, 5, 2])
        res = partition_list(head, 3)
        self.assertEqual(to_arr(res), [1, 2, 2, 4, 3, 5])

    def test_example_2(self):
        head = to_ll([2, 1])
        res = partition_list(head, 2)
        self.assertEqual(to_arr(res), [1, 2])

    def test_empty_list(self):
        self.assertIsNone(partition_list(None, 5))

    def test_single_element(self):
        head = to_ll([10])
        res = partition_list(head, 5)
        self.assertEqual(to_arr(res), [10])
        
        head2 = to_ll([2])
        res2 = partition_list(head2, 5)
        self.assertEqual(to_arr(res2), [2])

    def test_all_less(self):
        head = to_ll([1, 2, 0, -1])
        res = partition_list(head, 5)
        self.assertEqual(to_arr(res), [1, 2, 0, -1])

    def test_all_greater_or_equal(self):
        head = to_ll([5, 6, 7, 8])
        res = partition_list(head, 5)
        self.assertEqual(to_arr(res), [5, 6, 7, 8])

    def test_duplicates_and_negatives(self):
        head = to_ll([0, -5, 3, -5, 2, 0])
        res = partition_list(head, 0)
        self.assertEqual(to_arr(res), [-5, -5, 0, 3, 2, 0])

    def test_large_input(self):
        rng = random.Random(42)
        raw_data = [rng.randint(-100, 100) for _ in range(200)]
        pivot = 0
        
        expected_less = [val for val in raw_data if val < pivot]
        expected_greater = [val for val in raw_data if val >= pivot]
        expected = expected_less + expected_greater
        
        head = to_ll(raw_data)
        res = partition_list(head, pivot)
        self.assertEqual(to_arr(res), expected)
