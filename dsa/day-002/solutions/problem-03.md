# Solution 3: Spiral Matrix Traversal

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** 2D array boundary simulation

## Approach

Maintain four explicit boundaries (`top`, `bottom`, `left`, `right`) representing the remaining unvisited subgrid. Repeatedly traverse along the perimeter edges in clockwise order (top row left-to-right, right column top-to-bottom, bottom row right-to-left, and left column bottom-to-top), shrinking each boundary inward after its traversal until the boundaries cross.

## Thought Process

When traversing a grid in a spiral, the sequence of directions is always fixed: Right, Down, Left, Up, repeating cyclically. 

A naive or state-machine approach might simulate a walker that changes direction upon hitting a visited cell or an edge using an auxiliary 2D boolean array. While this takes $O(m \times n)$ time, it incurs $O(m \times n)$ extra space overhead and involves coordinate checks on every step.

A cleaner, $O(1)$ auxiliary space approach uses boundary pointers (`top`, `bottom`, `left`, `right`). Each complete sweep across an edge consumes an entire row or column. Once the top row is read from `left` to `right`, `top` is incremented. Once the right column is read from `top` to `bottom`, `right` is decremented. Crucially, before traversing leftwards or upwards, we must verify that the corresponding boundary hasn't crossed (i.e., `top <= bottom` and `left <= right`), preventing duplicate traversals in single-row or single-column matrices.

## Algorithm

1. Initialize `top = 0`, `bottom = m - 1`, `left = 0`, and `right = n - 1`.
2. Initialize an empty result list `order`.
3. While `top <= bottom` and `left <= right`:
4. Traverse from `left` to `right` along row `top`, appending each element to `order`, then increment `top`.
5. Traverse from `top` to `bottom` along column `right`, appending each element to `order`, then decrement `right`.
6. If `top <= bottom`, traverse from `right` down to `left` along row `bottom`, appending each element to `order`, then decrement `bottom`.
7. If `left <= right`, traverse from `bottom` down to `top` along column `left`, appending each element to `order`, then increment `left`.
8. Return `order`.

## Complexity Analysis

- **Time:** O(m * n): Every cell in the m x n matrix is visited exactly once.
- **Space:** O(1): Auxiliary space is O(1) beyond the space required to store the returned list of m * n elements.

## Edge Cases

- Single element (1x1): Handled by the first loop iteration which extracts matrix[0][0] and increments top, immediately terminating the loop.
- Single row (1xn): The top row is traversed, top increments past bottom, and the bottom row check (`top <= bottom`) prevents reading backwards.
- Single column (mx1): The top row (1 element) and right column are traversed, then right decrements past left, and the left column check (`left <= right`) prevents duplicate reads.
- Non-square matrices (m != n): Boundaries shrink independently, naturally terminating when whichever dimension is smaller runs out.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Return all elements of matrix in spiral order."""
    if not matrix or not matrix[0]:
        return []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    result: list[int] = []

    while top <= bottom and left <= right:
        # Traverse top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse bottom row, if still within bounds
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse left column, if still within bounds
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
```
