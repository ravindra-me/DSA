# Solution 5: Maximum Gap in Linear Time

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Pigeonhole Principle with Bucket Partitioning

## Approach

We can find the maximum gap in linear time using the Pigeonhole Principle combined with bucket partitioning. By dividing the range $[\min, \max]$ into $n - 1$ uniform buckets, the average gap between adjacent elements is at least $\lceil (\max - \min) / (n - 1) \rceil$. Therefore, the maximum gap cannot lie within any single bucket—it must span across consecutive non-empty buckets (from the maximum of one bucket to the minimum of the next non-empty bucket).

## Thought Process

A naive solution sorts the array in $O(n \log n)$ time using standard comparison sorting, then scans for the maximum difference between adjacent elements. To achieve $O(n)$ time, we need a non-comparison sorting or partitioning technique.

Notice that we do not actually need all elements to be fully sorted; we only need to know the maximum distance between two adjacent sorted elements. Let the minimum value be `min_val` and the maximum value be `max_val` across $n$ numbers. The total span `max_val - min_val` contains $n - 1$ intervals between the $n$ sorted numbers. By the Pigeonhole Principle, the average gap is $(\text{max\_val} - \text{min\_val}) / (n - 1)$. The maximum gap must therefore be at least this value.

If we choose a bucket size $b = \max(1, \lfloor(\text{max\_val} - \text{min\_val}) / (n - 1)\rfloor)$, any two elements inside the same bucket will have a difference strictly less than or equal to $b$. Hence, the maximum gap cannot occur between elements inside the same bucket (with appropriate bucket sizing where bucket span $\le b$). It can only occur between the maximum of a non-empty bucket and the minimum of the next non-empty bucket. Thus, we only need to record the minimum and maximum value inside each bucket, reducing both the time and extra space to $O(n)$.

## Algorithm

1. Handle the base case: if `len(nums) < 2`, return 0.
2. Find `min_val` and `max_val` of `nums`. If `min_val == max_val`, return 0.
3. Compute bucket size: `bucket_size = max(1, (max_val - min_val) // (n - 1))`. Compute bucket count: `bucket_count = (max_val - min_val) // bucket_size + 1`.
4. Initialize two arrays of size `bucket_count`: `bucket_min` filled with $\infty$ and `bucket_max` filled with $-\infty$.
5. Iterate through each number `x` in `nums`. Determine its bucket index: `idx = (x - min_val) // bucket_size`. Update `bucket_min[idx] = min(bucket_min[idx], x)` and `bucket_max[idx] = max(bucket_max[idx], x)`.
6. Iterate over the buckets tracking `prev_max` (initially `min_val`). For each non-empty bucket, update `max_gap = max(max_gap, bucket_min[i] - prev_max)` and then set `prev_max = bucket_max[i]`.
7. Return `max_gap`.

## Complexity Analysis

- **Time:** $O(n)$ because we make a constant number of passes over the input array of size $n$ and the bucket arrays of size at most $n + 1$.
- **Space:** $O(n)$ auxiliary space to store the minimum and maximum values for $O(n)$ buckets.

## Edge Cases

- Arrays with fewer than 2 elements: returned 0 immediately.
- Arrays where all elements are identical (max_val == min_val): returned 0 immediately, avoiding division by zero.
- Arrays where bucket_size would evaluate to 0 if not guarded: prevented using `max(1, ...)`.
- Inputs containing 0 and up to $10^9$: handled without overflow since Python integers have arbitrary precision and operations are well within standard ranges.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
import math

def maximum_gap(nums: list[int]) -> int:
    """Finds the maximum gap in sorted order in linear O(n) time."""
    n = len(nums)
    if n < 2:
        return 0

    min_val = min(nums)
    max_val = max(nums)
    if min_val == max_val:
        return 0

    bucket_size = max(1, (max_val - min_val) // (n - 1))
    bucket_count = (max_val - min_val) // bucket_size + 1

    bucket_min = [math.inf] * bucket_count
    bucket_max = [-math.inf] * bucket_count

    for num in nums:
        idx = (num - min_val) // bucket_size
        if num < bucket_min[idx]:
            bucket_min[idx] = num
        if num > bucket_max[idx]:
            bucket_max[idx] = num

    max_gap = 0
    prev_max = min_val

    for b_min, b_max in zip(bucket_min, bucket_max):
        if b_min == math.inf:
            continue
        max_gap = max(max_gap, int(b_min - prev_max))
        prev_max = b_max

    return max_gap
```
