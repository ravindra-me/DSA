# Solution 2: Strict In-Place Zero Partition

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Medium | **Concept:** In-place array partitioning with strict O(1) auxiliary space

## Approach

Use a two-pointer technique (read and write pointers). Iterate through the array with a read pointer `read_idx`; whenever a non-zero element is encountered, write it to `nums[write_idx]` and increment `write_idx`. Finally, fill the remaining elements from `write_idx` to the end of the array with zeros.

## Thought Process

A naive approach might allocate a new list, collect all non-zero elements, pad with zeros, and copy back to `nums`. While this runs in $O(n)$ time, it requires $O(n)$ auxiliary space, violating the strict $O(1)$ space constraint.

Another approach is removing zeros using `nums.pop(i)` and `nums.append(0)` in-place, but each removal shifts subsequent elements, yielding $O(n^2)$ time complexity, which would time out for $n = 10^5$.

To achieve both $O(n)$ time and $O(1)$ space, notice that `write_idx <= read_idx` is always true. As we scan with `read_idx`, we never overwrite an unread non-zero value. Thus, we can safely overwrite the prefix with non-zeros in their original relative order. Once all non-zeros are placed, the remaining slots from `write_idx` to `len(nums) - 1` are set to `0`. `write_idx` naturally represents the count of non-zero elements.

## Algorithm

1. Initialize `write_idx = 0` to track the destination index for the next non-zero element.
2. Loop `read_idx` through `range(len(nums))`.
3. If `nums[read_idx] != 0`, assign `nums[write_idx] = nums[read_idx]` and increment `write_idx` by 1.
4. After scanning the entire array, loop an index `i` from `write_idx` to `len(nums) - 1` and set `nums[i] = 0`.
5. Return `write_idx`, which equals the number of non-zero elements.

## Complexity Analysis

- **Time:** $O(n)$ because the array is traversed once to move non-zero elements and at most once more to fill trailing zeros, making total operations linear in the length of `nums`.
- **Space:** $O(1)$ auxiliary space because elements are modified directly within `nums` using only two index pointer variables.

## Edge Cases

- Single element array with zero: `nums = [0]` becomes `[0]`, returns `0`.
- Single element array with non-zero: `nums = [5]` becomes `[5]`, returns `1`.
- All zeros: no writes occur in the first pass; the second pass sets all elements to zero, returns `0`.
- No zeros: `write_idx` advances on every element, no trailing zeros are written, returns `len(nums)`.
- Alternating zeros and non-zeros or negative numbers: negative numbers are handled uniformly as non-zero integers.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def stable_zero_partition(nums: list[int]) -> int:
    """Partition zeros to the back in-place preserving relative order. Return non-zero count."""
    write_idx = 0
    n = len(nums)
    
    for read_idx in range(n):
        if nums[read_idx] != 0:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
            
    for i in range(write_idx, n):
        nums[i] = 0
        
    return write_idx
```
