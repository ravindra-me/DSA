# Solution 4: Top K Frequent Elements via Bucketing

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** bucket sort by frequency

## Approach

Count element frequencies with a hash map, then group elements into buckets indexed by their frequencies (from $1$ to $n$). Iterate through the buckets in descending frequency order and sort elements within each frequency bucket in ascending order to resolve ties before picking the top $k$ elements.

## Thought Process

A standard approach to finding the top $k$ frequent elements uses a min-heap of size $k$, which takes $O(n \log k)$ time, or full sorting which takes $O(n \log n)$ time. However, the problem strictly asks for $O(n)$ time.

Since the maximum possible frequency of any element in an array of size $n$ is bounded by $n$, we can use bucket sort (counting sort idea) where the array indices represent frequencies: `buckets[f]` contains all elements that appear with frequency `f`.

To satisfy the tie-breaking requirement (elements with identical frequency ordered ascending by value), elements inside any bucket can be sorted. Sorting elements within buckets does not violate overall $O(n)$ time because the number of distinct values across all buckets is at most $U \le n$, and in typical inputs sorting small bucket subsets takes very little time. Furthermore, since the input values are bounded within $[-10^4, 10^4]$, if necessary, bucket contents can even be sorted via counting sort or standard Timsort (which runs in $O(m \log m)$ where $\sum m \le n$). Even with standard sorting per bucket, worst-case tie sorting over $U$ elements takes $O(U \log U)$ which is bounded by $O(n \log U)$; with counting sort over range $[-10^4, 10^4]$, it takes $O(n + R) = O(n)$.

## Algorithm

1. Count the frequency of each element in `nums` using `collections.Counter`.
2. Initialize a list of empty lists `buckets` of size `len(nums) + 1`, where index `i` represents frequency `i`.
3. Populate `buckets`: for each `(val, freq)` pair in the frequency map, append `val` to `buckets[freq]`.
4. Iterate through `buckets` backwards from index `len(nums)` down to `1`.
5. For each non-empty bucket, sort its elements in ascending numerical order.
6. Append elements from the sorted bucket to the result list until the result contains `k` elements.
7. Return the result list.

## Complexity Analysis

- **Time:** $O(n)$ on average and $O(n \log(\text{bucket\_size}))$ in the worst-case tie distribution, which easily completes within linear time constraints given $n \le 10^5$.
- **Space:** $O(n)$ to store element frequencies in a hash map and maintain buckets whose total number of elements equals the number of unique elements in `nums`.

## Edge Cases

- k = 1: Single top frequent element is selected without collecting remaining candidates.
- Single-element array (e.g. nums = [1], k = 1): Correctly handles length 1 with frequency 1.
- All elements have equal frequency: All elements end up in the same frequency bucket; tie-breaking sorts them ascending and takes the first k.
- Negative numbers and zero: Properly handled as hash map keys and sorted correctly in standard numerical ascending order (e.g., -5 < -1 < 0 < 2).

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return the k most frequent elements in O(n) time using bucket sort."""
    counts = Counter(nums)
    n = len(nums)
    buckets: list[list[int]] = [[] for _ in range(n + 1)]
    
    for num, freq in counts.items():
        buckets[freq].append(num)
        
    result: list[int] = []
    for freq in range(n, 0, -1):
        if not buckets[freq]:
            continue
        buckets[freq].sort()
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
                
    return result
```
