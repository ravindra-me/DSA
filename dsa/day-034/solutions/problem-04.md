# Solution 4: K Closest Points to Origin

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Quickselect with Custom Distance Function

## Approach

We use the Quickselect algorithm based on squared Euclidean distance to find the $k$-th smallest distance partition in $O(N)$ average time complexity. By computing $x^2 + y^2$ directly, we avoid floating-point inaccuracies associated with square roots. Quickselect partially sorts the array in-place so that the first $k$ elements are the $k$ closest points to the origin.

## Thought Process

A naive approach calculates all Euclidean distances and fully sorts the points array, which takes $O(N \log N)$ time. Alternatively, a min-heap or max-heap can find the top $k$ points in $O(N \log k)$ time.

However, we only need to partition the array such that the $k$ smallest elements are on the left, regardless of their relative order. Quickselect achieves this in $O(N)$ average time. By choosing a random pivot during each step of Lomuto or Hoare partitioning, we guarantee linear expected performance and avoid $O(N^2)$ worst-case performance on already sorted inputs.

## Algorithm

1. Define a distance function $d(p) = p[0]^2 + p[1]^2$ to avoid square root calculations.
2. Define a recursive or iterative `quickselect(left, right, k)` function that operates in-place on the `points` array.
3. Pick a random pivot index between `left` and `right`, swap it with `right`.
4. Partition `points[left..right]` around the pivot distance.
5. If the pivot ends up at index `k - 1`, the first $k$ elements are the $k$ closest points, so we stop.
6. If the pivot index is greater than `k - 1`, recursively partition the left subarray `quickselect(left, pivot_index - 1, k)`.
7. Otherwise, recursively partition the right subarray `quickselect(pivot_index + 1, right, k)`.
8. Return `points[:k]`.

## Complexity Analysis

- **Time:** $O(N)$ average, $O(N^2)$ worst-case. With randomized pivot selection, the expected time complexity is linear.
- **Space:** $O(1)$ auxiliary space if done iteratively (or $O(\log N)$ average call stack space for recursive quickselect).

## Edge Cases

- $k == N$: Returns all points in the input.
- $k == 1$: Returns the single closest point.
- Duplicate distances or points: Handled correctly by standard partitioning operator comparison (`<=`).
- Negative coordinates: Squaring negative numbers naturally handles points in all four quadrants.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
import random
import sys

sys.setrecursionlimit(200000)

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    """Return the k closest points to the origin using Quickselect."""
    def dist_sq(p: list[int]) -> int:
        return p[0] * p[0] + p[1] * p[1]

    def partition(left: int, right: int) -> int:
        pivot_idx = random.randint(left, right)
        points[pivot_idx], points[right] = points[right], points[pivot_idx]
        pivot_dist = dist_sq(points[right])
        
        i = left
        for j in range(left, right):
            if dist_sq(points[j]) <= pivot_dist:
                points[i], points[j] = points[j], points[i]
                i += 1
        
        points[i], points[right] = points[right], points[i]
        return i

    left, right = 0, len(points) - 1
    target = k - 1
    while left < right:
        pivot_idx = partition(left, right)
        if pivot_idx == target:
            break
        elif pivot_idx < target:
            left = pivot_idx + 1
        else:
            right = pivot_idx - 1
            
    return points[:k]
```
