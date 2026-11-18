# Solution 5: Vertical Order Traversal of a Binary Tree

> Spoiler warning: try [the exercise](../exercises/problem-05.md) first.

**Difficulty:** Hard | **Concept:** Coordinate-based BFS / DFS with multi-key sorting

## Approach

Assign 2D coordinates `(row, col)` to each node starting with `(0, 0)` at the root. Collect tuples of `(col, row, val)` using any traversal (BFS or DFS), sort all tuples lexicographically, and group the values by column.

## Thought Process

The problem specifies a coordinate system where moving left adds 1 to `row` and subtracts 1 from `col`, while moving right adds 1 to `row` and adds 1 to `col`.

The final ordering requires:
1. Columns from leftmost to rightmost (ascending `col`).
2. Within the same column, top to bottom (ascending `row`).
3. Within the same column and same row, ascending node value (`val`).

Notice that standard Python tuple sorting on `(col, row, val)` naturally enforces this exact three-tier priority ordering. We can traverse the entire tree using standard BFS or DFS in $O(N)$ time, record `(col, row, val)` for every node, sort the collected entries in $O(N \log N)$ time, and then group by `col` using `itertools.groupby` or a simple linear pass.

## Algorithm

1. If the root is None, return an empty list.
2. Traverse the tree using BFS (queue of `(node, row, col)`) or DFS, collecting `(col, row, node.val)` for every node.
3. Sort the collected nodes list lexicographically by `(col, row, val)`.
4. Iterate through the sorted tuples, grouping elements by `col` into separate sublists.
5. Return the list of grouped sublists.

## Complexity Analysis

- **Time:** O(N log N) where N is the number of nodes in the binary tree, dominated by sorting the list of nodes. The tree traversal takes O(N) time and the final grouping takes O(N) time.
- **Space:** O(N) to store the coordinate tuples and the BFS queue or DFS recursion stack.

## Edge Cases

- Empty tree (root is None): handled immediately by returning an empty list [].
- Single node: sorted list has 1 element, resulting in [[val]].
- Skewed trees (linked list structure): handled correctly as column and row indices update incrementally without recursion overflow if using BFS.
- Nodes in the same row and column with identical or different values: multi-key sorting by (col, row, val) ensures correct tie-breaking.

## Implementation

Source: [`solutions/problem_05.py`](../solutions/problem_05.py) · Tests: [`tests/test_problem_05.py`](../tests/test_problem_05.py)

```python
from collections import deque
from itertools import groupby


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def vertical_traversal(root: TreeNode | None) -> list[list[int]]:
    """Return vertical order traversal of the binary tree sorted by column, row, and value."""
    if not root:
        return []

    nodes: list[tuple[int, int, int]] = []
    queue: deque[tuple[TreeNode, int, int]] = deque([(root, 0, 0)])

    while queue:
        node, row, col = queue.popleft()
        nodes.append((col, row, node.val))
        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    nodes.sort()

    result: list[list[int]] = []
    for _, group in groupby(nodes, key=lambda item: item[0]):
        result.append([val for _, _, val in group])

    return result
```
