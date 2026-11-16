# Solution 1: First Unique Character in Dynamic Stream

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy/Medium | **Concept:** FIFO queue with frequency counting for streaming order preservation

## Approach

We track character frequencies using a hash map (or fixed-size counter array) and maintain candidate first unique characters in arrival order using a FIFO queue (`collections.deque`). When queried, we lazily pop non-unique characters (frequency > 1) from the front of the queue until we find one with frequency 1 or the queue is exhausted.

## Thought Process

A naive approach might store all received characters in a dynamic array and on each `get_first_unique()` call scan from left to right, checking counts. That yields $O(N)$ per query, resulting in $O(N^2)$ overall across $10^5$ operations.

To improve this, notice two key properties:
1. FIFO order must be respected for reporting the *first* unique.
2. Once a character's frequency exceeds 1, it can never become unique again.

Hence, we can push newly encountered characters to a queue. During `get_first_unique()`, we examine the front of the queue. If the front character has a frequency greater than 1, it is permanently invalidated and can be popped (`popleft()`). Because each character is pushed at most once (or once per occurrence) and popped at most once over its lifetime, the amortized cost per operation is $O(1)$. Furthermore, since there are only 26 lowercase English letters, at most 26 distinct characters can ever be pushed to the queue if we only push upon the first occurrence.

## Algorithm

1. Initialize `counts` as a dictionary (or array of size 26) mapping each character to its occurrence count.
2. Initialize `queue` as a double-ended queue (`collections.deque`) to store characters in arrival order.
3. In `add(ch)`: increment `counts[ch]`. If `counts[ch] == 1`, append `ch` to `queue` (only first occurrences need to be queued).
4. In `get_first_unique()`: while `queue` is not empty and `counts[queue[0]] > 1`, pop from the front of `queue` (`queue.popleft()`).
5. If `queue` is not empty, return `queue[0]`; otherwise, return `""`.

## Complexity Analysis

- **Time:** Amortized $O(1)$ for both `add` and `get_first_unique`. Each of the 26 lowercase English letters is pushed to the queue at most once and popped at most once.
- **Space:** $O(1)$ auxiliary space beyond the fixed alphabet size ($|\Sigma| \le 26$), since the counter and the queue hold at most 26 unique characters.

## Edge Cases

- Empty stream: `get_first_unique()` called before any characters added returns `""`.
- All characters become duplicate: the queue drains completely and returns `""`.
- Immediate duplicate: e.g., 'a' then 'a' - becomes duplicate without any intervening characters.
- Large stream of identical characters: count increments efficiently without queue bloat if only pushed when count is 1.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
from collections import deque


class StreamFirstUnique:
    def __init__(self) -> None:
        """Initialize the stream data structure."""
        self._counts: dict[str, int] = {}
        self._queue: deque[str] = deque()

    def add(self, ch: str) -> None:
        """Add character ch to the stream."""
        new_count = self._counts.get(ch, 0) + 1
        self._counts[ch] = new_count
        if new_count == 1:
            self._queue.append(ch)

    def get_first_unique(self) -> str:
        """Return the first unique character in the stream, or empty string."""
        while self._queue and self._counts[self._queue[0]] > 1:
            self._queue.popleft()
        return self._queue[0] if self._queue else ""
```
