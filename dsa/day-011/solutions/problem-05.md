# Solution 5: Largest Rectangle in Histogram

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** monotonic-stack-over-indices

## Approach

Use a monotonic increasing stack storing bar indices. For each bar, when a bar of smaller height is encountered, pop bars from the stack. The popped bar is considered the bottleneck (minimum height) of a rectangle bounded between the previous index in the stack (left limit) and the current index (right limit). By appending a sentinel bar of height 0 at the end, all bars are guaranteed to be popped and evaluated.

## Thought Process

A naive brute-force approach considers every pair of indices $(i, j)$, finds the minimum height in that range, and computes the area: $\min(heights[i..j]) \times (j - i + 1)$. This takes $O(N^2)$ time (or $O(N^3)$ without tracking running minimums), which times out for $N = 10^5$.

Instead of iterating over rectangle endpoints, consider each bar as the *shortest* bar in some maximal rectangle. To maximize the rectangle with height $heights[k]$, we need to find how far it can extend to the left and to the right before encountering a bar shorter than $heights[k]$.

Finding the first smaller element to the left and to the right is the canonical problem solved by a monotonic stack. By maintaining a stack of indices with strictly increasing heights:
- When we see a height smaller than the top of the stack, the current index is the first smaller element to the right of the top.
- The element directly below the top in the stack is the first smaller element to the left.
- The width is therefore $(right\_index - left\_index - 1)$.

## Algorithm

1. Initialize an empty stack to hold indices and set `max_area = 0`.
2. Iterate through the array up to index `len(heights)` (inclusive). When `i == len(heights)`, treat the current height as 0 (sentinel) to flush all remaining items from the stack.
3. While the stack is not empty and the current height is less than the height at the index on top of the stack:
4. Pop the top index `h_idx` from the stack. The height of the rectangle is `heights[h_idx]`.
5. Determine the width: if the stack is now empty, width is `i`; otherwise, width is `i - stack[-1] - 1`.
6. Update `max_area = max(max_area, height * width)`.
7. Push the current index `i` onto the stack.
8. Return `max_area`.

## Complexity Analysis

- **Time:** O(N) because each bar index is pushed onto the stack exactly once and popped at most once.
- **Space:** O(N) in the worst case (e.g., strictly increasing heights) to store indices in the stack.

## Edge Cases

- Single element: The loop processes the element and the sentinel pops it immediately with width 1.
- All elements equal: The stack builds up and then unwinds with widths expanding properly.
- Strictly increasing: The stack grows until the sentinel is hit at index N, then pops all elements in descending order of index.
- Strictly decreasing: Every new element triggers a pop of the preceding element.
- All zeros: Areas computed will all be 0, returning 0.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def largest_rectangle_area(heights: list[int]) -> int:
    """Calculates the maximum rectangular area formed within a histogram in O(N) time."""
    stack: list[int] = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        current_height = 0 if i == n else heights[i]
        while stack and current_height < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area
```
