class NumArray:
    """Range sum query data structure using a 1D prefix sum array."""

    def __init__(self, nums: list[int]) -> None:
        """Precomputes prefix sums of nums in O(N) time."""
        self._prefix: list[int] = [0] * (len(nums) + 1)
        for i, val in enumerate(nums):
            self._prefix[i + 1] = self._prefix[i] + val

    def sum_range(self, left: int, right: int) -> int:
        """Computes sum of nums[left..right] in O(1) time."""
        return self._prefix[right + 1] - self._prefix[left]
