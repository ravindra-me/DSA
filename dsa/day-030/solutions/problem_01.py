import math

def min_eating_speed(piles: list[int], h: int) -> int:
    """Return the minimum integer speed k to eat all bananas within h hours."""
    low = 1
    high = max(piles)

    while low < high:
        mid = (low + high) // 2
        # Total hours needed at speed mid:
        # ceil(p / mid) is equivalent to (p + mid - 1) // mid
        hours_needed = sum((p + mid - 1) // mid for p in piles)
        if hours_needed <= h:
            high = mid
        else:
            low = mid + 1

    return low
