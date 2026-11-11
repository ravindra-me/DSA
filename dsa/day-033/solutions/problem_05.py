import heapq


def external_k_way_sort(stream: list[int], chunk_size: int) -> list[int]:
    """Simulates external merge sort using chunked runs and a min-heap k-way merge."""
    if not stream or chunk_size <= 0:
        return []

    # Phase 1: Run generation
    runs: list[list[int]] = []
    for i in range(0, len(stream), chunk_size):
        chunk = stream[i : i + chunk_size]
        chunk.sort()
        runs.append(chunk)

    # Phase 2: K-Way merge
    # Min-heap stores: (value, run_index, element_index)
    min_heap: list[tuple[int, int, int]] = []
    for run_idx, run in enumerate(runs):
        if run:
            min_heap.append((run[0], run_idx, 0))

    heapq.heapify(min_heap)

    merged: list[int] = []
    while min_heap:
        val, run_idx, elem_idx = heapq.heappop(min_heap)
        merged.append(val)
        next_elem_idx = elem_idx + 1
        if next_elem_idx < len(runs[run_idx]):
            heapq.heappush(min_heap, (runs[run_idx][next_elem_idx], run_idx, next_elem_idx))

    return merged
