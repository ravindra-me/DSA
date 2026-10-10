# Solution 4: Logarithmic Peak Finder

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Logarithmic time complexity O(log n) vs linear scan O(n)

## Approach

We can find a peak in $O(\log n)$ time using binary search. By comparing `nums[mid]` to `nums[mid + 1]`, we can determine whether the sequence is currently ascending or descending. If `nums[mid] < nums[mid + 1]`, an uphill slope exists to the right, guaranteeing at least one peak lies in `[mid + 1, right]`. Otherwise, a downhill slope exists (or `mid` is itself a peak), guaranteeing a peak lies in `[left, mid]`.

## Thought Process

A brute-force scan would examine each element linearly in $O(n)$ time by checking whether `nums[i] > nums[i - 1]` and `nums[i] > nums[i + 1]`. However, the problem explicitly demands $O(\log n)$ time complexity.

To achieve logarithmic time, we must eliminate half of the search space at each step without inspecting all elements. Even though the array is not globally sorted, the problem guarantees that adjacent elements are never equal (`nums[i] != nums[i + 1]`), and the boundary conditions act as $-\infty$.

Consider the midpoint `mid` and its neighbor `mid + 1`:
1. If `nums[mid] < nums[mid + 1]`, the values are increasing as we move right. Since the boundary at index $n$ is $-\infty$, the sequence cannot increase indefinitely. It must eventually peak and decrease (or terminate at index $n - 1$ as a peak). Thus, there is guaranteed to be at least one peak in the right half `[mid + 1, right]`.
2. If `nums[mid] > nums[mid + 1]`, the values are decreasing. By the symmetric argument with the boundary at index $-1$ being $-\infty$, there must be at least one peak in the left half `[left, mid]` (note that `mid` itself could be the peak).

By halving the search interval in every iteration, we guarantee convergence to a peak index in $O(\log n)$ steps.

## Algorithm

1. Initialize two pointers: `left = 0` and `right = len(nums) - 1`.
2. While `left < right`, compute the middle index `mid = left + (right - left) // 2`.
3. Compare `nums[mid]` with `nums[mid + 1]`.
4. If `nums[mid] < nums[mid + 1]`, move the left boundary to `mid + 1` because a peak must exist to the right.
5. Else (`nums[mid] > nums[mid + 1]`), move the right boundary to `mid` because `mid` itself or an element to the left must be a peak.
6. When `left == right`, the search space has converged to a single index. Return `left`.

## Complexity Analysis

- **Time:** $O(\log n)$ because the search space of size $n$ is halved on every iteration.
- **Space:** $O(1)$ auxiliary space as we only maintain two integer pointer variables.

## Edge Cases

- Single element array (len == 1): The loop `left < right` terminates immediately without entering, correctly returning index 0.
- Strictly monotonically increasing array: Each step moves `left` rightwards, eventually converging on the last index `n - 1`.
- Strictly monotonically decreasing array: Each step moves `right` leftwards, converging on index 0.
- Negative values and large 32-bit integers: Handled naturally since comparisons are strictly relative between adjacent integers.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def find_peak_element(nums: list[int]) -> int:
    """Find the index of any peak element in strictly O(log n) time."""
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
```
