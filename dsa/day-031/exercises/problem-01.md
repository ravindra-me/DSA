# Problem 1: Optimized Bubble Pass Counter

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy | Bubble sort mechanics, early termination, and swap tracking | [Day 31: Bubble, Selection & Insertion Sort](../README.md) |

## Problem Statement

Implement Bubble Sort on a list of integers with the early-exit optimization (terminate as soon as a full pass completes without any swaps). Return a tuple `(sorted_arr, total_swaps, passes_completed)`, where:
- `sorted_arr` is the sorted list in non-decreasing order.
- `total_swaps` is the total number of element swaps performed.
- `passes_completed` is the number of passes through the list executed (a pass checks adjacent pairs from index `0` up to `n - 1 - p` where `p` is the pass index $0, 1, \dots$). If the array is already sorted, exactly 1 pass is completed and 0 swaps occur.

Note: Do not mutate the input list directly; return a new list.

## Input

A list of integers `arr`.

## Output

A tuple `(list[int], int, int)` containing `(sorted_arr, total_swaps, passes_completed)`.

## Constraints

- 0 <= len(arr) <= 1000
- -10^6 <= arr[i] <= 10^6

## Examples

**Example 1**

```text
Input:  arr = [3, 2, 1]
Output: ([1, 2, 3], 3, 2)
```

Pass 1: (3,2)->swap [2,3,1], (3,1)->swap [2,1,3]. Swaps = 2. Pass 2: (2,1)->swap [1,2,3]. Swaps = 3. Pass 3 (early check): no swaps, but array is resolved. Specifically, after 2 passes, elements are sorted; checking pass 3 triggers 0 swaps, completing 3 passes total if we check again, or after pass 2 if tested. Follow the standard loop: each pass outer loop runs up to n-1 times; break immediately if swapped is False.

**Example 2**

```text
Input:  arr = [1, 2, 3, 4]
Output: ([1, 2, 3, 4], 0, 1)
```

Pass 1 compares (1,2), (2,3), (3,4). No swaps occur. Loop terminates early. Exactly 1 pass was completed.

**Example 3**

```text
Input:  arr = []
Output: ([], 0, 0)
```

An empty array requires 0 passes and 0 swaps.

## Function Signature

```python
def bubble_sort_analysis(arr: list[int]) -> tuple[list[int], int, int]:
    """Sorts arr using optimized bubble sort and returns (sorted_list, total_swaps, passes)."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Simulate the standard bubble sort with an outer loop and inner loop, maintaining a boolean swapped flag and counters for swaps and completed outer passes.

</details>

## Your Turn

- Write your solution in [`practice/problem_01.py`](../practice/problem_01.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-01.md`](../solutions/problem-01.md), but try first!
