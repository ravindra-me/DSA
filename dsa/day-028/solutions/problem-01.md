# Solution 1: First and Last Position of Target

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** first-last-occurrence

## Approach

We run two modified binary searches: one to find the left boundary (first occurrence) of the target and another to find the right boundary (last occurrence). By continuing the binary search even after finding an instance of `target`, we can shrink the search range to pinpoint the exact boundaries in $O(\log N)$ time.

## Thought Process

A naive approach would perform a standard binary search to find any occurrence of `target` and then scan left and right linearly to find the boundaries. However, in the worst case (e.g., an array filled entirely with `target`), the linear scan takes $O(N)$ time. To meet the $O(\log N)$ requirement, we must use binary search to locate both boundaries. Finding the lower bound involves biasing the binary search to search the left sub-array when `nums[mid] == target`. Finding the upper bound biases the search to the right sub-array when `nums[mid] == target`.

## Algorithm

1. Define a helper function `find_bound(is_first)` that performs a binary search.
2. Initialize `low = 0`, `high = len(nums) - 1`, and `bound = -1`.
3. While `low <= high`, calculate `mid = (low + high) // 2`.
4. If `nums[mid] == target`, record `bound = mid`. If `is_first` is True, search the left half by setting `high = mid - 1`; otherwise, search the right half by setting `low = mid + 1`.
5. If `nums[mid] < target`, move `low = mid + 1`.
6. If `nums[mid] > target`, move `high = mid - 1`.
7. Return `[find_bound(True), find_bound(False)]` after executing both searches.

## Complexity Analysis

- **Time:** $O(\log N)$ because two binary searches are executed, each dividing the search space in half at every step.
- **Space:** $O(1)$ auxiliary space as the binary searches run iteratively using a fixed number of variables.

## Edge Cases

- Empty list (`nums = []`): Both binary search calls immediately return `-1`, outputting `[-1, -1]`.
- Target not in list: `bound` remains `-1`, returning `[-1, -1]`.
- Single element list: Correctly returns `[0, 0]` if matched or `[-1, -1]` if not matched.
- All elements equal target: First search sets boundary to `0` and second sets boundary to `len(nums) - 1`.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def search_range(nums: list[int], target: int) -> list[int]:
    """Return the first and last 0-based indices of target in nums."""
    def find_bound(is_first: bool) -> int:
        low, high = 0, len(nums) - 1
        bound = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return bound

    return [find_bound(True), find_bound(False)]
```
