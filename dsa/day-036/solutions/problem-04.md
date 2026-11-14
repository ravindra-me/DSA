# Solution 4: Sort K-Messed Array

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Bounded Heap Sorting Window

## Approach

Maintain a sliding min-heap of size at most $k + 1$. Because every element is at most $k$ positions away from its sorted index, the smallest element of the entire array must reside within the first $k + 1$ elements. Repeatedly popping the minimum from this sliding window and inserting the next unseen element places each element into its correct sorted position in $O(\log k)$ time per step.

## Thought Process

A naive approach is to use standard sorting ($O(n \log n)$) or insertion sort, which runs in $O(n \cdot k)$ since elements only need to shift at most $k$ positions. When $k \ll n$, both can be improved.

Observe that for any index $i$ in the final sorted array, the element belonging at index $i$ could only have started in the window $[\max(0, i - k), \min(n - 1, i + k)]$. Specifically, the very first element (index $0$) must currently be within `nums[0 .. k]`. Thus, among the first $k + 1$ elements, the smallest is guaranteed to be the overall minimum element.

Once we extract this minimum and assign it to index $0$, the candidate pool for index $1$ is the remaining elements from the initial window plus index $k + 1$ (if within bounds). By maintaining a min-heap containing at most $k + 1$ elements, each extraction takes $O(\log k)$ time and each addition takes $O(\log k)$ time. This yields an overall time complexity of $O(n \log k)$ and $O(k)$ extra space.

## Algorithm

1. Handle the base case: if `len(nums) <= 1` or `k == 0`, return `nums` directly.
2. Insert the first $\min(k + 1, n)$ elements into a min-heap using `heapq.heapify`.
3. Initialize a write pointer `write_idx = 0`.
4. Iterate through the remaining elements `nums[i]` from index $k + 1$ to $n - 1$:
5. At each step, pop the minimum element from the heap with `heappop` and place it at `nums[write_idx]`.
6. Push `nums[i]` into the heap with `heappush` (or use `heapreplace` for efficiency) and increment `write_idx`.
7. After iterating through all remaining elements, pop the remaining elements from the heap one by one and write them to `nums[write_idx]` until the heap is empty.
8. Return the modified `nums`.

## Complexity Analysis

- **Time:** $O(n \log k)$: We insert and remove $n$ elements from a heap of size at most $k + 1$, each operation taking $O(\log k)$ time.
- **Space:** $O(k)$ auxiliary space: The min-heap holds at most $k + 1$ elements at any given time.

## Edge Cases

- Empty array (`nums = []`): immediately returned without modification.
- Single element (`len(nums) == 1`): immediately returned as already sorted.
- `k = 0`: every element is at most 0 positions away, meaning the array is already sorted; returned immediately.
- `k >= len(nums)`: handled safely by capping the initial heap size at `len(nums)`.
- Duplicate and negative values: correctly ordered by the min-heap comparison.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
import heapq


def sort_k_messed_array(nums: list[int], k: int) -> list[int]:
    """Sort an array where each element is at most k places away from sorted position."""
    n = len(nums)
    if n <= 1 or k == 0:
        return nums

    window_size = min(k + 1, n)
    heap = nums[:window_size]
    heapq.heapify(heap)

    write_idx = 0
    for read_idx in range(window_size, n):
        nums[write_idx] = heapq.heapreplace(heap, nums[read_idx])
        write_idx += 1

    while heap:
        nums[write_idx] = heapq.heappop(heap)
        write_idx += 1

    return nums
```
