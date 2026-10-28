# Solution 2: Majority Element Identifier

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** majority element counting and Boyer-Moore voting

## Approach

We use the Boyer-Moore Voting Algorithm to find the majority element in $O(n)$ time and $O(1)$ auxiliary space. By pairing up different elements and discarding them, the element with strictly more than $\lfloor n / 2 \rfloor$ occurrences is guaranteed to survive as the final candidate.

## Thought Process

A brute-force approach counts the occurrences of each element by scanning the list repeatedly, taking $O(n^2)$ time. A hash map counting frequencies improves this to $O(n)$ time but uses $O(n)$ extra space.

To achieve $O(1)$ space, notice the defining condition: the majority element appears more than $n / 2$ times. If we treat each occurrence of a candidate as $+1$ and any other element as $-1$, the majority element's total count across the entire array will be strictly positive ($> 0$). When the running count drops to zero, any prefix discarded has balanced votes, meaning the majority element must still form the majority of the remaining suffix. Thus, tracking a single candidate and a vote balance guarantees we identify the correct majority element.

## Algorithm

1. Initialize `candidate = None` and `count = 0`.
2. Iterate through each number `num` in `nums`.
3. If `count == 0`, assign `candidate = num` and set `count = 1`.
4. Else if `num == candidate`, increment `count` by 1.
5. Else, decrement `count` by 1.
6. Return `candidate` after scanning the entire array.

## Complexity Analysis

- **Time:** O(n) where n is the length of `nums`, because we perform a single linear scan over the list.
- **Space:** O(1) auxiliary space, as only two scalar variables (`candidate` and `count`) are maintained.

## Edge Cases

- Single-element array (e.g. `[1]`): `count` starts at 0, picks the element as candidate, and terminates with it.
- Array with all identical elements: `count` increments monotonically up to $n$ and candidate remains unchanged.
- Negative numbers and zero: Handled transparently by standard integer equality comparison.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def majority_element(nums: list[int]) -> int:
    """Find and return the majority element (> n // 2 times)."""
    candidate = 0
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate
```
