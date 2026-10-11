# Solution 5: First Missing Positive

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** index-as-hash-key / cycle placement in-place

## Approach

We place each positive number `x` within the range `1 <= x <= n` into its corresponding index `x - 1` using in-place swaps (cyclic sort). After placing numbers in their correct positions, we scan the array from left to right; the first index `i` where `nums[i] != i + 1` reveals that `i + 1` is the missing positive. If all positions `0` to `n - 1` hold `1` to `n`, the answer is `n + 1`.

## Thought Process

A naive approach uses a hash set to store all elements in $O(n)$ time and $O(n)$ auxiliary space, then searches for $1, 2, 3, \dots$. However, the problem strictly requires $O(1)$ auxiliary space. Key insight: for an array of length $n$, the smallest missing positive integer MUST lie in the range $[1, n + 1]$. This is because even if the array contains $1, 2, \dots, n$, the missing number is $n + 1$. We can use the input array itself as a hash table by attempting to move every element $x \in [1, n]$ to index $x - 1$. Since each swap places at least one number in its correct final position, the total number of swaps across the entire algorithm is bounded by $n$, yielding an $O(n)$ time and $O(1)$ auxiliary space solution.

## Algorithm

1. Iterate through the array with index `i` from `0` to `n - 1`.
2. While `1 <= nums[i] <= n` and `nums[nums[i] - 1] != nums[i]`, swap `nums[i]` with `nums[nums[i] - 1]`. This cyclic swapping continues until the element at index `i` is either out of the range `[1, n]` or is a duplicate already placed at its target index.
3. Iterate through the array again from index `i = 0` to `n - 1`.
4. If `nums[i] != i + 1`, return `i + 1` as the smallest missing positive integer.
5. If all positions `0` through `n - 1` contain `1` through `n`, return `n + 1`.

## Complexity Analysis

- **Time:** $O(n)$ - Each swap places at least one element into its correct index permanently. Thus, the inner `while` loop executes at most $n$ times across the entire runtime.
- **Space:** $O(1)$ auxiliary space - Modifies the input array in place without allocating additional data structures.

## Edge Cases

- Array with all negative numbers or zeros (e.g. `[-1, -2, 0]`): all cyclic swaps are skipped, loop finds `nums[0] != 1` and returns `1`.
- Array with duplicate positive values (e.g. `[1, 1]`): the duplicate check `nums[nums[i] - 1] != nums[i]` prevents infinite swapping loops.
- Array already sorted from `1` to `n` (e.g. `[1, 2, 3]`): second loop completes and correctly returns `n + 1` = `4`.
- Single element array (e.g. `[2]` or `[1]`): correctly returns `1` or `2` respectively.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def first_missing_positive(nums: list[int]) -> int:
    """Return the smallest missing positive integer in O(n) time and O(1) space."""
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_idx = nums[i] - 1
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1
```
