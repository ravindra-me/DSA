def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any value appears at least twice in nums."""
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
