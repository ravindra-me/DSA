# Solution 5: Optimal Budget Job Scheduler

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Binary Search on Answer with O(N log(Sum)) runtime complexity

## Approach

Use binary search on the answer (the maximum workload allocated to any worker). For any candidate completion time `mid`, greedily verify if the jobs can be partitioned into at most `k` contiguous subarrays whose sums do not exceed `mid`.

## Thought Process

A brute-force solution would consider all $\binom{n-1}{k-1}$ ways to partition the $n$ jobs into $k$ contiguous segments and pick the minimum of the maximum sum, which is combinatorial and intractable for $n = 10^5$.

Notice the monotonicity property: if it is possible to allocate jobs such that no worker exceeds time $T$, then it is also possible for any time $T' > T$. Conversely, if $T$ is impossible, any $T'' < T$ is also impossible. This monotonic predicate allows binary searching over the range of possible answers.

The search range is $[\max(\text{jobs}), \sum \text{jobs}]$ (or $0$ if jobs is empty). For a chosen threshold $T$, we greedily allocate contiguous tasks to the current worker until adding the next task exceeds $T$, at which point we advance to a new worker. If the number of workers needed is $\le k$, the threshold $T$ is feasible, so we search the lower half; otherwise, we search the upper half.

## Algorithm

1. Handle empty input edge case: if `jobs` is empty, return 0.
2. Initialize search boundaries: `low = max(jobs)` and `high = sum(jobs)`.
3. Define a helper function `can_partition(max_load)`: iterate through `jobs`, accumulating current worker's load. If adding the next job exceeds `max_load`, increment worker count and reset current load to this job. If worker count exceeds `k`, return False. Return True if all jobs fit into at most `k` workers.
4. Perform binary search while `low < high`: compute `mid = (low + high) // 2`. If `can_partition(mid)` is True, search lower half (`high = mid`); else search upper half (`low = mid + 1`).
5. Return `low` when search concludes.

## Complexity Analysis

- **Time:** O(n log(S)) where n is len(jobs) and S is sum(jobs). Each check runs in O(n) time, and the binary search range is at most S, requiring log2(S) iterations.
- **Space:** O(1) auxiliary space as only a few variables are maintained for the binary search and the greedy check.

## Edge Cases

- Empty `jobs` list: returns 0 immediately.
- k == len(jobs): each worker gets at most 1 job, answer is max(jobs).
- k == 1: a single worker must do all jobs, answer is sum(jobs).
- All jobs are 0: binary search gracefully handles low=0, high=0 and returns 0.
- Large values up to 10^9: Python handles arbitrarily large integers without overflow.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
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
```
