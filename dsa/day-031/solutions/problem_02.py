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
