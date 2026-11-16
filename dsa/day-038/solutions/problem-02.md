# Solution 2: FIFO Task Batcher with Capacity and Timeout

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Medium | **Concept:** Queue batch aggregation with timestamp and capacity flushing

## Approach

Maintain a queue (or list buffer) representing the current pending batch of tasks. For each incoming `(timestamp, task_id)`, check if the queue is non-empty and whether the elapsed time `current_timestamp - oldest_task_timestamp` is at least `max_wait_time`. If so, flush the entire pending queue as a batch. Next, append the incoming task to the queue. If the queue's length reaches `batch_size`, immediately flush it. Finally, after iterating through all tasks, flush any remaining tasks in the queue.

## Thought Process

A naive or simulation approach might step through time unit by unit, but `timestamp` can reach $10^9$, making time-stepping infeasible. Instead, events only happen upon arrival of each task. Tasks arrive in non-decreasing order of timestamp, so we process them linearly.

At each arrival, the two flushing rules dictate precise precedence:
1. Timeout check: If there are tasks already queued, we compare the current task's timestamp with the timestamp of the oldest task (at the front of the queue). If `curr_ts - oldest_ts >= max_wait_time`, the existing pending tasks have timed out and must be dispatched before accepting the new task.
2. Admission and capacity check: Once any expired batch is cleared, the new task is admitted into the queue. If admitting this task causes the queue size to reach `batch_size`, the batch is full and must be dispatched immediately.

Because tasks are flushed in FIFO order and batches are flushed as a whole, a simple dynamic list or `collections.deque` allows $O(1)$ operations per element, yielding an optimal $O(N)$ overall time complexity.

## Algorithm

1. Initialize an empty list `batches` to store the output batches.
2. Initialize an empty list or deque `current_batch` to store pending task tuples `(timestamp, task_id)`.
3. For each incoming task `(ts, task_id)` in `tasks`:
4. Check if `current_batch` is not empty and `ts - current_batch[0][0] >= max_wait_time`. If true, append `[tid for _, tid in current_batch]` to `batches` and clear `current_batch`.
5. Append `(ts, task_id)` to `current_batch`.
6. If `len(current_batch) == batch_size`, append `[tid for _, tid in current_batch]` to `batches` and clear `current_batch`.
7. After iterating through all tasks, if `current_batch` is not empty, append `[tid for _, tid in current_batch]` to `batches`.
8. Return `batches`.

## Complexity Analysis

- **Time:** O(N) where N is the number of tasks. Each task is added to a batch exactly once and extracted into a flushed batch list exactly once.
- **Space:** O(N) to store the result batches and at most O(batch_size) auxiliary space for the active queue at any point.

## Edge Cases

- Empty task list: Returns an empty list immediately without entering loops.
- Single task: Flushed in the final flush step as a single-element batch (or immediately if `batch_size == 1`).
- `batch_size == 1`: Every task is flushed immediately upon arrival into its own single-element batch.
- Simultaneous arrivals (`timestamp_i == timestamp_{i+1}`): `elapsed_time = 0 < max_wait_time`, so timeout will not trigger; capacity trigger operates normally.
- Large `max_wait_time` or large `timestamp` differences: Handled correctly since difference calculations use 64-bit integer arithmetic in Python without overflow.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def batch_tasks(batch_size: int, max_wait_time: int, tasks: list[tuple[int, str]]) -> list[list[str]]:
    """Flushes tasks in FIFO batches by capacity or timeout."""
    batches: list[list[str]] = []
    current_batch: list[tuple[int, str]] = []

    for ts, task_id in tasks:
        # Check if the pending batch timed out before admitting the new task
        if current_batch and (ts - current_batch[0][0]) >= max_wait_time:
            batches.append([item[1] for item in current_batch])
            current_batch = []

        # Admit the current task
        current_batch.append((ts, task_id))

        # Check if batch reached capacity
        if len(current_batch) == batch_size:
            batches.append([item[1] for item in current_batch])
            current_batch = []

    # Flush any remaining tasks
    if current_batch:
        batches.append([item[1] for item in current_batch])

    return batches
```
