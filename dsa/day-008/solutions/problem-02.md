# Solution 2: Continuous Resettable Counter

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Medium | **Concept:** Amortized state updates with lazy propagation

## Approach

We maintain a global timestamp counter and record both the baseline value and timestamp for the most recent `set_all` operation. Each individual counter tracks its own value and the timestamp when it was last modified. When reading or updating an element whose timestamp predates the latest `set_all`, we lazily reset it to the baseline before proceeding, achieving worst-case $O(1)$ time per operation.

## Thought Process

A naive approach updates every element in the array during `set_all(val)`, costing $O(n)$ time per reset. Across $m$ operations, this leads to an unacceptable $O(m \cdot n)$ total time complexity.

To achieve $O(1)$ worst-case time for `set_all`, we must avoid visiting every element. Instead, we can record the operation globally: store a `set_all_val` along with a logical clock or timestamp `set_all_time`.

Each index $i$ stores its value `values[i]` and the timestamp `update_time[i]` of its last direct update. Whenever an index is accessed (`get` or `increment`), we compare `update_time[i]` to `set_all_time`. If `update_time[i] < set_all_time`, the index was overwritten by a subsequent `set_all`, meaning its effective current value is `set_all_val`. For `increment`, we first resolve the lazy reset, add 1, and update `update_time[i]` to the current clock cycle.

## Algorithm

1. Initialize `values` array of size $n$ with zeros and `update_time` array of size $n$ with 0.
2. Maintain a global operation counter `current_time = 0`, a global reset value `set_all_val = 0`, and the timestamp of the latest reset `set_all_time = 0`.
3. For `set_all(val)`: increment `current_time`, set `set_all_val = val`, and set `set_all_time = current_time` in $O(1)$ time.
4. For `get(i)`: if `update_time[i] < set_all_time`, return `set_all_val`; otherwise, return `values[i]`.
5. For `increment(i)`: increment `current_time`. Check if `update_time[i] < set_all_time`. If so, set `values[i] = set_all_val + 1`; otherwise, set `values[i] = values[i] + 1`. In both cases, update `update_time[i] = current_time`.

## Complexity Analysis

- **Time:** O(1) worst-case time for __init__, increment, set_all, and get. Each operation does a constant number of comparisons and assignments.
- **Space:** O(n) space to store two lists of size n: values and update_time.

## Edge Cases

- size = 1: Single counter operates normally without boundary errors.
- Initial get before any modifications: Returns 0 since initial update_time equals set_all_time and values start at 0.
- Multiple consecutive set_all operations: Each overwrites set_all_val and advances set_all_time, correctly superseding older values.
- val = 0 in set_all: Correctly updates baseline even though 0 matches initial values.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
class ResettableCounters:
    """A fixed-size array of counters with O(1) increment, get, and set_all operations."""

    def __init__(self, size: int) -> None:
        """Initialize size counters with 0."""
        self._size: int = size
        self._values: list[int] = [0] * size
        self._update_time: list[int] = [0] * size
        self._current_time: int = 0
        self._set_all_val: int = 0
        self._set_all_time: int = 0

    def increment(self, i: int) -> None:
        """Add 1 to counter i in O(1) worst-case time."""
        self._current_time += 1
        if self._update_time[i] < self._set_all_time:
            self._values[i] = self._set_all_val + 1
        else:
            self._values[i] += 1
        self._update_time[i] = self._current_time

    def set_all(self, val: int) -> None:
        """Set all counters to val in O(1) worst-case time."""
        self._current_time += 1
        self._set_all_val = val
        self._set_all_time = self._current_time

    def get(self, i: int) -> int:
        """Return the value of counter i in O(1) worst-case time."""
        if self._update_time[i] < self._set_all_time:
            return self._set_all_val
        return self._values[i]
```
