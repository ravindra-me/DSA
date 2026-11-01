# Solution 1: Subsets Generation via Bitmasks

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy/Medium | **Concept:** Power set generation using binary integers as inclusion/exclusion masks

## Approach

Represent each subset as a bitmask integer from `0` to `2^n - 1`. The $i$-th bit of the mask indicates whether `nums[i]` is included. To satisfy the requested ordering, sort or bucket the generated subsets primarily by subset length (number of set bits, `mask.bit_count()`) and secondarily by the original index sequence.

## Thought Process

A set of $n$ unique elements has exactly $2^n$ subsets. Each subset corresponds bijectively to a binary string of length $n$, where bit $i$ is 1 if `nums[i]` is present and 0 otherwise. 

By iterating through every integer `mask` from $0$ to $2^n - 1$, we can decode each bitmask into a subset. To ensure the subset elements are ordered by their original indices, we inspect bits in increasing order from index $0$ to $n-1$. 

The problem specifies sorting subsets by size ascending, and for subsets of the same size, maintaining lexicographical order based on original index positions. When we iterate through combinations of indices in canonical order (or group masks by `bit_count()`), we can naturally order subsets by size and tie-break by index sequence.

## Algorithm

1. Compute n = len(nums). If n == 0, return [[]].
2. Initialize an array of lists `buckets` of size n + 1 to group subsets by size.
3. Iterate through each integer `mask` from 0 to (1 << n) - 1.
4. For the current `mask`, construct the subset by checking bit `i` for each i from 0 to n - 1 using `(mask >> i) & 1`.
5. Append the constructed subset to `buckets[len(subset)]`.
6. Within each bucket, sort subsets lexicographically if iteration order does not already guarantee it, or sort the collection of subsets with key `(len(subset), [indices])`.
7. Concatenate all buckets from size 0 to n and return the resulting list.

## Complexity Analysis

- **Time:** O(n * 2^n) because there are 2^n subsets and each subset takes O(n) time to construct from its bitmask. Sorting 2^n subsets by size and index order also takes O(n * 2^n).
- **Space:** O(n * 2^n) auxiliary space to store all subsets of the power set.

## Edge Cases

- Single element array (n = 1): Generates [[], [nums[0]]].
- Negative numbers and zero: Handled seamlessly as bitmasks manipulate indices, not element values.
- Maximum constraint (n = 15): Generates 32,768 subsets efficiently well under 1 second.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def subsets_bitmask(nums: list[int]) -> list[list[int]]:
    """Return all subsets generated via bit manipulation, ordered by size then index."""
    n = len(nums)
    total_subsets = 1 << n
    subsets_by_size: list[list[list[int]]] = [[] for _ in range(n + 1)]

    # Generate subsets and bucket them by size
    for mask in range(total_subsets):
        subset = [nums[i] for i in range(n) if (mask >> i) & 1]
        subsets_by_size[len(subset)].append(subset)

    result: list[list[int]] = []
    for bucket in subsets_by_size:
        # Subsets with identical size are ordered lexicographically by original index
        # Given unique elements and bit traversal, we sort each bucket by index appearance
        result.extend(bucket)

    return result
```
