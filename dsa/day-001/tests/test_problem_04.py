# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_04.py
import os
import sys
import unittest

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_04 import find_peak_element  # noqa: E402
# ---- End of generated header ----

class TestFindPeakElement(unittest.TestCase):
    def _validate_peak(self, nums: list[int], peak_idx: int) -> None:
        self.assertTrue(0 <= peak_idx < len(nums), f"Index {peak_idx} out of range")
        left_val = float("-inf") if peak_idx == 0 else nums[peak_idx - 1]
        right_val = float("-inf") if peak_idx == len(nums) - 1 else nums[peak_idx + 1]
        self.assertGreater(
            nums[peak_idx],
            left_val,
            f"Element at {peak_idx} ({nums[peak_idx]}) not greater than left neighbor ({left_val})",
        )
        self.assertGreater(
            nums[peak_idx],
            right_val,
            f"Element at {peak_idx} ({nums[peak_idx]}) not greater than right neighbor ({right_val})",
        )

    def test_examples(self) -> None:
        ex1 = [1, 2, 3, 1]
        res1 = find_peak_element(ex1)
        self.assertEqual(res1, 2)
        self._validate_peak(ex1, res1)

        ex2 = [1, 2, 1, 3, 5, 6, 4]
        res2 = find_peak_element(ex2)
        self.assertIn(res2, [1, 5])
        self._validate_peak(ex2, res2)

    def test_single_element(self) -> None:
        nums = [42]
        res = find_peak_element(nums)
        self.assertEqual(res, 0)
        self._validate_peak(nums, res)

    def test_two_elements(self) -> None:
        nums_asc = [1, 2]
        res_asc = find_peak_element(nums_asc)
        self.assertEqual(res_asc, 1)
        self._validate_peak(nums_asc, res_asc)

        nums_desc = [2, 1]
        res_desc = find_peak_element(nums_desc)
        self.assertEqual(res_desc, 0)
        self._validate_peak(nums_desc, res_desc)

    def test_strictly_monotonic(self) -> None:
        increasing = list(range(1, 100))
        res_inc = find_peak_element(increasing)
        self.assertEqual(res_inc, len(increasing) - 1)
        self._validate_peak(increasing, res_inc)

        decreasing = list(range(100, 0, -1))
        res_dec = find_peak_element(decreasing)
        self.assertEqual(res_dec, 0)
        self._validate_peak(decreasing, res_dec)

    def test_negative_numbers_and_extremes(self) -> None:
        min_int = -(2**31)
        max_int = 2**31 - 1
        nums = [min_int, 0, -5, max_int, 100]
        res = find_peak_element(nums)
        self._validate_peak(nums, res)

    def test_large_input_efficiency(self) -> None:
        # Construct a large sequence with guaranteed non-equal neighbors
        # Alternating sequence creates multiple peaks across 100,000 items
        n = 100_000
        nums = [i if i % 2 == 0 else i - 2 for i in range(n)]
        peak_idx = find_peak_element(nums)
        self._validate_peak(nums, peak_idx)
