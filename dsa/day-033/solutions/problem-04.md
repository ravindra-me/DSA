# Solution 4: Count Global Inversions

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Augmenting the merge step to count cross-inversions in O(n log n)

## Approach

We can count inversions using a modified Merge Sort. During the divide step, the count of inversions is the sum of inversions in the left half, inversions in the right half, and split inversions where one element comes from the left and the other from the right. When merging two sorted halves `left` and `right`, whenever an element from `right` is smaller than the current element in `left`, it is smaller than all remaining elements in `left`, adding `len(left) - i` inversions in $O(1)$ time.

## Thought Process

A brute-force solution checks every pair $(i, j)$ with $i < j$, checking if $nums[i] > nums[j]$, which takes $O(n^2)$ time. Given $n \le 5 \times 10^4$, $O(n^2)$ requires around $2.5 \times 10^9$ operations and will time out.

To achieve $O(n \log n)$, we recognize that counting inversions is closely related to sorting: an inversion is simply a pair of elements that is out of sorted order. If we recursively sort and count inversions in the left half and right half, the only remaining inversions are cross-inversions (pairs $(i, j)$ where $i$ is in the left subarray and $j$ is in the right subarray).

Because both halves are sorted prior to the merge step, when we compare `left[i]` and `right[j]`: if `left[i] <= right[j]`, `left[i]` cannot form an inversion with `right[j]` or anything after it. But if `left[i] > right[j]`, then since `left` is sorted, every element from `left[i]` to `left[len(left) - 1]` is also strictly greater than `right[j]`. We can therefore count `len(left) - i` inversions in $O(1)$ time and advance $j$. Merging takes linear time at each recursion level, yielding the standard merge sort recurrence $T(n) = 2T(n/2) + O(n)$, which solves to $O(n \log n)$.

## Algorithm

1. Create a helper function `sort_and_count(arr, temp, left, right)` that sorts the subarray `arr[left:right + 1]` in-place using a scratch buffer `temp` and returns the inversion count.
2. Base case: If `left >= right`, return 0 since a subarray of size 0 or 1 contains no inversions.
3. Divide: Calculate `mid = (left + right) // 2`. Recursively call `sort_and_count` on `[left, mid]` and `[mid + 1, right]`, summing their returned counts.
4. Merge step: Maintain pointer `i = left` for the left half and `j = mid + 1` for the right half, and write into `temp[k]` starting at `k = left`.
5. While both halves have elements: if `arr[i] <= arr[j]`, copy `arr[i]` to `temp[k]` and increment `i`. Otherwise (`arr[i] > arr[j]`), add `(mid - i + 1)` to the split inversion count, copy `arr[j]` to `temp[k]`, and increment `j`.
6. Copy any remaining elements from either half into `temp`, and then copy the merged elements from `temp[left:right + 1]` back to `arr[left:right + 1]`.
7. Return the sum of left inversions, right inversions, and split inversions.

## Complexity Analysis

- **Time:** $O(n \log n)$ because the recursion tree has depth $O(\log n)$ and the merge step at each level processes $n$ elements in $O(n)$ time.
- **Space:** $O(n)$ auxiliary space for the temporary buffer used during merging and $O(\log n)$ recursion stack frames.

## Edge Cases

- Empty array or single-element array: returns 0 immediately because `len(nums) < 2`.
- Already sorted array in ascending order: returns 0; no cross-inversions are triggered.
- Reverse sorted array: returns the maximum possible number of inversions, $n(n - 1) / 2$.
- Duplicate elements: handled correctly using `<=` during merge comparison (`arr[i] <= arr[j]`) so identical values do not count as inversions.
- Negative numbers and large values: standard numerical comparisons work without overflow in Python.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
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
```
