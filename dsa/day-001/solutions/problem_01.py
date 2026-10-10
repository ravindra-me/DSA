def find_missing_number(nums: list[int]) -> int:
    """Return the single missing number from the range [0, len(nums)]."""
    missing = len(nums)
    for index, value in enumerate(nums):
        missing ^= index ^ value
    return missing
