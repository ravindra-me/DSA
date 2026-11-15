# Solution 2: Sort Pairs by Secondary Key Stably

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Stable Counting Sort using prefix sums

## Approach

We implement the classic stable counting sort using prefix sums over the score range `[0, 100]`. By scanning the input backwards and using the prefix sums as 1-based output positions, elements with equal keys maintain their original relative order.

## Thought Process

A comparison-based sort like Timsort runs in $O(N \log N)$ time. However, the keys (scores) are integers strictly bounded in $[0, 100]$, which is a very small range ($K = 101$). Counting sort can achieve linear $O(N + K)$ time.

To ensure stability without relying on linked buckets or dynamic lists, we use the prefix-sum counting sort technique:
1. Count frequencies of each score in an array `count` of size 101.
2. Compute prefix sums in-place so that `count[v]` tells us the total number of elements with score $\le v$.
3. Traverse the input array in reverse (from index $N-1$ down to 0). For each element with score $v$, its destination index in the output array is `count[v] - 1`. We then decrement `count[v]`. Traversing right-to-left ensures that later elements with the same score end up at higher indices, preserving stability.

## Algorithm

1. Handle the base case: if `records` is empty or has length 1, return a copy of `records`.
2. Initialize an array `count` of size 101 with zeros.
3. Iterate through `records` and increment `count[score]` for each pair.
4. Compute prefix sums: for `i` from 1 to 100, set `count[i] += count[i - 1]`.
5. Allocate an output array `output` of length equal to `len(records)`.
6. Iterate through `records` in reverse (from index `len(records) - 1` down to 0).
7. For each item `(id, score)`, place it at `output[count[score] - 1]`, then decrement `count[score]` by 1.
8. Return `output`.

## Complexity Analysis

- **Time:** O(N + K) where N is the number of records and K = 101 is the range of possible score values. With K being constant, this is O(N).
- **Space:** O(N + K) auxiliary space to store the output array and the frequency/prefix sum array.

## Edge Cases

- Empty input (`records = []`): handled immediately by returning an empty list.
- Single element (`len(records) == 1`): returns a shallow copy of the list.
- All elements have identical scores: reverse placement correctly preserves original order for all items.
- Scores at boundary values 0 and 100: correctly indexed in the 0..100 array without out-of-bounds errors.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def stable_sort_scores(records: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Stably sorts pairs by score using prefix-sum counting sort."""
    if len(records) <= 1:
        return list(records)

    max_score = 100
    count = [0] * (max_score + 1)

    # 1. Count frequencies
    for _, score in records:
        count[score] += 1

    # 2. Compute prefix sums (cumulative counts)
    for score in range(1, max_score + 1):
        count[score] += count[score - 1]

    # 3. Build output array iterating right-to-left to ensure stability
    output: list[tuple[str, int]] = [("", 0)] * len(records)
    for i in range(len(records) - 1, -1, -1):
        item = records[i]
        score = item[1]
        output[count[score] - 1] = item
        count[score] -= 1

    return output
```
