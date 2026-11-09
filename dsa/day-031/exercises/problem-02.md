# Problem 2: Minimal Write Selection Sort

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Selection sort write minimization and tracking index updates | [Day 31: Bubble, Selection & Insertion Sort](../README.md) |

## Problem Statement

Selection sort is notable because it writes to each position at most once. However, unnecessary swaps (swapping an element with itself when it is already in the minimum position) waste write endurance.

Implement Selection Sort to sort `arr` in non-decreasing order while returning the list of swap pairs performed. Specifically:
- Scan from index `i = 0` to `n - 2`. Find the smallest element in `arr[i ... n-1]`. If there are duplicate minimum elements, select the one with the smallest index (maintaining leftmost preference).
- If the minimum element index `min_idx != i`, perform a swap and record the pair `(i, min_idx)`.
- If `min_idx == i`, do NOT perform a swap and do not record a pair.
- Return a tuple `(sorted_arr, swaps)` where `swaps` is a list of tuples `(i, j)` recording every actual swap performed in chronological order.

## Input

A list of integers `arr`.

## Output

A tuple `(list[int], list[tuple[int, int]])` containing the sorted list and the list of swap index pairs.

## Constraints

- 0 <= len(arr) <= 1000
- -10^6 <= arr[i] <= 10^6

## Examples

**Example 1**

```text
Input:  arr = [4, 3, 2, 1]
Output: ([1, 2, 3, 4], [(0, 3), (1, 2)])
```

i=0: min is 1 at index 3 -> swap (0, 3), array becomes [1, 3, 2, 4]. i=1: min is 2 at index 2 -> swap (1, 2), array becomes [1, 2, 3, 4]. i=2: min is 3 at index 2 -> min_idx == i, no swap. Result: 2 swaps.

**Example 2**

```text
Input:  arr = [1, 2, 3]
Output: ([1, 2, 3], [])
```

Array is already sorted; min_idx == i at every step, so 0 swaps are performed.

## Function Signature

```python
def selection_sort_tracked(arr: list[int]) -> tuple[list[int], list[tuple[int, int]]]:
    """Sorts arr using selection sort without self-swaps, returning (sorted_arr, swaps)."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Selection sort with a strict min_idx != i check before mutating the array and appending to the swap history.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
