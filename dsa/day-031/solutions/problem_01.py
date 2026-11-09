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
