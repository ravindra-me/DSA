def corp_flight_bookings(bookings: list[list[int]], n: int) -> list[int]:
    """Compute total reserved seats for flights 1 to n using a difference array."""
    res = [0] * n
    for first, last, seats in bookings:
        res[first - 1] += seats
        if last < n:
            res[last] -= seats

    for i in range(1, n):
        res[i] += res[i - 1]

    return res
