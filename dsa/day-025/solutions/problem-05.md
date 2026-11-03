# Solution 5: Stream Peak Detection

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Stateful streaming linear search over infinite dynamic window

## Approach

To detect a peak in a streaming context, we maintain a fixed-size window of the most recent three values: `prev_prev`, `prev`, and the incoming `curr`. A peak is detected at `prev` if and only if `prev_prev < prev` and `prev > curr` (strictly greater).

## Thought Process

In a static array, a peak at index $i$ requires checking $A[i-1] < A[i]$ and $A[i] > A[i+1]$. In a stream, we cannot know if $A[i]$ is a peak until $A[i+1]$ arrives. Therefore, we delay reporting the status of $A[i]$ by one time step. We only need to store the previous two values seen in the stream, giving an optimal $O(1)$ time complexity per stream element and $O(1)$ auxiliary space.

## Algorithm

1. Initialize state variables `prev_prev` and `prev` to `None`.
2. When `process(val)` is called:
3. If both `prev_prev` and `prev` are not `None`, check if `prev_prev < prev` and `prev > val`.
4. If the peak condition holds, record `prev` as the peak value to return.
5. Shift the stream history: update `prev_prev = prev` and `prev = val`.
6. Return the detected peak value if found, otherwise return `None`.

## Complexity Analysis

- **Time:** $O(1)$ per `process` call. Each stream element undergoes a constant number of operations.
- **Space:** $O(1)$ auxiliary memory. Only two scalar values (`prev_prev` and `prev`) are stored.

## Edge Cases

- Fewer than 3 elements processed: Cannot form a peak; returns `None`.
- Equal adjacent elements: Peak condition strictly requires `prev_prev < prev` and `prev > curr`, so duplicate values naturally invalidate peak status.
- Negative numbers and bounds: Handled correctly by standard comparison operations.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
class StreamPeakFinder:
    """Detects local peaks in a stream of numbers using a sliding 3-element window."""

    def __init__(self):
        self._prev_prev: int | None = None
        self._prev: int | None = None

    def process(self, val: int) -> int | None:
        """Process a new stream value and return a peak if finalized, else None."""
        peak = None
        if self._prev_prev is not None and self._prev is not None:
            if self._prev_prev < self._prev and self._prev > val:
                peak = self._prev

        self._prev_prev = self._prev
        self._prev = val
        return peak
```
