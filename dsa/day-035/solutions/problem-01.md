# Solution 1: Visible Mountains Count

> Spoiler warning: try [the exercise](../exercises/problem-01.md) first.

**Difficulty:** Easy/Medium | **Concept:** Next Greater Element with distance thresholding

## Approach

We process the mountains from right to left using a monotonic stack that maintains elements in strictly decreasing order. For a mountain at index `i`, it can always see its immediate right neighbor. Beyond that, it can see each mountain popped from the stack (which are strictly smaller than `heights[i]`) plus the first mountain remaining on the stack (which is greater than or equal to `heights[i]`), as this element blocks any further vision to the right.

## Thought Process

A brute-force solution checks every pair `(i, j)` with `i < j` and scans all intermediate elements to see if they are strictly less than `min(heights[i], heights[j])`. This takes $O(N^2)$ or $O(N^3)$ time, which is too slow for $N = 10^5$.

To optimize, notice that as mountain `i` looks right, it sees mountain `i + 1`. If `heights[i+1] < heights[i]`, mountain `i` can also see over `i + 1` to see the next taller mountain beyond it, and so on, until it hits a mountain with height $\ge heights[i]$. Any mountain strictly smaller than `heights[i]` that is visible to `i` must have been the peak blocking vision for something closer, which corresponds precisely to the elements maintained in a monotonically decreasing stack when iterating from right to left.

## Algorithm

1. Initialize an array `ans` of length `N` with zeros and an empty stack to store indices.
2. Iterate `i` from `N - 1` down to `0`.
3. While stack is not empty and `heights[stack[-1]] < heights[i]`, pop index `j` from stack and increment `ans[i]` by 1.
4. If stack is not empty after the loop (meaning there is a mountain to the right with `heights[stack[-1]] >= heights[i]`), increment `ans[i]` by 1 because mountain `i` can see that mountain, but no further.
5. Special check: if `stack` is not empty and `heights[stack[-1]] == heights[i]`, mountain `i` can see `stack[-1]`, but popped elements smaller than `heights[i]` were already counted. We then pop equal elements or keep stack strictly monotonic as appropriate. Specifically, push `i` onto stack.
6. Return `ans`.

## Complexity Analysis

- **Time:** O(N) because each element is pushed onto the stack once and popped at most once.
- **Space:** O(N) for the monotonic stack and the output array.

## Edge Cases

- Single mountain (N=1): returns [0].
- Strictly decreasing heights: each mountain can only see its immediate right neighbor, returning [1, 1, ..., 1, 0].
- Strictly increasing heights: mountain i can see mountain i+1 which blocks vision further right, returning [1, 1, ..., 1, 0].
- Equal heights: equal adjacent mountains can see each other, but block vision beyond.

## Implementation

Source: [`solutions/problem_01.py`](../solutions/problem_01.py) · Tests: [`tests/test_problem_01.py`](../tests/test_problem_01.py)

```python
def count_visible_mountains(heights: list[int]) -> list[int]:
    """Calculates the number of visible mountains to the right for each mountain."""
    n = len(heights)
    if n <= 1:
        return [0] * n
    
    ans = [0] * n
    stack = []  # stores indices
    
    for i in range(n - 1, -1, -1):
        count = 0
        while stack and heights[stack[-1]] < heights[i]:
            count += 1
            stack.pop()
            
        if stack:
            if heights[stack[-1]] == heights[i]:
                count += 1
                stack.pop()
            else:
                count += 1
                
        ans[i] = count
        stack.append(i)
        
    return ans
```
