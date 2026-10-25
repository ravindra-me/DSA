# Solution 3: Longest Consecutive Sequence

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** O(1) set/map lookup for connected component discovery

## Approach

Store all numbers in a hash set to enable $O(1)$ average-time lookups. Iterate through the set and only begin counting a consecutive sequence if the current number is the start of a sequence (i.e. `num - 1` is not in the set).

## Thought Process

A naive approach might sort the array in $O(n \log n)$ time, or check for consecutive chains from each number repeatedly, potentially leading to $O(n^2)$ time if sequences are traversed redundantly.

To achieve $O(n)$ time, we need $O(1)$ existence checks, which a hash set provides. If we simply expand forward from every number, an already-visited sequence could be traversed multiple times (e.g., in `[1, 2, 3, 4]`, expanding from 1 takes 4 steps, from 2 takes 3 steps, etc., leading to $O(n^2)$ worst-case).

The key insight is sequence-start identification: a number `x` is the beginning of a sequence if and only if `x - 1` is not present in the set. By only expanding sequences from their minimum element, each element in any consecutive component is visited at most twice (once during the outer loop and once during the inner forward expansion). This guarantees strictly $O(n)$ total time.

## Algorithm

1. Handle the empty list base case: if `nums` is empty, return 0.
2. Convert `nums` into a hash set `num_set` to remove duplicates and allow $O(1)$ membership checks.
3. Initialize `max_length = 0`.
4. For each number `num` in `num_set`:
5. Check if `num - 1` is in `num_set`. If it is, `num` is not the start of a sequence, so continue to the next number.
6. If `num - 1` is not in `num_set`, start a chain with `current_num = num` and `current_streak = 1`.
7. While `current_num + 1` is in `num_set`, increment `current_num` and `current_streak`.
8. Update `max_length = max(max_length, current_streak)`.
9. Return `max_length`.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the number of elements in `nums`. Building the set takes $O(n)$. Each number is checked as a sequence start once, and only sequence starts perform inner while-loop increments. Because every element is visited at most twice during inner traversals, the total work is linear.
- **Space:** $O(n)$ to store the unique elements of `nums` in a hash set.

## Edge Cases

- Empty array: returns 0 immediately.
- Single element: loop runs once, streak is 1, returns 1.
- Duplicates (e.g., `[0, 1, 1, 2]`): `set(nums)` deduplicates values automatically, preventing duplicate-induced infinite loops or inflated counts.
- Negative numbers and zero: negative integers work seamlessly with integer arithmetic and hash set lookup.
- Array with no consecutive elements (all gaps >= 2): every element starts a sequence of length 1, returns 1.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def longest_consecutive_sequence(nums: list[int]) -> int:
    """Return the length of the longest consecutive sequence in O(n) time."""
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only attempt to build sequences from their start
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1

            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1

            if current_streak > max_length:
                max_length = current_streak

    return max_length
```
