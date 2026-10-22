# Solution 5: Bounded Producer-Consumer Buffer Simulator

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Bounded queue simulation with buffer overflow shedding and consumer latency

## Approach

We maintain a FIFO queue of task finish times representing tasks currently in progress or waiting in the buffer. When a new task arrives at `arrival_time`, we first pop all tasks from the front of the queue whose finish times are $\le$ `arrival_time`. If the remaining queue length exceeds `capacity` (note: 1 task being executed + up to `capacity` waiting tasks means max queue size is `capacity + 1`), the buffer is full and the task is dropped. Otherwise, the task's start time is $\max(\text{arrival\_time}, \text{finish time of previous task})$, its finish time is $\text{start time} + \text{duration}$, and this finish time is pushed onto the queue.

## Thought Process

A naive discrete-event simulation might step forward unit-by-unit in time, which would take $O(\max(T))$ time—completely infeasible given timestamps up to $10^9$. Instead, we jump from event to event, driven by task arrivals.

Notice that each task finishes at a deterministic time once started, and tasks are executed strictly in FIFO order. If we record the finish times of tasks currently in the system:
1. The head of this queue is the task currently running on the worker.
2. The remaining elements are tasks waiting in the bounded buffer.

When a task arrives at time $t$:
- Any task with finish time $\le t$ has completed execution by time $t$. We dequeue all such tasks.
- If the queue is empty, the worker is idle; the task starts immediately at $t$ and finishes at $t + d$.
- If the queue is not empty, the task at the head is actively executing. The number of tasks waiting in the queue is `len(queue) - 1`. Therefore, if `len(queue) - 1 == capacity` (or equivalently `len(queue) > capacity`), the buffer is full, and the arriving task must be dropped (`-1`).
- If there is buffer space, this task will begin right after the last task currently scheduled (the back of the queue) finishes at $T_{\text{last}}$. Its finish time will be $T_{\text{last}} + d$. We append this finish time to the queue and record it.

## Algorithm

1. Initialize an empty list `results` of size `len(tasks)`.
2. Initialize a double-ended queue `queue` to store finish times of tasks currently in service or in the waiting buffer.
3. Iterate through `tasks` with index `i` and `(arrival_time, duration)`.
4. While `queue` is not empty and `queue[0] <= arrival_time`, pop the left element from `queue`.
5. If `len(queue) == 0`: the worker is idle. Set `finish_time = arrival_time + duration`. Append `finish_time` to `queue` and record `results[i] = finish_time`.
6. Else if `len(queue) <= capacity`: the worker is busy but the waiting queue has room (`len(queue) - 1 < capacity`). Set `finish_time = queue[-1] + duration`. Append `finish_time` to `queue` and record `results[i] = finish_time`.
7. Else (`len(queue) > capacity`): the waiting queue is full. Record `results[i] = -1` (dropped).
8. Return `results`.

## Complexity Analysis

- **Time:** O(N) where N is the number of tasks. Each task is added to and removed from the deque at most once.
- **Space:** O(N) to store the results list, and O(min(N, capacity)) for the deque storing active/waiting finish times.

## Edge Cases

- Empty task list: Returns an empty list immediately.
- Capacity = 0 or 1: With capacity = 1, at most 1 task can wait while 1 executes (queue size up to 2).
- Simultaneous arrivals: If multiple tasks arrive at the same timestamp, tasks arriving earlier process completions up to that timestamp, and subsequent tasks correctly see the updated queue state.
- Large gaps between arrivals: Handled naturally because all prior tasks finish before the new arrival, leaving the queue empty and the worker idle.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
from collections import deque

def simulate_task_pipeline(capacity: int, tasks: list[tuple[int, int]]) -> list[int]:
    """Simulate bounded producer-consumer queue and return finish times."""
    results: list[int] = [-1] * len(tasks)
    # queue stores the finish times of tasks currently being processed or waiting
    finish_times: deque[int] = deque()

    for i, (arrival, duration) in enumerate(tasks):
        # Evict all tasks that finished at or before the current arrival time
        while finish_times and finish_times[0] <= arrival:
            finish_times.popleft()

        if not finish_times:
            # Worker is idle
            end_time = arrival + duration
            finish_times.append(end_time)
            results[i] = end_time
        elif len(finish_times) <= capacity:
            # Worker is busy, but waiting queue has room (< capacity waiting tasks)
            end_time = finish_times[-1] + duration
            finish_times.append(end_time)
            results[i] = end_time
        else:
            # Waiting queue is full (len(finish_times) == capacity + 1)
            results[i] = -1

    return results
```
