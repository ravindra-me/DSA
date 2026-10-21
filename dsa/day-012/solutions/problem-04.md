# Solution 4: Largest Rectangle in Histogram

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Finding left and right smaller boundaries to calculate maximal area

## Approach

For each bar to be the bottleneck (minimum height) of a rectangle, we need to find how far it can extend to the left and right. This corresponds to finding the first strictly smaller bar to its left and right. A monotonic increasing stack stores indices of bars; whenever a bar shorter than the stack top is encountered, the popped bar's boundaries are fully determined, allowing us to compute its maximal rectangle area in $O(1)$ time.

## Thought Process

A brute-force solution considers every possible pair of left and right boundaries $(i, j)$, determines the minimum height in that range, and computes the area in $O(n^3)$ or $O(n^2)$ time. This is far too slow for $n = 10^5$.

Instead of iterating over boundaries, invert the perspective: iterate over each bar $i$ and ask, 'What is the largest rectangle where bar $i$ is the limiting (shortest) height?' That rectangle extends left until the first bar strictly shorter than `heights[i]`, and right until the first bar strictly shorter than `heights[i]`.

Finding the previous smaller element and the next smaller element is the quintessential application of a monotonic stack. By maintaining a stack of indices with increasing heights, when we see a height smaller than the top of the stack, the current index serves as the right boundary for the popped element, and the new top of the stack serves as the left boundary. Appending a dummy 0 at the end forces all remaining elements in the stack to be popped and processed.

## Algorithm

1. Initialize an empty stack `stack` to store indices of bars in strictly increasing order of height, and `max_area = 0`.
2. Append a sentinel height `0` to the end of `heights` (or iterate up to index `len(heights)` treating the final height as `0`) to ensure every index gets popped.
3. Iterate through index `i` from `0` to `len(heights)`:
4. While `stack` is not empty and the current bar's height is strictly less than `heights[stack[-1]]`:
5. Pop the top index `h_idx` from `stack`. The height of the rectangle is `h = heights[h_idx]`.
6. Determine the width: if `stack` is empty, the rectangle extends from index `0` to `i - 1`, so `width = i`. Otherwise, it extends from `stack[-1] + 1` to `i - 1`, so `width = i - stack[-1] - 1`.
7. Update `max_area = max(max_area, h * width)`.
8. Push current index `i` onto `stack`.
9. Return `max_area`.

## Complexity Analysis

- **Time:** O(n) where n is the number of bars. Each bar is pushed onto the stack exactly once and popped at most once.
- **Space:** O(n) for the monotonic stack storing at most n + 1 indices in the worst case (strictly increasing heights).

## Edge Cases

- Single element: The loop processes the element and the trailing 0 sentinel immediately calculates height * 1.
- All heights are zero: Every calculated height will be 0, returning 0 correctly.
- All heights are equal: Each element is popped by subsequent or final sentinel, properly computing the full span width.
- Strictly increasing or strictly decreasing heights: Handled naturally; monotonic stack maintains correct boundaries without special branching.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def largest_rectangle_area(heights: list[int]) -> int:
    """Find the area of the largest rectangle in a histogram."""
    stack: list[int] = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        current_height = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > current_height:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)

    return max_area
```
