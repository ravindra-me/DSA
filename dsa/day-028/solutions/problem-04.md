# Solution 4: Find Peak Element

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** peak-finding

## Approach

We use binary search by comparing the middle element `nums[mid]` with its right neighbor `nums[mid + 1]`. If `nums[mid] < nums[mid + 1]`, there must be at least one peak in the right half because the sequence increases towards `mid + 1` and eventually drops off at the array boundary (or earlier). If `nums[mid] > nums[mid + 1]`, a peak exists in the left half (including `mid`). This guarantees convergence to a peak in $O(\log N)$ time.

## Thought Process

A naive scan checking `nums[i - 1] < nums[i] > nums[i + 1]` takes $O(N)$ time. To reach $O(\log N)$, we look for binary search invariants.

Since `nums[-1] = nums[n] = -∞` and adjacent elements are distinct (`nums[i] != nums[i + 1]`), any subarray with an upward slope must eventually peak before hitting an implicit $-\infty$ boundary. Comparing `nums[mid]` with `nums[mid + 1]` tells us the local slope:
- Upward slope (`nums[mid] < nums[mid + 1]`): A peak is guaranteed to exist strictly to the right (`left = mid + 1`).
- Downward slope (`nums[mid] > nums[mid + 1]`): A peak is guaranteed to exist at `mid` or to the left (`right = mid`).

Thus, we can halve the search space at each step without missing a peak.

## Algorithm

1. Initialize two pointers `left = 0` and `right = len(nums) - 1`.
2. Loop while `left < right`:
3. Compute `mid = left + (right - left) // 2`.
4. If `nums[mid] < nums[mid + 1]`, set `left = mid + 1` (a peak must lie to the right).
5. Otherwise (`nums[mid] > nums[mid + 1]`), set `right = mid` (a peak must lie at or to the left of `mid`).
6. Return `left` (or `right`), which points to a valid peak element index.

## Complexity Analysis

- **Time:** $O(\log N)$ because the search range is halved in each step.
- **Space:** $O(1)$ auxiliary space as we only store a few integer pointers.

## Edge Cases

- Single element array: `left` equals `right` (0) initially, loop terminates immediately, returning 0.
- Strictly increasing array: standard binary search moves `left` all the way to `len(nums) - 1`, which is the peak.
- Strictly decreasing array: binary search moves `right` all the way to 0, which is the peak.
- Negative numbers and wide range bounds: comparison functions correctly handle negative integers without overflow issues.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def find_peak_element(nums: list[int]) -> int:
    """Return the 0-based index of any peak element in nums."""
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
```
