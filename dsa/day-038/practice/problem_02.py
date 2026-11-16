def batch_tasks(batch_size: int, max_wait_time: int, tasks: list[tuple[int, str]]) -> list[list[str]]:
    """Flushes tasks in FIFO batches by capacity or timeout."""
    raise NotImplementedError
