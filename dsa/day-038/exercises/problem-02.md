# Problem 2: FIFO Task Batcher with Capacity and Timeout

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Queue batch aggregation with timestamp and capacity flushing | [Day 38: Queue](../README.md) |

## Problem Statement

In a backend service, incoming events arrive as pairs `(timestamp, task_id)` in non-decreasing order of `timestamp`. To optimize network requests, tasks must be batched together and dispatched under two conditions:
1. As soon as the queue accumulates `batch_size` tasks, those `batch_size` tasks are flushed immediately as a batch at that arrival timestamp.
2. If the duration between the arrival timestamp of the oldest pending task in the queue and the current task's timestamp exceeds or equals `max_wait_time`, all pending tasks in the queue must be flushed before the new task is admitted.
3. Any remaining tasks after all inputs have been processed are flushed together in a final batch at the timestamp of the last flushed task (or their arrival timestamp if no flush occurred).

Given `batch_size`, `max_wait_time`, and a list of `tasks` where each task is `(timestamp, task_id)`, return a list of batches, where each batch is a list of `task_id` strings.

## Input

An integer `batch_size`, an integer `max_wait_time`, and a list of tuples `tasks: list[tuple[int, str]]`.

## Output

A list of lists of strings: `list[list[str]]` containing the task IDs in each flushed batch.

## Constraints

- 1 <= batch_size <= 1000
- 1 <= max_wait_time <= 10^9
- 0 <= len(tasks) <= 10^4
- 0 <= timestamp <= 10^9
- tasks are sorted such that timestamp_i <= timestamp_{i+1}.

## Examples

**Example 1**

```text
Input:  batch_size = 3, max_wait_time = 10, tasks = [(1, "t1"), (3, "t2"), (11, "t3"), (12, "t4")]
Output: [["t1", "t2"], ["t3", "t4"]]
```

At timestamp 11, the oldest task is t1 at timestamp 1. Age is 11 - 1 = 10 >= max_wait_time (10). Thus [t1, t2] is flushed before t3 is enqueued. Later, [t3, t4] are flushed at termination.

**Example 2**

```text
Input:  batch_size = 2, max_wait_time = 5, tasks = []
Output: []
```

Empty input produces no batches.

## Function Signature

```python
def batch_tasks(batch_size: int, max_wait_time: int, tasks: list[tuple[int, str]]) -> list[list[str]]:
    """Flushes tasks in FIFO batches by capacity or timeout."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Simulate FIFO queues checking the head timestamp against the current event to trigger timeout flushes, followed by capacity checks on enqueue. Target O(N) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
