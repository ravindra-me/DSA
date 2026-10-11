# Solution 1: Remove Element In-Place

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** in-place updates and overwrite pointers

## Approach

Maintain a write pointer initialized to 0 and iterate through the array with a read pointer. Whenever an element does not equal `val`, copy it to the write pointer's index and increment the write pointer.

## Thought Process

A naive approach might delete matching elements one-by-one using list deletion (e.g., `nums.remove(val)` or `del nums[i]`), but each deletion shifts subsequent elements in $O(n)$ time, leading to an overall $O(n^2)$ complexity which would be too slow for $n = 10^5$.

Another approach is creating a new list with filtered elements and copying them back, requiring $O(n)$ extra space. However, the problem specifies modifying `nums` in-place with $O(1)$ auxiliary space.

To achieve $O(n)$ time and $O(1)$ space, we use the two-pointer 'overwrite' technique: one pointer iterates over every item (read pointer) and another marks the next available position to place a valid item (write pointer). Only non-matching elements are written, naturally overwriting or ignoring instances of `val`.

## Algorithm

1. Initialize `write_index = 0`.
2. Loop through each index `read_index` from `0` to `len(nums) - 1`.
3. If `nums[read_index] != val`, assign `nums[write_index] = nums[read_index]` and increment `write_index` by 1.
4. If `nums[read_index] == val`, skip it without advancing `write_index`.
5. Return `write_index`, which represents the count $k$ of elements not equal to `val`.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the length of `nums`. Each element is visited exactly once.
- **Space:** $O(1)$ auxiliary space because elements are modified directly within the input array without allocating extra collections.

## Edge Cases

- Empty array: the loop does not run, and `0` is immediately returned.
- All elements equal `val`: `write_index` is never incremented, returning `0` with no invalid items in the prefix.
- No elements equal `val`: `write_index` advances on every step, returning `len(nums)` with all original elements retained.
- Single element array: correctly returns `0` if it matches `val`, or `1` if it does not.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def remove_element(nums: list[int], val: int) -> int:
    """Remove all occurrences of val in-place and return the count of remaining elements."""
    write_index = 0
    for read_index in range(len(nums)):
        if nums[read_index] != val:
            nums[write_index] = nums[read_index]
            write_index += 1
    return write_index
```
