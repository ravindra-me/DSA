# Solution 3: Recent Calls Rate Limiter

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Sliding window time-series queue

## Approach

Maintain a FIFO queue (`collections.deque`) of incoming request timestamps. For each call to `ping(t)`, append `t` to the queue and repeatedly pop timestamps from the front that are strictly less than `t - 3000`. The number of elements remaining in the queue is the exact number of requests in the range `[t - 3000, t]`.

## Thought Process

A brute-force approach would store every timestamp in a list and, on every `ping(t)`, scan through the list (or run a binary search) to count how many timestamps fall within `[t - 3000, t]`. While binary search is $O(\log N)$, storing all timestamps incurs $O(N)$ space over time, and a linear scan would take $O(N)$ per call leading to $O(N^2)$ overall.

Because timestamps arrive in strictly increasing order, any timestamp that falls outside the window `[t - 3000, t]` will also fall outside any future window `[t' - 3000, t']` where $t' > t$. Thus, expired timestamps will never be counted again and can be discarded immediately.

A double-ended queue (deque) allows $O(1)$ amortized push to the back and pop from the front. Each timestamp is added once and removed at most once across the lifetime of the counter, yielding $O(1)$ amortized time per `ping` and $O(W)$ space, where $W$ is the maximum number of requests within any 3000 ms window.

## Algorithm

1. Initialize an empty double-ended queue `requests` during `__init__`.
2. When `ping(t)` is called, push `t` to the right end of `requests`.
3. While `requests` is non-empty and `requests[0] < t - 3000`, pop the left element from `requests`.
4. Return the length of `requests`.

## Complexity Analysis

- **Time:** $O(1)$ amortized per `ping`. Each timestamp is appended to the deque once and popped from the deque at most once across all calls.
- **Space:** $O(W)$ auxiliary space, where $W$ is the maximum number of requests that fall within any 3000 ms sliding window (bounded by at most 3001 if timestamps were discrete integer increments, and at most $N$ in general).

## Edge Cases

- First call to ping: the deque is initially empty; adding one timestamp results in a count of 1 without popping.
- Timestamp exactly at boundary: when `t_prev == t - 3000`, the condition `requests[0] < t - 3000` is false, so `t_prev` is preserved (inclusive boundary).
- Timestamp at `t_prev == t - 3001`: correctly pruned as it is strictly less than `t - 3000`.
- Sparse requests: calls separated by more than 3000 ms (e.g., $t=1$ then $t=4000$) will evict all previous timestamps, returning 1.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
from collections import deque


class RecentCounter:
    """Counts the number of recent requests within a 3000 ms sliding window."""

    def __init__(self) -> None:
        """Initialize the counter with an empty timestamp queue."""
        self._requests: deque[int] = deque()

    def ping(self, t: int) -> int:
        """Record request at time t and return count in [t - 3000, t]."""
        self._requests.append(t)
        min_time = t - 3000
        while self._requests and self._requests[0] < min_time:
            self._requests.popleft()
        return len(self._requests)
```
