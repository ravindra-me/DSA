def min_completion_time(jobs: list[int], k: int) -> int:
    """Find the minimum possible maximum workload in O(n log(sum)) time and O(1) space."""
    if not jobs:
        return 0

    low = max(jobs)
    high = sum(jobs)

    def can_partition(max_load: int) -> bool:
        workers_used = 1
        current_load = 0
        for job in jobs:
            if current_load + job > max_load:
                workers_used += 1
                current_load = job
                if workers_used > k:
                    return False
            else:
                current_load += job
        return True

    while low < high:
        mid = (low + high) // 2
        if can_partition(mid):
            high = mid
        else:
            low = mid + 1

    return low
