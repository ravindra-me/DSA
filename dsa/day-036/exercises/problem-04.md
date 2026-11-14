# Problem 4: Sort K-Messed Array

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Bounded Heap Sorting Window | [Day 36: Heap Sort](../README.md) |

## Problem Statement

Given an array of integers `nums` where each element is at most `k` positions away from its target sorted position, sort the array in ascending order.

Your solution must run in $O(n \log k)$ time and use $O(k)$ auxiliary space. You may implement a min-heap or min-sift logic directly, or use Python's `heapq`.

## Input

- `nums: list[int]` - A nearly sorted list.
- `k: int` - Maximum distance of any element from its sorted index ($0 \le k < \text{len}(nums)$).

## Output

`list[int]` - The sorted list.

## Constraints

- 0 <= len(nums) <= 10^5
- 0 <= k < max(1, len(nums))
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [3, 2, 1, 5, 4, 7, 6, 5], k = 3
Output: [1, 2, 3, 4, 5, 5, 6, 7]
```

Every element is within 3 positions of where it belongs.

**Example 2**

```text
Input:  nums = [1, 2, 3], k = 0
Output: [1, 2, 3]
```

k = 0 means the array is already sorted.

## Function Signature

```python
def sort_k_messed_array(nums: list[int], k: int) -> list[int]:
    """Sort an array where each element is at most k places away from sorted position."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a min-heap of size at most k + 1. For each position from 0 to n - 1, extract the minimum to the output and insert the next available element into the heap.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
