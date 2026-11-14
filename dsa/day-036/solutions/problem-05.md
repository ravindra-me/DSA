# Solution 5: In-Place Partial Selection Sort via Heap

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Partial Heap Sort for Top-K Elements

## Approach

Build a max-heap in-place across the entire array in $O(n)$ time using Floyd's bottom-up heap construction (`sift_down`). Then, perform $k$ iterations of heap extraction: swap the root (`nums[0]`) with the current end of the active heap (`nums[i]`), and sift down the new root within the reduced heap of size $i$. After $k$ extractions, the largest $k$ elements are placed in their final sorted positions at `nums[n - k:]`.

## Thought Process

A full heap sort takes $O(n \log n)$ time by building a max-heap and extracting all $n$ elements. Each extraction places the largest remaining element at the end of the unsorted prefix.

Since we only need the top $k$ elements in sorted order at `nums[n - k:]`, we do not need to extract all $n$ elements. After building the max-heap in $O(n)$ time, running just $k$ extraction steps takes $k \times O(\log n) = O(k \log n)$ time.

Each extraction step places the current maximum element at `nums[n - 1]`, then `nums[n - 2]`, down to `nums[n - k]`. Because we extract the largest first and place it at the furthest available index, the resulting suffix `nums[n - k:]` will naturally be sorted in non-decreasing (ascending) order. The remaining $n - k$ elements stay in `nums[:n - k]`, all smaller than or equal to `nums[n - k]`, satisfying all problem constraints in strictly $O(1)$ auxiliary space.

## Algorithm

1. Check if $k \le 0$ or $n \le 1$; if so, return immediately as no work is needed.
2. Define an in-place `sift_down(arr, root, end)` helper that pushes a value down the max-heap bounded by `end`.
3. Heapify the entire array `nums` into a max-heap in $O(n)$ time by calling `sift_down` backwards from index `(n - 2) // 2` down to `0`.
4. Loop $k$ times for extraction index $i$ going from $n - 1$ down to $n - k$:
5. Swap `nums[0]` with `nums[i]` (placing the maximum remaining element at position $i$).
6. Call `sift_down(nums, 0, i)` to restore the max-heap property for the remaining heap of size $i$.

## Complexity Analysis

- **Time:** $O(n + k \log n)$. Floyd's heapify algorithm takes $O(n)$ time. Each of the $k$ extractions requires swapping and a sift-down step taking $O(\log n)$ time.
- **Space:** $O(1)$ auxiliary space. All operations (heapify, swapping, sift-down) are performed iteratively in-place on `nums`.

## Edge Cases

- Empty array (`nums = []`): handled immediately since `k` must be 0 and `len(nums) <= 1` returns.
- $k = 0$: no extraction steps are performed, array remains valid.
- $k = n$: performs full heap sort, leaving the entire array fully sorted.
- Duplicate elements: sift-down preserves weak ordering (`>=`), correctly handling duplicates without infinite loops or errors.
- Negative numbers and zeros: comparisons use standard integer `<=` and `>=` which handle negative values naturally.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def partial_heap_sort(nums: list[int], k: int) -> None:
    """Place the k largest elements of nums in ascending order at nums[len(nums)-k:] in-place."""
    n = len(nums)
    if k <= 0 or n <= 1:
        return

    # Ensure k does not exceed array length
    k = min(k, n)

    def _sift_down(arr: list[int], root: int, end: int) -> None:
        while True:
            left_child = 2 * root + 1
            right_child = left_child + 1
            largest = root

            if left_child < end and arr[left_child] > arr[largest]:
                largest = left_child
            if right_child < end and arr[right_child] > arr[largest]:
                largest = right_child

            if largest == root:
                break

            arr[root], arr[largest] = arr[largest], arr[root]
            root = largest

    # 1. Build max-heap in-place: O(n)
    for i in range((n - 2) // 2, -1, -1):
        _sift_down(nums, i, n)

    # 2. Extract k largest elements: O(k log n)
    for i in range(n - 1, n - 1 - k, -1):
        nums[0], nums[i] = nums[i], nums[0]
        _sift_down(nums, 0, i)
```
