# Solution 5: Corporate Flight Bookings

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Difference Array

## Approach

Use a difference array (prefix sum of changes) to perform range additions in $O(1)$ time per booking, followed by a single prefix sum pass in $O(n)$ time to recover the final seat counts.

## Thought Process

A naive approach updates each flight in range `[first, last]` directly for each booking. In the worst case, each booking spans $O(n)$ flights, yielding an $O(n \times m)$ time complexity where $m$ is `len(bookings)`. With $n, m \le 2 \times 10^4$, this results in up to $4 \times 10^8$ operations, which easily risks timing out.

To optimize, observe that adding `seats` to every index in `[first, last]` implies that the change from flight `first - 1` to `first` increases by `seats`, and the change from `last` to `last + 1` decreases by `seats`. By maintaining a difference array `diff` of size $n + 1$ (or $n$), we can apply range updates in $O(1)$ by doing `diff[first - 1] += seats` and `diff[last] -= seats` (if `last < n`). Once all bookings are processed, taking the running prefix sum across `diff` yields the exact seat counts for all flights in a single $O(n)$ sweep.

## Algorithm

1. Initialize an array `res` of length `n` with zeros.
2. For each booking `[first, last, seats]`: add `seats` to `res[first - 1]` to mark the start of the reservation interval. If `last < n`, subtract `seats` from `res[last]` to mark the end of the interval.
3. Iterate through `res` from index 1 to `n - 1`, setting `res[i] += res[i - 1]` to compute the running prefix sum in-place.
4. Return `res`.

## Complexity Analysis

- **Time:** $O(n + m)$ where $n$ is the number of flights and $m$ is the number of bookings. Each booking update takes $O(1)$ time and the prefix sum pass takes $O(n)$ time.
- **Space:** $O(1)$ auxiliary space beyond the output array of size $n$, as the prefix sum is computed in-place on the output buffer.

## Edge Cases

- Single flight (`n = 1`): Booking updates index 0 and avoids out-of-bounds access since `last == n`.
- Full range bookings (`first == 1` and `last == n`): The end boundary adjustment is safely skipped since `last == n`.
- Single-flight bookings (`first == last`): Start added at `first - 1`, subtracted at `first` if `first < n`.
- Multiple bookings on the exact same flight or interval: Difference array naturally accumulates additive changes correctly.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
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
```
