# Solution 4: Uniform Bucket Sort

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Bucket Sort with uniform distribution normalization

## Approach

Bucket Sort partitions the input interval $[0.0, 1.0)$ into $n$ equal-width sub-intervals (buckets). Each element $x$ is placed into bucket index $\lfloor n \cdot x \rfloor$. Under a uniform distribution, the expected number of elements per bucket is $O(1)$, so sorting each bucket with insertion sort (or Python's Timsort) takes expected $O(1)$ time per bucket. Concatenating all sorted buckets yields the completely sorted array in expected linear time.

## Thought Process

Comparison-based sorts (like mergesort or quicksort) require $\Omega(n \log n)$ time in the worst and average cases. However, when we have distributional information—specifically, that inputs are drawn uniformly and independently from $[0.0, 1.0)$—we can break the comparison-sort barrier.

By dividing the range into $n$ contiguous sub-intervals $[0, 1/n), [1/n, 2/n), \dots, [(n-1)/n, 1)$, every number $x$ can be routed in $O(1)$ time to bucket index $b = \lfloor n \cdot x \rfloor$. Because all elements in bucket $i$ are strictly less than all elements in bucket $j$ for $i < j$, we only need to sort within each bucket and concatenate. When the input is uniformly distributed, the bucket sizes follow a binomial distribution $B(n, 1/n)$. The expected time spent sorting each bucket of size $k$ using an $O(k^2)$ sort is $E[O(k^2)] = O(1)$, leading to total expected runtime $\sum_{i=0}^{n-1} O(1) = O(n)$.

## Algorithm

1. Check if len(nums) <= 1; if so, return a copy of nums immediately.
2. Initialize $n$ empty buckets (lists), where $n = \text{len}(nums)$.
3. For each value $x$ in `nums`, compute its bucket index as `int(x * n)`. Clamp index to $n - 1$ if floating-point inaccuracies cause `int(x * n) == n`.
4. Append each value to its corresponding bucket.
5. Iterate through each bucket, sort it using insertion sort, and append the sorted values to a result list.
6. Return the assembled result list.

## Complexity Analysis

- **Time:** Average: $O(n)$. For uniform distribution, each bucket has expected size $O(1)$, so sorting takes expected $O(1)$ per bucket. Worst case: $O(n^2)$ if all elements hash into the same bucket and insertion sort is used.
- **Space:** $O(n)$ auxiliary space to allocate $n$ buckets holding the $n$ elements in total.

## Edge Cases

- Empty list: returns empty list immediately.
- Single element list: returns a copy of the list.
- Duplicates: correctly placed into the same bucket and stably sorted.
- Floating-point boundary at $x = 0.0$: maps to bucket index 0 without issue.
- Floating-point values extremely close to 1.0: guarded by `min(int(x * n), n - 1)` against out-of-bounds indexing.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def _insertion_sort(bucket: list[float]) -> None:
    """Sorts a bucket in-place using insertion sort."""
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def bucket_sort(nums: list[float]) -> list[float]:
    """Sorts floats in [0, 1) in average O(n) time using Bucket Sort."""
    n = len(nums)
    if n <= 1:
        return list(nums)

    buckets: list[list[float]] = [[] for _ in range(n)]

    for x in nums:
        index = int(x * n)
        if index >= n:
            index = n - 1
        buckets[index].append(x)

    result: list[float] = []
    for bucket in buckets:
        _insertion_sort(bucket)
        result.extend(bucket)

    return result
```
