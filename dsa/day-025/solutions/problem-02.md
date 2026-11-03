# Solution 2: Sentinel Target Search

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Sentinel search technique to eliminate bound checks

## Approach

Sentinel linear search appends the `target` to the end of the array to act as a sentinel. This guarantees that the search loop will always find `target` eventually, allowing us to remove the array bound check `i < len(nums)` inside the inner loop. Afterwards, we restore the original array and check if the matched index was before the sentinel position.

## Thought Process

Standard linear search requires two checks per iteration: checking if the loop index is within bounds (`i < n`) and checking if the current element matches the target (`nums[i] == target`). By appending `target` to the end of `nums`, we guarantee that `nums[i] == target` will eventually evaluate to `True`. Thus, the index check inside the loop condition can be safely eliminated, reducing the overhead per iteration. Once the loop terminates, if the index `i` reached the appended sentinel position, the target was not in the original array. Finally, we must pop the sentinel element to restore `nums` to its original state as required.

## Algorithm

1. Handle the empty list edge case immediately by returning `False`.
2. Append `target` to the end of `nums` as a sentinel.
3. Initialize index `i = 0`.
4. Loop while `nums[i] != target`, incrementing `i` by 1 each time (no bounds checking needed).
5. Pop the last element from `nums` to restore its original state.
6. Return `True` if `i < len(nums)` (meaning `target` was found before the sentinel), otherwise `False`.

## Complexity Analysis

- **Time:** O(N) time complexity where N is the length of `nums`. In the worst case, we inspect each element once.
- **Space:** O(1) auxiliary space complexity. The sentinel is appended and removed in-place, modifying `nums` temporarily.

## Edge Cases

- Empty list (`nums = []`): Handled by checking if `nums` is empty before appending the sentinel, returning `False` immediately.
- Target is the last element: The loop stops at index `len(nums) - 1`, restoring `nums` correctly and returning `True`.
- Target is absent: The loop stops at the sentinel index `len(nums)`, restoring `nums` correctly and returning `False`.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def sentinel_search(nums: list[int], target: int) -> bool:
    """Perform linear search using the sentinel technique to eliminate bound checks."""
    if not nums:
        return False
    
    last_idx = len(nums)
    nums.append(target)
    
    i = 0
    while nums[i] != target:
        i += 1
    
    nums.pop()
    return i < last_idx
```
