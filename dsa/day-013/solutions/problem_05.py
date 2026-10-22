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
