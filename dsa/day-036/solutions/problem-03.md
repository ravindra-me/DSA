# Solution 3: Classic In-Place Heap Sort

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Full Heap Sort Algorithm

## Approach

Heap sort sorts an array in-place by treating the array as a complete binary tree. First, we build a max-heap in $O(n)$ time using bottom-up sift-down operations. Then, we repeatedly swap the maximum element at root (index 0) with the last element of the active heap, decrement the active heap size, and sift down the new root to restore the max-heap property. Once the active heap shrinks to 1, the entire array is sorted in ascending order.

## Thought Process

A naive sorting approach might use an external priority queue or duplicate the array, taking $O(n)$ extra space. Alternatively, an $O(n^2)$ selection sort finds the maximum element in the unsorted prefix repeatedly and places it at the end.

Heap sort optimizes selection sort by organizing the unsorted prefix into a max-heap data structure stored entirely in-place within the array. Finding the maximum takes $O(1)$ time, and extracting it while restoring the heap property takes $O(\log n)$ time via `_sift_down`. Building the initial max-heap bottom-up takes $O(n)$ time rather than $O(n \log n)$ because elements lower in the tree require fewer swap steps.

Iterative `sift_down` ensures strictly $O(1)$ auxiliary space without recursive call stack overhead.

## Algorithm

1. Handle trivial inputs: if `len(nums) <= 1`, return immediately as the array is already sorted.
2. Define an iterative helper `_sift_down(nums, n, root)` that moves the element at `root` down the tree of size `n` until both children are smaller or equal to it.
3. Phase 1 (Heapify): Start from the last internal node index `(n // 2) - 1` down to index 0, calling `_sift_down(nums, n, i)` to build a max-heap in $O(n)$ time.
4. Phase 2 (Sort-down): Iterate `end` from `n - 1` down to 1. In each iteration, swap `nums[0]` with `nums[end]`, and call `_sift_down(nums, end, 0)` on the reduced heap of size `end`.
5. After all iterations, `nums` is sorted in ascending order in-place.

## Complexity Analysis

- **Time:** $O(n \log n)$ in the worst, average, and best cases. Building the heap takes $O(n)$ time, and each of the $n - 1$ extractions takes $O(\log n)$ time.
- **Space:** $O(1)$ auxiliary space because all swaps and index manipulations are performed directly within `nums` using an iterative sift-down routine.

## Edge Cases

- Empty list (`nums = []`): Handled immediately by the length check `n <= 1` without executing loops.
- Single element (`nums = [x]`): Handled immediately by the length check `n <= 1`.
- Already sorted or reverse-sorted lists: Max-heap property correctly handles both without infinite loops or invalid index accesses.
- Duplicate and all-identical values: Sift-down strictly uses strictly greater (`>`) comparisons, properly terminating when elements are equal.
- Extreme values: Standard 64-bit integer comparisons handle numbers up to $\pm 10^9$ without overflow or issues.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def _sift_down(nums: list[int], n: int, root: int) -> None:
    """Sift down root within the prefix of nums of length n to maintain max-heap."""
    largest = root
    while True:
        left = 2 * root + 1
        right = 2 * root + 2

        if left < n and nums[left] > nums[largest]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right

        if largest == root:
            break

        nums[root], nums[largest] = nums[largest], nums[root]
        root = largest


def heap_sort(nums: list[int]) -> None:
    """Sort nums in ascending order in-place using Heap Sort."""
    n = len(nums)
    if n <= 1:
        return

    # Phase 1: Build max-heap (bottom-up)
    for i in range((n // 2) - 1, -1, -1):
        _sift_down(nums, n, i)

    # Phase 2: Extract elements one by one
    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        _sift_down(nums, end, 0)
```
