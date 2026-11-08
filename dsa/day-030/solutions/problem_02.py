def max_distance(position: list[int], m: int) -> int:
    """Return maximum possible minimum magnetic force between any two balls."""
    position.sort()

    def can_place(d: int) -> bool:
        count = 1
        last_pos = position[0]
        for pos in position[1:]:
            if pos - last_pos >= d:
                count += 1
                last_pos = pos
                if count == m:
                    return True
        return False

    low = 1
    high = position[-1] - position[0]
    ans = 1

    while low <= high:
        mid = (low + high) // 2
        if can_place(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
