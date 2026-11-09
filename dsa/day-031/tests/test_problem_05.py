# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_05.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_05 import stable_multikey_sort  # noqa: E402
# ---- End of generated header ----

import random
from unittest import TestCase

class TestStableMultiKeySort(TestCase):
    def test_example_1(self):
        records = [
            {"id": 1, "department": "Engineering", "salary": 90000},
            {"id": 2, "department": "Marketing", "salary": 70000},
            {"id": 3, "department": "Engineering", "salary": 120000},
            {"id": 4, "department": "Marketing", "salary": 70000}
        ]
        expected = [
            {"id": 3, "department": "Engineering", "salary": 120000},
            {"id": 1, "department": "Engineering", "salary": 90000},
            {"id": 2, "department": "Marketing", "salary": 70000},
            {"id": 4, "department": "Marketing", "salary": 70000}
        ]
        result = stable_multikey_sort(records)
        self.assertEqual(result, expected)
        # Ensure original input is not mutated
        self.assertEqual(records[0]["id"], 1)

    def test_empty_list(self):
        self.assertEqual(stable_multikey_sort([]), [])

    def test_single_element(self):
        records = [{"id": 42, "department": "Sales", "salary": 50000}]
        self.assertEqual(stable_multikey_sort(records), records)

    def test_stability_identical_keys(self):
        records = [
            {"id": 1, "department": "HR", "salary": 50000},
            {"id": 2, "department": "HR", "salary": 50000},
            {"id": 3, "department": "HR", "salary": 50000},
            {"id": 4, "department": "HR", "salary": 50000}
        ]
        result = stable_multikey_sort(records)
        self.assertEqual([r["id"] for r in result], [1, 2, 3, 4])

    def test_departments_and_salaries_ordering(self):
        records = [
            {"id": 1, "department": "B", "salary": 100},
            {"id": 2, "department": "A", "salary": 100},
            {"id": 3, "department": "A", "salary": 200},
            {"id": 4, "department": "B", "salary": 300},
            {"id": 5, "department": "A", "salary": 200}
        ]
        expected = [
            {"id": 3, "department": "A", "salary": 200},
            {"id": 5, "department": "A", "salary": 200},
            {"id": 2, "department": "A", "salary": 100},
            {"id": 4, "department": "B", "salary": 300},
            {"id": 1, "department": "B", "salary": 100}
        ]
        self.assertEqual(stable_multikey_sort(records), expected)

    def test_zero_salary_and_single_char_department(self):
        records = [
            {"id": 10, "department": "Z", "salary": 0},
            {"id": 11, "department": "A", "salary": 0},
            {"id": 12, "department": "Z", "salary": 10}
        ]
        expected = [
            {"id": 11, "department": "A", "salary": 0},
            {"id": 12, "department": "Z", "salary": 10},
            {"id": 10, "department": "Z", "salary": 0}
        ]
        self.assertEqual(stable_multikey_sort(records), expected)

    def test_large_input_stability_and_correctness(self):
        rng = random.Random(1337)
        departments = ["Eng", "Sales", "Legal", "Ops", "Product"]
        salaries = [50000, 60000, 70000, 80000]
        records = []
        for i in range(500):
            records.append({
                "id": i,
                "department": rng.choice(departments),
                "salary": rng.choice(salaries)
            })

        result = stable_multikey_sort(records)

        # Verify department order is non-decreasing
        for i in range(len(result) - 1):
            curr_dept, next_dept = result[i]["department"], result[i + 1]["department"]
            curr_sal, next_sal = result[i]["salary"], result[i + 1]["salary"]
            
            self.assertTrue(curr_dept <= next_dept)
            if curr_dept == next_dept:
                self.assertTrue(curr_sal >= next_sal)
                if curr_sal == next_sal:
                    # Verify stability: original relative order preserved
                    self.assertTrue(result[i]["id"] < result[i + 1]["id"])
