# Solution 2: Stable Merge Sort on Key-Value Pairs

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Implementing out-of-place merge sort while preserving stability

## Approach

Merge sort follows a divide-and-conquer paradigm: divide the list into two halves, recursively sort both halves, and merge the sorted halves. Stability is guaranteed during the merge step by always taking the element from the left sublist whenever its `key` is less than or equal to the `key` of the element from the right sublist.

## Thought Process

A stable sort preserves the relative order of elements that have equal keys. Python's built-in `list.sort()` is stable (Timsort), but implementing merge sort directly illustrates the mechanism of stability.

In standard merge sort, when merging two sorted arrays `left` and `right`, comparing `left[i][0] <= right[j][0]` ensures that ties are broken in favor of the element from `left`, which appeared earlier in the original list. If strict inequality `<` were used instead, elements from `right` would be taken before equal elements from `left`, breaking stability.

Recursively splitting the array into halves until singletons remain takes $O(\log n)$ levels of recursion. Merging takes $O(n)$ work per level, yielding a total time complexity of $O(n \log n)$ and auxiliary space of $O(n)$.

## Algorithm

1. Check base cases: if the length of `records` is 0 or 1, return a copy of `records` directly.
2. Find the midpoint `mid = len(records) // 2` and recursively sort `left = records[:mid]` and `right = records[mid:]`.
3. Initialize two pointers `i = 0` for `left` and `j = 0` for `right`, and an empty list `merged`.
4. While both pointers are within bounds, compare the keys: if `left[i][0] <= right[j][0]`, append `left[i]` to `merged` and advance `i`. Otherwise, append `right[j]` to `merged` and advance `j`.
5. Append any remaining elements from `left` and `right` to `merged`.
6. Return the merged list.

## Complexity Analysis

- **Time:** $O(n \log n)$, where $n$ is the number of records. The array is split in half at each level ($	ext{depth} = \log_2 n$), and each merge step scans elements linearly in $O(n)$ time.
- **Space:** $O(n)$ auxiliary space to allocate slices and temporary merged buffers during the recursive steps.

## Edge Cases

- Empty list: returns empty list immediately without recursing.
- Single element: returns the single element list directly.
- All elements have identical keys: the `<=` condition ensures all elements preserve their initial relative order.
- Already sorted or reverse sorted: handles uniformly in $O(n \log n)$ time while preserving original relative order for any duplicates.
- Negative keys and large magnitude keys (up to $10^9$): integer comparisons handle negative numbers and large bounds natively.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
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
```
