# Problem 5: Corporate Flight Bookings

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Difference Array | [Day 21: Prefix & Suffix Techniques](../README.md) |

## Problem Statement

There are `n` flights labeled from `1` to `n`.

You are given an array of flight bookings `bookings`, where `bookings[i] = [first_i, last_i, seats_i]` represents a booking for a sequence of flights from flight `first_i` to flight `last_i` (inclusive) with `seats_i` seats reserved on each flight in the range.

Return an array `answer` of length `n`, where `answer[i]` is the total number of seats reserved on flight `i + 1`.

## Input

`bookings`: list of triplets `[first, last, seats]` (1-indexed flight numbers).
`n`: integer total number of flights.

## Output

`list[int]`: 0-indexed list of length `n` containing total seats reserved per flight.

## Constraints

- 1 <= n <= 2 * 10^4
- 1 <= len(bookings) <= 2 * 10^4
- bookings[i].length == 3
- 1 <= first_i <= last_i <= n
- 1 <= seats_i <= 10^4

## Examples

**Example 1**

```text
Input:  bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]], n = 5
Output: [10, 55, 45, 25, 25]
```

Flight 1: 10 = 10
Flight 2: 10 + 20 + 25 = 55
Flight 3: 20 + 25 = 45
Flight 4: 25 = 25
Flight 5: 25 = 25

**Example 2**

```text
Input:  bookings = [[1, 2, 10], [2, 2, 15]], n = 2
Output: [10, 25]
```

Flight 1 gets 10 seats. Flight 2 gets 10 + 15 = 25 seats.

## Function Signature

```python
def corp_flight_bookings(bookings: list[list[int]], n: int) -> list[int]:
    """Compute total reserved seats for flights 1 to n using a difference array."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use a difference array to record +seats at the start index and -seats at the end + 1 index in O(1) time per booking, then perform a single prefix sum sweep in O(n) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
