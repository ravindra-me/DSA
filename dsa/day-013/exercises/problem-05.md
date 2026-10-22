# Problem 5: Bounded Producer-Consumer Buffer Simulator

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Bounded queue simulation with buffer overflow shedding and consumer latency | [Day 13: Queue](../README.md) |

## Problem Statement

Simulate a multi-tasking producer-consumer system with a single worker thread and a bounded queue of capacity `capacity`.

You are given a list of `tasks`, where each task is represented by a tuple `(arrival_time, duration)`. Tasks are sorted in non-decreasing order of `arrival_time`. If two tasks arrive at the same time, they arrive in the order given in the list.

System Rules:
1. The worker can only process one task at a time. Once started, a task cannot be interrupted and takes exactly `duration` units of time.
2. The system maintains a bounded FIFO queue of capacity `capacity` to hold tasks waiting to be processed.
3. When a task arrives at `arrival_time`:
   - Any task currently being processed that finishes at or before `arrival_time` completes, and the worker immediately begins the next task from the queue (if any).
   - If the worker is idle upon arrival (no task currently running and queue is empty), the task starts execution immediately at `start_time = arrival_time`.
   - If the worker is busy, the task tries to enter the waiting queue. If the waiting queue already has `capacity` tasks, the incoming task is **dropped** (represented by a completion time of `-1`). Otherwise, it is appended to the waiting queue.
4. Whenever the worker finishes a task at time `T`, it immediately pulls the next task from the waiting queue (if non-empty) and starts it at time `T`.

Return a list of integers where the $i$-th integer is the time task $i$ **finished execution**, or `-1` if task $i$ was dropped.

## Input

- `capacity: int`: Maximum number of tasks the waiting queue can hold.
- `tasks: list[tuple[int, int]]`: List of `(arrival_time, duration)` pairs.

## Output

`list[int]`: Completion time for each task in input order, with `-1` for dropped tasks.

## Constraints

- 1 <= capacity <= 10^5
- 0 <= len(tasks) <= 10^5
- 0 <= arrival_time <= 10^9
- 1 <= duration <= 10^9
- tasks is sorted by arrival_time.

## Examples

**Example 1**

```text
Input:  capacity = 1, tasks = [(0, 5), (1, 3), (2, 4), (5, 2)]
Output: [5, 8, -1, 10]
```

Task 0 arrives at 0, worker idle -> starts at 0, finishes at 5. Task 1 arrives at 1, worker busy -> queue = [Task 1] (size 1/1). Task 2 arrives at 2, queue full -> dropped (-1). At time 5, Task 0 finishes. Worker starts Task 1 from queue (runs 5 to 8). Task 3 arrives at 5, worker busy -> queue has space, queue = [Task 3]. Task 1 finishes at 8; Task 3 runs 8 to 10.

**Example 2**

```text
Input:  capacity = 2, tasks = []
Output: []
```

An empty task list returns an empty completion list.

## Function Signature

```python
from collections import deque

def simulate_task_pipeline(capacity: int, tasks: list[tuple[int, int]]) -> list[int]:
    """Simulate bounded producer-consumer queue and return finish times."""
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Simulate time progression using a FIFO queue of task finish times or track `worker_available_time` alongside a queue holding task durations.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
