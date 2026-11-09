# Problem 3: Sort Nearly-Sorted Array (k-Sorted)

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium | Insertion sort efficiency on inputs with bounded inversion distance | [Day 31: Bubble, Selection & Insertion Sort](../README.md) |

## Problem Statement

An array is said to be **$k$-sorted** if each element is at most $k$ positions away from its target position in the fully sorted array. For example, a $1$-sorted array has each element within distance 1 of its sorted location.

Insertion sort is known to run in $O(n \cdot k)$ time on $k$-sorted arrays. Implement an in-place insertion sort function `sort_k_sorted(arr: list[int], k: int) -> list[int]` that sorts a $k$-sorted array by shifting elements at most $k$ positions. Your solution must run in $O(n \cdot k)$ time and $O(1)$ auxiliary memory.

Return the sorted list. (You may mutate `arr` in place and return it).

## Input

A list of integers `arr` and an integer `k`.

## Output

The sorted list of integers in non-decreasing order.

## Constraints

- 0 <= len(arr) <= 10^5
- 0 <= k <= 100
- k < len(arr) if len(arr) > 0 else k == 0
- -10^9 <= arr[i] <= 10^9

## Examples

**Example 1**

```text
Input:  arr = [3, 2, 1, 5, 4, 7, 6], k = 2
Output: [1, 2, 3, 4, 5, 6, 7]
```

Every element is at most 2 steps away from its final index. Insertion sort places each item with at most k shifts.

**Example 2**

```text
Input:  arr = [10], k = 0
Output: [10]
```

Single element array is already sorted.

## Function Signature

```python
def sort_k_sorted(arr: list[int], k: int) -> list[int]:
    """Sorts a k-sorted array in-place in O(n * k) time using insertion sort."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Standard insertion sort algorithm: for each index i, slide arr[i] leftwards stopping as soon as an element <= key is found. Because the array is k-sorted, the inner while loop executes at most k times, yielding O(n * k) total time.

</details>

## Your Turn

- Write your solution in [`practice/problem_03.py`](../practice/problem_03.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-03.md`](../solutions/problem-03.md), but try first!
