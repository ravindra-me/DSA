# Problem 2: Sort Pairs by Secondary Key Stably

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Stable Counting Sort using prefix sums | [Day 37: Counting, Bucket & Radix Sort](../README.md) |

## Problem Statement

You are given a list of pairs `(id, score)` where `id` is a string identifier and `score` is an integer in the range `[0, 100]`. Stably sort the pairs in ascending order of `score`.

Because the sort must be stable, if two pairs have the same `score`, their original relative order from the input list must be strictly preserved.

## Input

A list of tuples `records: list[tuple[str, int]]` where each tuple is `(id, score)`.

## Output

A list of tuples `list[tuple[str, int]]` sorted by `score` in ascending order stably.

## Constraints

- 0 <= len(records) <= 10^5
- 0 <= score <= 100
- 1 <= len(id) <= 20

## Examples

**Example 1**

```text
Input:  records = [("Alice", 85), ("Bob", 70), ("Charlie", 85), ("Dave", 90)]
Output: [("Bob", 70), ("Alice", 85), ("Charlie", 85), ("Dave", 90)]
```

Alice and Charlie both have a score of 85. Alice appeared before Charlie in the input, so Alice appears first in the output.

**Example 2**

```text
Input:  records = []
Output: []
```

Empty list produces empty list.

## Function Signature

```python
def stable_sort_scores(records: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Stably sorts pairs by score using prefix-sum counting sort."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Use standard cumulative prefix-sum counting sort and iterate through the input backwards to guarantee stability in O(n + k) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
