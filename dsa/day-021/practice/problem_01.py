class NumArray:
    """Range sum query data structure using a 1D prefix sum array."""

    def __init__(self, nums: list[int]) -> None:
        """Precomputes prefix sums of nums in O(N) time."""
        raise NotImplementedError

    def sum_range(self, left: int, right: int) -> int:
        """Computes sum of nums[left..right] in O(1) time."""
        raise NotImplementedError
