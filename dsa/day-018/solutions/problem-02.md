# Solution 2: Intersection of Two Arrays

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Set deduplication and set intersection

## Approach

Convert `nums1` into a hash set to achieve $O(1)$ average-time lookups and deduplication. Iterate through `nums2`, collecting elements present in the set into a result set, and finally return the sorted elements.

## Thought Process

A brute-force approach compares every element in `nums1` with every element in `nums2`, taking $O(n \times m)$ time, followed by deduplication and sorting. 

To optimize, we can use a hash set. Inserting all elements of `nums1` into a hash set `set1` takes $O(n)$ time. Then, looking up each element of `nums2` in `set1` takes $O(1)$ on average. By adding matched elements to another hash set (or using Python's built-in set intersection `&`), we ensure uniqueness in $O(n + m)$ time. Finally, sorting the unique common elements takes $O(k \log k)$ where $k \le \min(n, m, 1001)$ based on the problem constraints.

## Algorithm

1. Convert `nums1` into a hash set `set1` to deduplicate its elements and allow $O(1)$ lookups.
2. Initialize an empty result set `common`.
3. Iterate through each number `x` in `nums2`; if `x` is in `set1`, add `x` to `common`.
4. Sort the elements of `common` in ascending order and return them as a list.

## Complexity Analysis

- **Time:** $O(n + m + k \log k)$ where $n = \text{len}(nums1)$, $m = \text{len}(nums2)$, and $k$ is the number of unique intersecting elements. Given $0 \le \text{nums}[i] \le 1000$, $k \le 1001$, making the sort negligible.
- **Space:** $O(n + k)$ to store the hash set of elements from `nums1` and the intersecting elements.

## Edge Cases

- No overlapping elements: returns an empty list `[]`.
- Single-element arrays: handled uniformly, returns `[x]` if equal, `[]` if distinct.
- All elements identical in both lists: deduplicates to a single element `[x]`.
- Values at the boundaries of the constraints ($0$ and $1000$): correctly processed with standard integer hashing.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """Return sorted list of unique common elements between nums1 and nums2."""
    set1 = set(nums1)
    result = set()
    for num in nums2:
        if num in set1:
            result.add(num)
    return sorted(result)
```
