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
