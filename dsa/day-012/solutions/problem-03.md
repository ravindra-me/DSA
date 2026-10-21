# Solution 3: Next Greater Element II (Circular Array)

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Monotonic stack on circular / wrapped arrays

## Approach

Simulate traversing the array twice using index wrapping modulo `n` (`i % n`) while maintaining a monotonic decreasing stack of indices. As we encounter elements, we pop indices from the stack whose corresponding values are smaller than the current element, setting their next greater value.

## Thought Process

A circular array of length $n$ means any element can search for its next greater element up to $n - 1$ steps ahead, wrapping around the end back to index 0. A naive brute force checks up to $n - 1$ subsequent elements for each element in $O(n^2)$ time, which is too slow for $n = 10^5$.

Instead of physically duplicating the array (which takes extra space), we can iterate through the range $[0, 2n - 1)$ and access elements via `nums[i % n]`. Using a monotonic decreasing stack of indices:
- While the stack is non-empty and the current value `nums[i % n]` is strictly greater than `nums[stack[-1]]`, the current value is the next greater element for `stack.pop()`.
- During the first pass ($i < n$), we push $i$ onto the stack to resolve its next greater element later.
- In the second pass ($n \le i < 2n$), we do not need to push indices onto the stack because all elements needing answers were already pushed during the first pass; we only use elements in the second pass to resolve any remaining pending indices.

## Algorithm

1. Let $n = \text{len}(nums)$. Initialize a result array `result` of size $n$ filled with `-1`.
2. Initialize an empty stack `stack` to store indices of unresolved elements.
3. Loop $i$ from $0$ up to $2n - 1$:
4. Let $idx = i \% n$ and $val = nums[idx]$.
5. While `stack` is not empty and $nums[stack[-1]] < val$, pop index `prev_idx` from `stack` and set `result[prev_idx] = val`.
6. If $i < n$, push $i$ onto `stack`.
7. After the loop finishes, return `result`.

## Complexity Analysis

- **Time:** O(n): Each index from 0 to n - 1 is pushed onto the stack at most once and popped at most once. The loop runs 2n times, doing constant work per iteration aside from stack pops.
- **Space:** O(n): The stack stores at most n indices in the worst case (e.g., strictly decreasing or all identical elements), and the result array takes O(n) space.

## Edge Cases

- Single element: Length 1 array has no other elements to wrap around to, immediately returning `[-1]`.
- All identical elements: No element can be strictly greater than any other; all positions remain `-1`.
- Strictly decreasing array: Elements wrap around and find the largest element at index 0, except for index 0 itself which remains `-1`.
- Strictly increasing array: Every element finds its next neighbor immediately, while the last element remains `-1`.
- Negative numbers and zeros: Handled naturally since comparisons are standard integer comparisons.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def next_greater_elements(nums: list[int]) -> list[int]:
    """Find the next greater circular element for each position."""
    n = len(nums)
    result = [-1] * n
    stack: list[int] = []

    for i in range(2 * n):
        val = nums[i % n]
        while stack and nums[stack[-1]] < val:
            prev_index = stack.pop()
            result[prev_index] = val
        if i < n:
            stack.append(i)

    return result
```
