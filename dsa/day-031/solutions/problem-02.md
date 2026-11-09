# Solution 2: Minimal Write Selection Sort

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Selection sort write minimization and tracking index updates

## Approach

Selection sort divides the list into a sorted prefix and an unsorted suffix. In each pass $i$ from $0$ to $n-2$, scan the suffix to find the minimum element's first occurrence (`min_idx`). To minimize write operations, only swap `arr[i]` and `arr[min_idx]` when `min_idx != i`, appending `(i, min_idx)` to the swaps list.

## Thought Process

Standard selection sort performs $O(n^2)$ comparisons regardless of input distribution, but its key advantage over algorithms like insertion sort or bubble sort is that it performs at most $O(n)$ writes (swaps). In hardware with write-endurance limitations (like flash memory or EEPROM), minimizing writes is critical.

To implement this write minimization without modifying the core selection sort logic, we track the index of the minimum element in `arr[i:n]`. By using a strict inequality `<` during the scan, we automatically choose the earliest (leftmost) occurrence in the case of duplicates. After finding `min_idx`, we check if `min_idx != i`. If true, we swap elements at $i$ and `min_idx`, and record the swap `(i, min_idx)`. If false, the element is already in its proper position, so we avoid a redundant self-swap.

## Algorithm

1. Create a copy of `arr` or work directly on a mutable copy `res` to avoid modifying input in-place unexpectedly (or sort a copy and return it).
2. Initialize an empty list `swaps = []`.
3. Let `n = len(res)`. Loop `i` from `0` to `n - 2`.
4. Initialize `min_idx = i`.
5. Loop `j` from `i + 1` to `n - 1`. If `res[j] < res[min_idx]`, update `min_idx = j`.
6. If `min_idx != i`, swap `res[i]` and `res[min_idx]`, and append `(i, min_idx)` to `swaps`.
7. Return `(res, swaps)`.

## Complexity Analysis

- **Time:** $O(n^2)$ comparisons in all cases because for each $i$, the loop scans all $j > i$.
- **Space:** $O(n)$ auxiliary space to return the sorted copy and up to $n - 1$ recorded swap pairs.

## Edge Cases

- Empty array (`len(arr) == 0`): The loop range $0$ to $-2$ does not execute; returns `([], [])`.
- Single element (`len(arr) == 1`): The loop range $0$ to $-1$ does not execute; returns `([arr[0]], [])`.
- Already sorted array: `min_idx` will equal `i` at each iteration, resulting in 0 swaps recorded.
- Duplicate minimums: Strict inequality `<` ensures the first (leftmost) minimum index is selected.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def selection_sort_tracked(arr: list[int]) -> tuple[list[int], list[tuple[int, int]]]:
    """Sorts arr using selection sort without self-swaps, returning (sorted_arr, swaps)."""
    res = list(arr)
    n = len(res)
    swaps: list[tuple[int, int]] = []

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if res[j] < res[min_idx]:
                min_idx = j
        if min_idx != i:
            res[i], res[min_idx] = res[min_idx], res[i]
            swaps.append((i, min_idx))

    return res, swaps
```
