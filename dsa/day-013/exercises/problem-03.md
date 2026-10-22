# Problem 3: Recent Calls Rate Limiter

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Sliding window time-series queue | [Day 13: Queue](../README.md) |

## Problem Statement

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:
- `RecentCounter()`: Initializes the counter with zero recent requests.
- `ping(t: int) -> int`: Adds a new request at timestamp `t`, where `t` represents some time in milliseconds, and returns the number of requests that have happened in the past `3000` milliseconds (inclusive of `t`). That is, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

It is guaranteed that every call to `ping` uses a strictly larger value of `t` than the previous call.

## Input

Sequential integer timestamps `t` passed to `ping`.

## Output

Integer count of requests falling in `[t - 3000, t]`.

## Constraints

- 1 <= t <= 10^9
- Each test case will call ping with strictly increasing values of t.
- At most 10^4 calls will be made to ping.

## Examples

**Example 1**

```text
Input:  rc = RecentCounter()
rc.ping(1) -> 1
rc.ping(100) -> 2
rc.ping(3001) -> 3
rc.ping(3002) -> 3
Output: 1, 2, 3, 3
```

At t=3002, the window is [2, 3002]. Request 1 falls outside the range and is discarded, leaving requests [100, 3001, 3002] for a count of 3.

**Example 2**

```text
Input:  rc = RecentCounter()
rc.ping(1) -> 1
rc.ping(4000) -> 1
Output: 1, 1
```

At t=4000, the window is [1000, 4000]. Request 1 at t=1 is discarded, leaving only request 4000.

## Function Signature

```python
from collections import deque

class RecentCounter:
    def __init__(self) -> None:
        """Initialize the counter."""
        pass

    def ping(self, t: int) -> int:
        """Record request at time t and return count in [t - 3000, t]."""
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Store timestamps in a FIFO queue. For every ping, enqueue the current timestamp and dequeue older elements until the front is within [t - 3000, t].

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
