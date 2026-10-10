def two_sum_sorted(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Find two numbers in a sorted list that sum to target, returning 1-based indices."""
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return (left + 1, right + 1)
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return None
