# Problem 2: Stable Merge Sort on Key-Value Pairs

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Implementing out-of-place merge sort while preserving stability | [Day 33: Merge Sort](../README.md) |

## Problem Statement

You are given a list of tuples `records` where each tuple is `(key, original_index)`. Implement merge sort to sort the list in non-decreasing order based exclusively on `key`. Your implementation must be **stable**: for any two tuples with identical `key`, the tuple that appeared earlier in the input (smaller `original_index`) must appear before the other in the output.

## Input

`records: list[tuple[int, int]]` containing pairs of integer `key` and original 0-based index.

## Output

`list[tuple[int, int]]` sorted primarily by `key` in non-decreasing order, maintaining original order on ties.

## Constraints

- 0 <= len(records) <= 10^4
- -10^9 <= key <= 10^9
- 0 <= original_index < len(records)

## Examples

**Example 1**

```text
Input:  records = [(4, 0), (2, 1), (2, 2), (1, 3)]
Output: [(1, 3), (2, 1), (2, 2), (4, 0)]
```

(2, 1) appears before (2, 2) in the sorted output, maintaining stability.

**Example 2**

```text
Input:  records = []
Output: []
```

Empty list produces empty list.

**Example 3**

```text
Input:  records = [(5, 0), (5, 1), (5, 2)]
Output: [(5, 0), (5, 1), (5, 2)]
```

All keys identical; output preserves exact original order.

## Function Signature

```python
def stable_merge_sort(records: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Sorts records by key using stable merge sort."""
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Implement recursive divide-and-conquer merge sort. During the merge step, if `left[i][0] <= right[j][0]`, always pick from `left` first to guarantee stability.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
