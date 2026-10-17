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
from problem_04 import ListNode, partition_list  # noqa: E402
# ---- End of generated header ----

import random

def build_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head: ListNode | None) -> list[int]:
    result = []
    curr = head
    visited_count = 0
    while curr is not None:
        result.append(curr.val)
        curr = curr.next
        visited_count += 1
        if visited_count > 10000:  # Cycle safety guard
            raise ValueError("Cycle detected in linked list")
    return result


class TestPartitionList(TestCase):
    def test_example_1(self) -> None:
        head = build_linked_list([1, 4, 3, 2, 5, 2])
        result = partition_list(head, 3)
        self.assertEqual(linked_list_to_list(result), [1, 2, 2, 4, 3, 5])

    def test_example_2_empty_list(self) -> None:
        result = partition_list(None, 0)
        self.assertIsNone(result)

    def test_single_element_less_and_greater(self) -> None:
        head1 = build_linked_list([5])
        result1 = partition_list(head1, 10)
        self.assertEqual(linked_list_to_list(result1), [5])

        head2 = build_linked_list([5])
        result2 = partition_list(head2, 3)
        self.assertEqual(linked_list_to_list(result2), [5])

    def test_all_elements_less_than_pivot(self) -> None:
        head = build_linked_list([1, 2, 0, -3])
        result = partition_list(head, 5)
        self.assertEqual(linked_list_to_list(result), [1, 2, 0, -3])

    def test_all_elements_greater_than_or_equal_to_pivot(self) -> None:
        head = build_linked_list([5, 6, 7, 5])
        result = partition_list(head, 5)
        self.assertEqual(linked_list_to_list(result), [5, 6, 7, 5])

    def test_negative_values_and_duplicates(self) -> None:
        values = [-5, 10, -20, 0, 0, -5, 15, -1]
        head = build_linked_list(values)
        result = partition_list(head, 0)
        expected = [v for v in values if v < 0] + [v for v in values if v >= 0]
        self.assertEqual(linked_list_to_list(result), expected)

    def test_large_random_input(self) -> None:
        rng = random.Random(42)
        values = [rng.randint(-1000, 1000) for _ in range(5000)]
        pivot = rng.randint(-500, 500)

        head = build_linked_list(values)
        result = partition_list(head, pivot)

        expected = [v for v in values if v < pivot] + [v for v in values if v >= pivot]
        self.assertEqual(linked_list_to_list(result), expected)
