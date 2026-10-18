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
from problem_02 import ListNode, remove_kth_from_end  # noqa: E402
# ---- End of generated header ----

def list_to_linked(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_to_list(head: ListNode | None) -> list[int]:
    result = []
    curr = head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    return result

class TestRemoveKthFromEnd(TestCase):
    def test_example_1(self):
        head = list_to_linked([1, 2, 3, 4, 5])
        res = remove_kth_from_end(head, 2)
        self.assertEqual(linked_to_list(res), [1, 2, 3, 5])

    def test_example_2_single_node(self):
        head = list_to_linked([1])
        res = remove_kth_from_end(head, 1)
        self.assertEqual(linked_to_list(res), [])

    def test_example_3_remove_head_two_nodes(self):
        head = list_to_linked([1, 2])
        res = remove_kth_from_end(head, 2)
        self.assertEqual(linked_to_list(res), [2])

    def test_remove_last_node(self):
        head = list_to_linked([10, 20, 30])
        res = remove_kth_from_end(head, 1)
        self.assertEqual(linked_to_list(res), [10, 20])

    def test_negative_and_zero_values(self):
        vals = [-100, 0, 50, -25, 0]
        head = list_to_linked(vals)
        res = remove_kth_from_end(head, 3)
        self.assertEqual(linked_to_list(res), [-100, 0, -25, 0])

    def test_duplicates(self):
        vals = [7, 7, 7, 7]
        head = list_to_linked(vals)
        res = remove_kth_from_end(head, 2)
        self.assertEqual(linked_to_list(res), [7, 7, 7])

    def test_large_input(self):
        n = 50_000
        k = 12_345
        vals = list(range(n))
        head = list_to_linked(vals)

        res = remove_kth_from_end(head, k)
        res_list = linked_to_list(res)

        # Expected: vals with index n - k removed
        expected_removed_idx = n - k
        expected = vals[:expected_removed_idx] + vals[expected_removed_idx + 1:]
        self.assertEqual(len(res_list), n - 1)
        self.assertEqual(res_list, expected)
