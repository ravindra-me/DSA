# Problem 5: Optimal Budget Job Scheduler

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Binary Search on Answer with O(N log(Sum)) runtime complexity | [Day 41: Big O Notation & Complexity Analysis](../README.md) |

## Problem Statement

You are given an array of non-negative integers `jobs` where `jobs[i]` represents the processing time of the $i$-th job, and an integer `k` representing the number of available workers. All jobs must be processed sequentially by assigning contiguous segments of jobs to workers (each worker takes a contiguous subarray of jobs). Each worker can work concurrently, but cannot be assigned non-contiguous tasks.

The completion time of the entire schedule is the maximum total time assigned to any single worker. Determine the minimum possible completion time to complete all jobs with at most `k` workers.

Your solution must run in $O(n \log(\sum \text{jobs}))$ time and $O(1)$ auxiliary space.

## Input

A list of non-negative integers `jobs` and an integer `k` (`1 <= k <= len(jobs)`).

## Output

An integer representing the minimized maximum workload among workers.

## Constraints

- 1 <= k <= len(jobs) <= 10^5
- 0 <= jobs[i] <= 10^9
- k <= len(jobs)

## Examples

**Example 1**

```text
Input:  jobs = [1, 2, 3, 4, 5], k = 2
Output: 9
```

Partition jobs into [1, 2, 3] (sum 6) and [4, 5] (sum 9). The maximum load is 9.

**Example 2**

```text
Input:  jobs = [10, 20, 30], k = 3
Output: 30
```

Each worker takes one job. Max load is 30.

## Function Signature

```python
def min_completion_time(jobs: list[int], k: int) -> int:
    """Find the minimum possible maximum workload in O(n log(sum)) time and O(1) space."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Binary search on the answer in the range [max(jobs), sum(jobs)] and use a greedy linear scan to verify if k workers suffice.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
