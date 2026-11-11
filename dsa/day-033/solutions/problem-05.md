# Solution 5: Simulate External K-Way Merge Sort

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Chunk-based external sorting and multiway merging with bounded memory buffer

## Approach

Divide the input stream into chunks of size at most `chunk_size` and sort each in memory to create initial runs. Then, use a min-heap initialized with the first element of each run along with its run index and element offset to perform a $k$-way merge, repeatedly extracting the minimum element and pushing the next element from that same run until all runs are exhausted.

## Thought Process

In external sorting, the dataset exceeds main memory capacity, so it cannot be sorted entirely in RAM at once. The canonical solution has two phases:

1. **Run Generation**: Stream data into memory buffers of size $M = \text{chunk\_size}$, sort each buffer (e.g., using merge sort or Timsort), and write the sorted run back to secondary storage (simulated here as a list of lists).
2. **Multiway Merge**: To combine $k = \lceil N / M \rceil$ sorted runs, load the smallest unmerged element from each run into a min-heap of size at most $k$. The root of the heap contains the overall smallest element. Pop it, append it to the final output, and insert the next element from the run that contributed the popped value.

A naive approach might concatenate all runs and sort again or merge runs pairwise repeatedly (which requires $O(\log k)$ passes over the data). Using a priority queue enables merging all $k$ runs in a single pass with $O(N \log k)$ comparisons.

## Algorithm

1. Check if `stream` is empty; if so, return `[]`.
2. Partition `stream` into consecutive chunks of size `chunk_size`. For each chunk, sort it in ascending order to create a run.
3. Initialize a min-heap with tuples `(val, run_idx, elem_idx)` representing the first element (`elem_idx = 0`) of each run `run_idx`.
4. Initialize an empty result list `merged`.
5. While the min-heap is non-empty: pop `(val, run_idx, elem_idx)` from the heap and append `val` to `merged`.
6. If `elem_idx + 1 < len(runs[run_idx])`, push `(runs[run_idx][elem_idx + 1], run_idx, elem_idx + 1)` into the heap.
7. Return `merged` once the heap is empty.

## Complexity Analysis

- **Time:** O(N log(chunk_size) + N log k) where N = len(stream) and k = ceil(N / chunk_size). Sorting k chunks of size M takes O(k * M log M) = O(N log M). Merging N elements using a heap of size at most k takes O(N log k). Overall time is O(N log(chunk_size) + N log k) = O(N log N).
- **Space:** O(N) to store the runs and output in this in-memory simulation, with the merge min-heap occupying O(k) additional space where k = ceil(N / chunk_size).

## Edge Cases

- Empty stream: `stream = []` immediately returns `[]`.
- Stream smaller than or equal to `chunk_size`: produces only 1 run; the min-heap holds 1 item and simply empties the run into the result.
- Duplicate elements: min-heap tuples compare cleanly; duplicates in values are broken by run and element index.
- Negative numbers and zeros: handled naturally by numeric comparison.
- Non-multiple chunk sizes: the final chunk is shorter than `chunk_size`, which is handled safely by bounds checks.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
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
```
