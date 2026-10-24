# Solution 2: Recent Calls Counter

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Fixed time-window eviction using deque

## Approach

Maintain a queue (using `collections.deque`) of incoming request timestamps. Because timestamps are strictly increasing, old timestamps that fall outside `[t - 3000, t]` will always be at the front of the queue and can be evicted from left to right.

## Thought Process

A naive approach might store all timestamps in a dynamic array (list) and, for each `ping(t)`, scan through the list or binary search for the first timestamp `>= t - 3000`. Scanning takes $O(N)$ time per query ($O(N^2)$ overall), while binary search takes $O(\log N)$ time per query but retains all $N$ elements in memory.

Since requests arrive in strictly increasing order, any request older than $t - 3000$ will never be valid for any future `ping(t')` where $t' > t$. Thus, outdated timestamps can be permanently discarded. A double-ended queue (or standard FIFO queue) naturally supports appending new timestamps to the back and popping expired timestamps from the front. Each timestamp is added once and popped at most once, achieving amortized $O(1)$ time per `ping` operation.

## Algorithm

1. Initialize an empty double-ended queue `self._requests = collections.deque()`.
2. Upon calling `ping(t)`, append `t` to the right end of `self._requests`.
3. Calculate the lower bound threshold `threshold = t - 3000`.
4. While `self._requests` is not empty and `self._requests[0] < threshold`, pop the oldest timestamp from the left.
5. Return the number of remaining elements in `self._requests`, which is `len(self._requests)`.

## Complexity Analysis

- **Time:** Amortized $O(1)$ per `ping(t)`. Over $N$ total calls, every timestamp is pushed into the deque exactly once and popped at most once, yielding $O(N)$ total operations.
- **Space:** $O(W)$ auxiliary space, where $W$ is the maximum number of requests that occur within any 3000 ms sliding window (at most $\min(N, 3001)$ requests).

## Edge Cases

- First ping: deque was empty; simply appends and returns 1.
- Exact boundary match ($t_1 = t_2 - 3000$): since the window $[t - 3000, t]$ is inclusive, $t_1$ is retained.
- Large gap between pings ($t_{k+1} - t_k > 3000$): the while loop clears all previous elements, leaving only the newly added ping.
- Bursts of pings close together: all pings within 3000 ms are retained and accurately counted.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
from collections import deque


class RecentCounter:
    """Counts recent calls within a 3000 ms sliding window."""

    WINDOW_SIZE: int = 3000

    def __init__(self) -> None:
        """Initialize the counter with an empty window of requests."""
        self._requests: deque[int] = deque()

    def ping(self, t: int) -> int:
        """Record ping at time t and return count in [t - 3000, t]."""
        self._requests.append(t)
        min_time = t - self.WINDOW_SIZE
        while self._requests and self._requests[0] < min_time:
            self._requests.popleft()
        return len(self._requests)
```
