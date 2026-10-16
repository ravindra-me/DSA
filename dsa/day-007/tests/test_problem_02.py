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
from problem_02 import ListNode, remove_elements  # noqa: E402
# ---- End of generated header ----

import random
from typing import List, Optional

def helpers_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def helpers_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

class TestRemoveElements(unittest.TestCase):
    def test_example_1(self):
        head = helpers_to_linked_list([1, 2, 6, 3, 4, 5, 6])
        res = remove_elements(head, 6)
        self.assertEqual(helpers_to_list(res), [1, 2, 3, 4, 5])

    def test_example_2_all_removed(self):
        head = helpers_to_linked_list([7, 7, 7, 7])
        res = remove_elements(head, 7)
        self.assertEqual(helpers_to_list(res), [])

    def test_empty_list(self):
        res = remove_elements(None, 1)
        self.assertIsNone(res)

    def test_single_element_match(self):
        head = helpers_to_linked_list([5])
        res = remove_elements(head, 5)
        self.assertIsNone(res)

    def test_single_element_no_match(self):
        head = helpers_to_linked_list([5])
        res = remove_elements(head, 3)
        self.assertEqual(helpers_to_list(res), [5])

    def test_consecutive_duplicates(self):
        head = helpers_to_linked_list([1, 2, 2, 2, 3])
        res = remove_elements(head, 2)
        self.assertEqual(helpers_to_list(res), [1, 3])

    def test_value_not_present(self):
        head = helpers_to_linked_list([1, 2, 3, 4])
        res = remove_elements(head, 5)
        self.assertEqual(helpers_to_list(res), [1, 2, 3, 4])

    def test_large_input(self):
        rng = random.Random(42)
        values = [rng.randint(0, 10) for _ in range(10000)]
        target = 5
        expected = [x for x in values if x != target]
        
        head = helpers_to_linked_list(values)
        res = remove_elements(head, target)
        self.assertEqual(helpers_to_list(res), expected)
