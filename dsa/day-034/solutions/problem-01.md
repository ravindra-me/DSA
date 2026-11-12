# Solution 1: Lomuto Partition Scheme

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Lomuto Partitioning

## Approach

Swap the pivot element to the end of the array to place it in the standard Lomuto pivot position. Then maintain a boundary index `i` for elements less than or equal to the pivot, scan through the array with index `j`, and swap `nums[j]` with `nums[i]` whenever `nums[j] <= pivot`. Finally, swap the pivot at the end with `nums[i]` to place the pivot into its correct partitioned position.

## Thought Process

Lomuto partitioning processes an array in a single pass ($O(N)$ time) with $O(1)$ extra space. By swapping the specified `pivot_index` element with the last element (`nums[-1]`), we reduce the problem to standard Lomuto partitioning over the range `[0, len(nums) - 1]`. The array is logically divided into three sections: elements $\le$ pivot, elements $>$ pivot, and unexamined elements. Incrementing the boundary `i` and swapping on finding an element $\le$ pivot maintains these invariants.

## Algorithm

1. Identify the pivot value `pivot_val = nums[pivot_index]`.
2. Swap `nums[pivot_index]` with `nums[-1]` to position the pivot at the end.
3. Initialize index `i = 0`, which tracks the boundary where elements `<= pivot_val` will be placed.
4. Iterate `j` from `0` to `len(nums) - 2` (excluding the pivot at the end).
5. If `nums[j] <= pivot_val`, swap `nums[i]` and `nums[j]`, then increment `i`.
6. After the loop, swap `nums[i]` with `nums[-1]` to move the pivot value to its final position at index `i`.
7. Return `i`.

## Complexity Analysis

- **Time:** O(N) where N is the length of `nums`, as it performs a single linear pass over the array.
- **Space:** O(1) auxiliary space because partitioning is done in-place.

## Edge Cases

- Single element array (`len(nums) == 1`): loop range is empty, pivot stays at index 0, returns 0.
- Pivot is already at the end (`pivot_index == len(nums) - 1`): swapping to end is a self-swap, partitioning works normally.
- Array with duplicate elements: elements equal to pivot are grouped on the left side (<= pivot).
- Negative numbers and zero: handled naturally by standard standard integer comparisons.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def partition_lomuto(nums: list[int], pivot_index: int) -> int:
    """Partition nums in-place using Lomuto scheme with the given pivot index.

    Returns the final index of the pivot element after partitioning.
    """
    n = len(nums)
    pivot_val = nums[pivot_index]
    
    # Move pivot to the end
    nums[pivot_index], nums[-1] = nums[-1], nums[pivot_index]
    
    i = 0
    for j in range(n - 1):
        if nums[j] <= pivot_val:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            
    # Move pivot to its final place
    nums[i], nums[-1] = nums[-1], nums[i]
    return i
```
