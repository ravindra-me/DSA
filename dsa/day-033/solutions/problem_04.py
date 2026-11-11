def count_inversions(nums: list[int]) -> int:
    """Counts the total number of inversions in nums in O(n log n) time."""
    if len(nums) < 2:
        return 0

    # Work on a copy to avoid mutating the caller's input
    arr = list(nums)
    temp = [0] * len(arr)

    def _merge_and_count(left: int, mid: int, right: int) -> int:
        inversions = 0
        i = left
        j = mid + 1
        k = left

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inversions += mid - i + 1
                j += 1
            k += 1

        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1

        arr[left : right + 1] = temp[left : right + 1]
        return inversions

    def _sort_and_count(left: int, right: int) -> int:
        if left >= right:
            return 0
        mid = (left + right) // 2
        inv_left = _sort_and_count(left, mid)
        inv_right = _sort_and_count(mid + 1, right)
        inv_split = _merge_and_count(left, mid, right)
        return inv_left + inv_right + inv_split

    return _sort_and_count(0, len(arr) - 1)
