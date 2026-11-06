# Solution 5: Search a 2D Matrix II

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** matrix-binary-search

## Approach

Start at the top-right corner of the matrix. If the current element is greater than `target`, move left (eliminating the current column). If it is smaller than `target`, move down (eliminating the current row). Repeat until `target` is found or the matrix boundaries are exceeded.

## Thought Process

A naive approach checks every element in $O(m \times n)$ time. Searching each row with binary search takes $O(m \log n)$ time. However, starting from the top-right corner (row 0, column $n-1$) allows us to treat the matrix as a decision tree: elements to the left are smaller, and elements below are larger. In each step, we eliminate either an entire row or an entire column, reaching an optimal $O(m + n)$ time complexity.

## Algorithm

1. If the matrix is empty (no rows or no columns), return False.
2. Initialize pointer `row = 0` and pointer `col = len(matrix[0]) - 1`.
3. Loop while `row < len(matrix)` and `col >= 0`:
4. If `matrix[row][col] == target`, return True.
5. If `matrix[row][col] > target`, decrement `col` by 1.
6. Else (`matrix[row][col] < target`), increment `row` by 1.
7. If the loop exits without finding the target, return False.

## Complexity Analysis

- **Time:** O(m + n) where m is the number of rows and n is the number of columns. In each iteration we decrement col or increment row, performing at most m + n steps.
- **Space:** O(1) auxiliary space as we only store two integer indices.

## Edge Cases

- Single element matrix: handled correctly by starting row 0, col 0.
- Target smaller than all elements: col decrements to -1 immediately, returning False.
- Target larger than all elements: row increments out of bounds, returning False.
- Negative values and duplicates: work naturally since row/column monotonic ordering properties hold.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Return True if target exists in matrix, else False."""
    if not matrix or not matrix[0]:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    row = 0
    col = cols - 1
    
    while row < rows and col >= 0:
        val = matrix[row][col]
        if val == target:
            return True
        elif val > target:
            col -= 1
        else:
            row += 1
            
    return False
```
