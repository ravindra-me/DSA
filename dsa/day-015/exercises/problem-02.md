# Problem 2: Recent Calls Counter

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Fixed time-window eviction using deque | [Day 15: Deque & Monotonic Queue](../README.md) |

## Problem Statement

Design a class `RecentCounter` that counts the number of recent requests within a sliding time window.

Implement the `RecentCounter` class:
- `RecentCounter()`: Initializes the counter with zero requests.
- `ping(t: int) -> int`: Adds a new request at time `t` (in milliseconds) and returns the number of requests that have happened in the inclusive range `[t - 3000, t]`.

It is guaranteed that every call to `ping` uses a strictly larger value of `t` than the previous call.

## Input

Calls to `RecentCounter()` and `ping(t)` where `t` is a positive integer.

## Output

Integer count of requests within `[t - 3000, t]`.

## Constraints

- 1 <= t <= 10^9
- Each call to ping has strictly increasing t.
- At most 10^5 calls will be made to ping.

## Examples

**Example 1**

```text
Input:  counter = RecentCounter(); counter.ping(1); counter.ping(100); counter.ping(3001); counter.ping(3002)
Output: 1, 2, 3, 3
```

ping(1) -> [1] (1)
ping(100) -> [1, 100] (2)
ping(3001) -> [1, 100, 3001] (3)
ping(3002) -> 1 is outside [2, 3002], so [100, 3001, 3002] (3)

**Example 2**

```text
Input:  counter = RecentCounter(); counter.ping(10); counter.ping(4000)
Output: 1, 1
```

At t=4000, window is [1000, 4000], so 10 is evicted, leaving only [4000].

## Function Signature

```python
class RecentCounter:
    def __init__(self) -> None:
        """Initialize the counter."""

    def ping(self, t: int) -> int:
        """Record ping at time t and return count in [t - 3000, t]."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Store timestamps in a deque. For every `ping(t)`, append `t`, pop all elements smaller than `t - 3000` from the front, and return the size of the deque.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
