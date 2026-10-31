# Solution 2: Remove Duplicates from Sorted Array II

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Same-direction read/write pointers with frequency thresholding

## Approach

Maintain a write pointer `write` representing the index where the next valid element should be placed. Since an element can appear at most twice, an element `nums[read]` can be written if either `write < 2` or `nums[read] != nums[write - 2]`. Because the input is sorted, comparing against the element written two positions prior guarantees that no number appears more than twice.

## Thought Process

A brute-force approach might count occurrences using a hash table or pop extra elements from the list. However, popping elements from an array costs $O(n)$ per deletion, leading to $O(n^2)$ total time. Allocating a new list takes $O(n)$ auxiliary space, violating the in-place requirement.

To achieve $O(n)$ time and $O(1)$ space, we use two pointers: a `read` pointer scanning through each element of `nums`, and a `write` pointer pointing to the destination for accepted elements.

Because `nums` is already sorted, all identical values are contiguous. The question is: when should we allow `nums[read]` to be written? We want at most 2 copies of each distinct value. If `nums[read] == nums[write - 2]`, it means the value at `write - 2` and the value at `write - 1` are already equal to `nums[read]`, so writing `nums[read]` would create a 3rd instance. If `nums[read] != nums[write - 2]`, it cannot possibly be the 3rd instance. Thus, the condition `write < 2 or nums[read] != nums[write - 2]` cleanly decides retention without any extra frequency counters or state tracking.

## Algorithm

1. If the length of `nums` is 2 or less, return `len(nums)` directly as no element can appear more than twice.
2. Initialize `write = 2` (the first two elements are always kept).
3. Iterate `read` from index 2 to `len(nums) - 1`.
4. If `nums[read] != nums[write - 2]`, assign `nums[write] = nums[read]` and increment `write` by 1.
5. Return `write` as the new length `k`.

## Complexity Analysis

- **Time:** O(n) where n is the number of elements in nums. Each element is inspected once by the read pointer and written at most once.
- **Space:** O(1) auxiliary space as all modifications are performed in-place using two integer pointers.

## Edge Cases

- Array with length <= 2: trivially valid, handled by early return or naturally if starting write at 2.
- All elements identical (e.g., [1, 1, 1, 1]): correctly reduced to exactly two copies.
- Array with no duplicates (e.g., [1, 2, 3, 4]): all elements are retained unchanged, write reaches len(nums).
- Negative numbers and zeroes: values work identically due to comparison by value.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def remove_duplicates_at_most_two(nums: list[int]) -> int:
    """Modify nums in-place so each element appears at most twice. Return new length."""
    if len(nums) <= 2:
        return len(nums)

    write = 2
    for read in range(2, len(nums)):
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1

    return write
```
