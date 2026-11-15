# Solution 1: Sort Colors and Frequencies

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy | **Concept:** Counting Sort with shift offset and key preservation

## Approach

Counting sort works by counting the occurrences of each distinct value in the input array. Because elements can be negative (ranging down to $-10^4$), we determine the minimum and maximum values (or shift by the minimum value) to map each integer to a non-negative index in a frequency array.

## Thought Process

Standard comparison-based sorts like MergeSort or Timsort take $O(n \log n)$ time. However, when the range of possible values $k = \max(nums) - \min(nums) + 1$ is bounded and relatively small (here $k \le 2 \times 10^4 + 1$, while $n \le 10^5$), we can achieve linear time $O(n + k)$ via Counting Sort.

Since indices in an array cannot be negative, we offset every number by $\min(nums)$, so that $\min(nums)$ maps to index 0, and $\max(nums)$ maps to index $\max(nums) - \min(nums)$. After populating the frequency array, we iterate through the frequencies and reconstruct the output array in ascending order.

## Algorithm

1. If `nums` is empty, immediately return an empty list `[]`.
2. Find `min_val = min(nums)` and `max_val = max(nums)`.
3. Allocate a count array of size `max_val - min_val + 1` initialized to zeros.
4. Iterate through each number `x` in `nums`, incrementing `count[x - min_val]`.
5. Iterate through `count` with index `i`. For each index, append `(i + min_val)` to the result list `count[i]` times.
6. Return the reconstructed sorted list.

## Complexity Analysis

- **Time:** O(n + k) where n is the number of elements and k = max(nums) - min(nums) + 1. Since k <= 20001 and n <= 10^5, this runs in strictly linear time.
- **Space:** O(n + k) auxiliary space: O(k) for the frequency count array and O(n) to store the returned sorted output list.

## Edge Cases

- Empty input: Handled as an early return of `[]` before min/max calculation.
- Single element: Range is 0, frequency is 1, returns the single element correctly.
- All identical elements (including negative or zero): Range is 0, counts accumulated at index 0, correctly reconstructs the array.
- Negative numbers and zero: Properly mapped using `min_val` offset so negative values map to valid positive indices.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def counting_sort(nums: list[int]) -> list[int]:
    """Sorts integers in O(n + k) time using counting sort."""
    if not nums:
        return []

    min_val = min(nums)
    max_val = max(nums)
    range_len = max_val - min_val + 1

    counts = [0] * range_len
    for num in nums:
        counts[num - min_val] += 1

    result: list[int] = []
    for idx, count in enumerate(counts):
        if count > 0:
            result.extend([idx + min_val] * count)

    return result
```
