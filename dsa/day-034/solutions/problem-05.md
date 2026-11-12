# Solution 5: Wiggle Sort II

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** 3-Way Partitioning with Index Mapping

## Approach

To achieve $O(N)$ time and $O(1)$ extra space, we first find the median using Quickselect in average $O(N)$ time (or Python's standard partition equivalent logic). Then, we perform a 3-way Dutch National Flag partitioning relative to the median, but mapped through a virtual index transformation `(1 + 2 * i) % (n | 1)` to interleave elements smaller than the median at even indices (from right to left) and elements larger than the median at odd indices.

## Thought Process

A naive approach sorts the array in $O(N \log N)$ time, splits it into two halves, and interleaves them (smaller half at even indices, larger half at odd indices, both reversed to prevent identical median values from clustering together at adjacent positions). To reach $O(N)$ time and $O(1)$ extra space, we replace sorting with Quickselect to find the median element in $O(N)$ time. Then, instead of copying to temporary arrays, we use virtual index mapping. The virtual index mapping maps index $i$ to `(1 + 2 * i) % (n | 1)`. This reorders the linear scanning indices such that `0, 1, 2, ...` map to odd indices `1, 3, 5, ...` followed by even indices `0, 2, 4, ...`. Running 3-way partitioning with respect to the median over these mapped indices rearranges elements > median into odd indices and elements < median into even indices in-place.

## Algorithm

1. Find the median of `nums` using Quickselect (nth_element logic) in $O(N)$ average time.
2. Define virtual index mapping function `mapped_idx(i)` as `(1 + 2 * i) % (n | 1)`.
3. Initialize three pointers for 3-way partitioning: `left = 0`, `i = 0`, `right = n - 1`.
4. Loop while `i <= right`: get actual indices `actual_i = mapped_idx(i)`, `actual_left = mapped_idx(left)`, `actual_right = mapped_idx(right)`.
5. If `nums[actual_i] > median`: swap `nums[actual_i]` with `nums[actual_left]`, increment `left` and `i`.
6. Else if `nums[actual_i] < median`: swap `nums[actual_i]` with `nums[actual_right]`, decrement `right`.
7. Else (`nums[actual_i] == median`): increment `i`.

## Complexity Analysis

- **Time:** $O(N)$ average time using Quickselect for median finding, followed by a single $O(N)$ pass for 3-way partitioning.
- **Space:** $O(1)$ auxiliary space as the array is modified in-place using index mapping.

## Edge Cases

- Arrays of length 1 or 2: Handled trivially without swapping.
- Array with many duplicate values (e.g., [2, 2, 3, 2]): The virtual index mapping ensures that equal median values are placed at opposite ends (far end of odd indices and start of even indices), maintaining the strict inequality constraints.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
import random

def wiggle_sort(nums: list[int]) -> None:
    """
    Reorders the array in-place such that nums[0] < nums[1] > nums[2] < nums[3]...
    Achieves O(N) average time complexity and O(1) extra space.
    """
    n = len(nums)
    if n <= 1:
        return

    def quickselect(left: int, right: int, k: int) -> int:
        while left <= right:
            pivot_idx = random.randint(left, right)
            pivot_val = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            
            store_idx = left
            for i in range(left, right):
                if nums[i] < pivot_val:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1
            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            
            if store_idx == k:
                return nums[store_idx]
            elif store_idx < k:
                left = store_idx + 1
            else:
                right = store_idx - 1
        return nums[k]

    median = quickselect(0, n - 1, n // 2)

    # Virtual index mapping
    # Maps 0, 1, 2, ... to 1, 3, 5, ... 0, 2, 4, ...
    def map_index(i: int) -> int:
        return (1 + 2 * i) % (n | 1)

    # 3-way partitioning using mapped indices
    left, i, right = 0, 0, n - 1
    while i <= right:
        mapped_i = map_index(i)
        if nums[mapped_i] > median:
            mapped_left = map_index(left)
            nums[mapped_i], nums[mapped_left] = nums[mapped_left], nums[mapped_i]
            left += 1
            i += 1
        elif nums[mapped_i] < median:
            mapped_right = map_index(right)
            nums[mapped_i], nums[mapped_right] = nums[mapped_right], nums[mapped_i]
            right -= 1
        else:
            i += 1
```
