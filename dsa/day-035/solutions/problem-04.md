# Solution 4: Maximal Rectangle of Ones in Binary Grid

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** 2D Grid reduction to Monotonic Stack Histogram

## Approach

We maintain a 1D array representing the continuous height of consecutive `'1'`s for each column up to the current row. For each row, updating this height array transforms the problem into finding the 'Largest Rectangle in Histogram', which can be solved in $O(C)$ time using a monotonic stack. By repeating this for all $R$ rows, the total time complexity becomes $O(R 	imes C)$.

## Thought Process

A brute-force solution checking every possible subgrid of size $(r_1, c_1)$ to $(r_2, c_2)$ and verifying if it contains only `'1'`s takes $O(R^3 C^3)$ time, or $O(R^2 C^2)$ using 2D prefix sums. We can do much better by viewing each row as the base of a histogram. If matrix cell $(r, c)$ is `'1'`, the height of column $c$ increases by 1 relative to row $r-1$; if it is `'0'`, the height resets to 0. For each row, calculating the maximal rectangular area in the histogram defined by these column heights takes linear time $O(C)$ with a monotonic increasing stack. Total time is $O(R 	imes C)$, which is optimal since every cell must be inspected at least once.

## Algorithm

1. Initialize `max_area = 0` and a `heights` array of size $C$ filled with zeros.
2. For each row in `matrix`:
3. Update `heights[c]`: if `matrix[r][c] == '1'`, increment `heights[c]` by 1; otherwise, reset `heights[c] = 0`.
4. Compute the largest rectangle area in `heights` using a monotonic stack:
5. Iterate through `heights` up to index $C$ (using 0 as a sentinel height at index $C$).
6. While the stack is not empty and the current height is less than `heights[stack[-1]]`:
7. Pop the top height `h = heights[stack.pop()]`.
8. Determine the width `w`: if the stack is empty, `w = i`; else `w = i - stack[-1] - 1`.
9. Update `max_area = max(max_area, h * w)`.
10. Push current column index `i` onto the stack.
11. Return `max_area`.

## Complexity Analysis

- **Time:** $O(R \times C)$ where $R$ is the number of rows and $C$ is the number of columns. Processing each row updates heights in $O(C)$ time and runs the monotonic stack in $O(C)$ time.
- **Space:** $O(C)$ auxiliary space to store the column heights array and the monotonic stack.

## Edge Cases

- Single cell matrix `[['0']]` or `[['1']]`: Correctly yields 0 or 1 respectively.
- All zeros grid: Heights remain zero across all rows, max area returned is 0.
- All ones grid: Stack correctly computes total area $R \times C$.
- Single row or single column matrix: Correctly computes maximum consecutive ones length.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
def maximal_rectangle(matrix: list[list[str]]) -> int:
    """Calculates the area of the largest rectangle containing only '1's in a binary grid."""
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for c in range(cols):
            if row[c] == '1':
                heights[c] += 1
            else:
                heights[c] = 0

        stack = []
        for i in range(cols + 1):
            current_height = heights[i] if i < cols else 0
            while stack and current_height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

    return max_area
```
