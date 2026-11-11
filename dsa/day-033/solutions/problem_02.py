def stable_merge_sort(records: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Sorts records by key using stable merge sort."""
    if len(records) <= 1:
        return list(records)

    mid = len(records) // 2
    left = stable_merge_sort(records[:mid])
    right = stable_merge_sort(records[mid:])

    merged: list[tuple[int, int]] = []
    i = 0
    j = 0
    len_left = len(left)
    len_right = len(right)

    while i < len_left and j < len_right:
        # '<=' ensures stability: ties favor the left subarray (earlier original index)
        if left[i][0] <= right[j][0]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    if i < len_left:
        merged.extend(left[i:])
    if j < len_right:
        merged.extend(right[j:])

    return merged
