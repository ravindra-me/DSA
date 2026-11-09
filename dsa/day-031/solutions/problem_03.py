def sort_k_sorted(arr: list[int], k: int) -> list[int]:
    """Sorts a k-sorted array in-place in O(n * k) time using insertion sort."""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
