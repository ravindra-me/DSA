# Solution 1: Optimized Bubble Pass Counter

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Bubble sort mechanics, early termination, and swap tracking

## Approach

Make a shallow copy of the input list and run standard Bubble Sort with an early-exit flag. In each outer iteration (pass), iterate through adjacent pairs up to `n - 1 - p`, swapping pairs that are out of order, counting swaps, and setting a flag `swapped = True`. If a pass finishes with `swapped == False`, break immediately. Return the sorted copy, the cumulative swap count, and the number of completed passes.

## Thought Process

Standard Bubble Sort runs $n - 1$ passes unconditionally, leading to an $O(n^2)$ best-case runtime even if the list is already sorted. By introducing a boolean flag `swapped` that is reset to `False` at the start of each pass, we can detect whether any elements were out of order. If no elements were swapped during a pass, the list must already be fully sorted, and we can terminate early. For an array with $n \le 1$, zero passes are needed because no adjacent pairs exist to be checked. For $n \ge 2$, at least one pass must be performed. When early termination occurs, the number of passes completed is precisely the number of outer loop iterations that actually executed.

## Algorithm

1. Check if length $n \le 1$. If so, return `(list(arr), 0, 0)` immediately since no passes or swaps can be performed.
2. Create a copy of `arr` named `res`, and initialize `total_swaps = 0` and `passes_completed = 0`.
3. Iterate with pass index `p` from `0` to `n - 2`.
4. Increment `passes_completed` by 1 and set `swapped = False`.
5. For index `i` from `0` to `n - 2 - p`, compare `res[i]` and `res[i + 1]`. If `res[i] > res[i + 1]`, swap them, increment `total_swaps`, and set `swapped = True`.
6. After the inner loop, if `not swapped`, break out of the outer loop early.
7. Return `(res, total_swaps, passes_completed)`.

## Complexity Analysis

- **Time:** $O(n^2)$ worst and average case when the list is reversed or disordered; $O(n)$ best case when the list is already sorted, as it terminates after 1 pass.
- **Space:** $O(n)$ auxiliary space to return a new sorted list without mutating the original input.

## Edge Cases

- Empty list (`[]`): Handled by the $n \le 1$ check, returns `([], 0, 0)`.
- Single element (`[x]`): Handled by the $n \le 1$ check, returns `([x], 0, 0)`.
- Already sorted list: Completes exactly 1 pass with 0 swaps and exits.
- Reverse sorted list: Completes $n - 1$ passes with the maximum number of swaps $n(n - 1) / 2$.
- List with duplicates: Preserves stability (does not swap equal elements), correctly counting only necessary swaps.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def bubble_sort_analysis(arr: list[int]) -> tuple[list[int], int, int]:
    """Sorts arr using optimized bubble sort and returns (sorted_list, total_swaps, passes)."""
    n = len(arr)
    if n <= 1:
        return list(arr), 0, 0

    res = list(arr)
    total_swaps = 0
    passes_completed = 0

    for p in range(n - 1):
        passes_completed += 1
        swapped = False
        for i in range(n - 1 - p):
            if res[i] > res[i + 1]:
                res[i], res[i + 1] = res[i + 1], res[i]
                total_swaps += 1
                swapped = True
        if not swapped:
            break

    return res, total_swaps, passes_completed
```
