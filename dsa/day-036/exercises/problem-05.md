# Problem 5: In-Place Partial Selection Sort via Heap

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Partial Heap Sort for Top-K Elements | [Day 36: Heap Sort](../README.md) |

## Problem Statement

You are given an array of integers `nums` and an integer `k`. Rearrange `nums` in-place such that the largest `k` elements of the array appear in sorted ascending order in the last `k` positions of the array (`nums[len(nums) - k :]`).

The remaining `len(nums) - k` elements in the first part of the array do not need to be sorted, but must contain the remaining smaller elements.

Your algorithm must modify `nums` in-place with strictly $O(1)$ auxiliary space and run in $O(n + k \log n)$ time. Do not use Python's built-in `sort()` or external data structures.

## Input

- `nums: list[int]` - The input array.
- `k: int` - Number of largest elements to extract and sort ($0 \le k \le \text{len}(nums)$).

## Output

None (modifies `nums` in-place).

## Constraints

- 0 <= len(nums) <= 10^5
- 0 <= k <= len(nums)
- -10^9 <= nums[i] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [9, 3, 7, 1, 8, 2, 5], k = 3
Output: [1, 2, 3, 5, 7, 8, 9] (Note: first 4 elements can be in any order such that last 3 are [7, 8, 9])
```

The 3 largest elements (7, 8, 9) are sorted at indices 4, 5, 6.

**Example 2**

```text
Input:  nums = [4, 1, 2], k = 0
Output: [4, 1, 2]
```

k = 0 requires 0 elements to be placed.

## Function Signature

```python
def partial_heap_sort(nums: list[int], k: int) -> None:
    """Place the k largest elements of nums in ascending order at nums[len(nums)-k:] in-place."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Build a max-heap across the entire array in O(n), then perform exactly k extraction iterations of swap-and-sift_down to place the k largest elements in sorted order at the end.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
