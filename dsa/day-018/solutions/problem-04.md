# Solution 4: Longest Consecutive Sequence

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** O(1) lookups and sequence boundary detection with HashSet

## Approach

Insert all numbers into a `set` to achieve $O(1)$ lookups. Iterate through the numbers in the set, identifying sequence starters as numbers `x` where `x - 1` is not present in the set. For each starter, incrementally count consecutive numbers (`x + 1`, `x + 2`, ...) to find the length of the sequence.

## Thought Process

Sorting the array would yield an $O(N \log N)$ solution, but the problem requires $O(N)$ time complexity. To avoid sorting, we can use a hash set for $O(1)$ presence checks. A naive approach might count consecutive numbers starting from every element, leading to $O(N^2)$ time if long sequences are repeatedly traversed. To achieve linear time, we only start expanding a sequence if the current number is the *beginning* of a sequence (i.e., `num - 1` is NOT in the set). Since each number is part of at most one sequence traversal (when starting from its sequence head), every element is visited a constant number of times, guaranteeing $O(N)$ overall runtime.

## Algorithm

1. Convert the input list `nums` into a HashSet `num_set` to remove duplicates and enable $O(1)$ lookups.
2. Initialize `max_length = 0`.
3. For each element `num` in `num_set`:
4. Check if `num - 1` is in `num_set`. If it is, skip `num` because it cannot be the start of a longest sequence.
5. If `num - 1` is not in `num_set`, `num` is the start of a sequence. Set `current_num = num` and `current_length = 1`.
6. While `current_num + 1` is in `num_set`, increment `current_num` and `current_length` by 1.
7. Update `max_length = max(max_length, current_length)`.
8. Return `max_length`.

## Complexity Analysis

- **Time:** $O(N)$ because converting the array to a set takes $O(N)$ time, and each number is visited at most twice (once in the loop and at most once during sequence expansion).
- **Space:** $O(N)$ to store unique elements in the hash set.

## Edge Cases

- Empty input list: handled by initializing `max_length = 0`, returning 0 immediately.
- Single element list: sequence length is 1.
- Duplicates present: converting to a set automatically removes duplicates without affecting sequence continuity.
- Negative numbers and zero: negative numbers work seamlessly with addition/subtraction in Python integers.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def longest_consecutive(nums: list[int]) -> int:
    """Return length of longest consecutive elements sequence in O(N) time."""
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Check if `num` is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            if current_length > max_length:
                max_length = current_length

    return max_length
```
