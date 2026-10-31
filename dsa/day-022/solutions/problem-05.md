# Solution 5: Container With Most Water

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Greedy area maximization via inward converging pointers

## Approach

Use two pointers starting at opposite ends of the array. At each step, compute the current area formed by the two lines. The bottleneck of the container is always the shorter line; moving the taller line inward could only decrease or match the height while strictly reducing the width, guaranteeing no larger area. Therefore, greedily advance the pointer pointing to the shorter line inward.

## Thought Process

A brute-force solution checks all pairs `(i, j)` with $i < j$, calculating $(j - i) \times \min(\text{height}[i], \text{height}[j])$. This takes $O(n^2)$ time, which is far too slow for $n = 10^5$.

To optimize, observe that the area depends on width $(j - i)$ and height $\min(h[i], h[j])$. Starting with the maximum possible width requires placing pointers at the ends: `left = 0` and `right = n - 1`.

At any configuration `(left, right)`, the water level is bounded by `min(height[left], height[right])`. If `height[left] < height[right]`, any other pair involving `left` (e.g., `(left, right - 1)`, `(left, right - 2)`, etc.) will have a smaller width and a height bounded by `height[left]`. Thus, no other container using `left` can beat the current area formed by `(left, right)`. We can safely discard `left` and increment `left += 1` without missing the optimal solution. Symmetrically, if `height[right] <= height[left]`, we decrement `right -= 1`.

## Algorithm

1. Initialize `left = 0`, `right = len(height) - 1`, and `max_water = 0`.
2. While `left < right`:
3. Compute the current width `width = right - left`.
4. If `height[left] < height[right]`, calculate area using `height[left] * width`, update `max_water = max(max_water, area)`, and increment `left += 1`.
5. Otherwise, calculate area using `height[right] * width`, update `max_water = max(max_water, area)`, and decrement `right -= 1`.
6. Return `max_water` once pointers meet.

## Complexity Analysis

- **Time:** $O(n)$ where $n$ is the length of `height`. Each step moves either `left` or `right` inward by 1, performing at most $n - 1$ steps.
- **Space:** $O(1)$ auxiliary space as only a few pointer and scalar variables are maintained.

## Edge Cases

- Minimum length array ($n = 2$): Loop executes exactly once, computing the only possible area.
- All elements have height 0: Result is correctly 0.
- Uniform heights: Pointers converge inward; the maximum is attained at the widest ends.
- Decreasing or strictly increasing heights: Pointers move correctly toward the taller end.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def max_area(height: list[int]) -> int:
    """Compute the maximum water volume a container can hold."""
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        h_left = height[left]
        h_right = height[right]
        width = right - left

        if h_left < h_right:
            area = h_left * width
            left += 1
        else:
            area = h_right * width
            right -= 1

        if area > max_water:
            max_water = area

    return max_water
```
