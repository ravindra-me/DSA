# Solution 2: In-Place Max-Heapify Subtree

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Sift-Down / Heapify Routine

## Approach

In a max-heap, every parent node must be greater than or equal to both of its children. When a node violates this property, we iteratively compare it with its left (`2*i + 1`) and right (`2*i + 2`) children within the active boundary `heap_size`. If the largest value among the parent and existing children is a child, we swap the parent with that largest child and continue sifting down from the child's index until the heap property is restored or a leaf is reached.

## Thought Process

When constructing or maintaining a binary max-heap represented as an array, the fundamental primitive is `sift_down` (or `max_heapify`). Given that both subtrees of node `i` already satisfy the max-heap property, node `i` might be smaller than one or both of its children.

To restore the max-heap invariant for the subtree at index `i`, we must find the maximum of `nums[i]`, `nums[left]`, and `nums[right]`. If `nums[i]` is already the largest, the subtree is valid and we can terminate early. Otherwise, we swap `nums[i]` with the larger child. This swap guarantees the new root of this subtree is maximal. However, moving the smaller element down may violate the max-heap property in the child's subtree, so we continue the process iteratively down that branch.

An iterative approach is preferred over recursion to avoid call stack overhead and guarantee $O(1)$ auxiliary space.

## Algorithm

1. Initialize `curr = i`.
2. While `curr` has at least a left child within the heap (`2 * curr + 1 < heap_size`):
3. Calculate indices `left = 2 * curr + 1` and `right = 2 * curr + 2`.
4. Determine `largest = curr`. If `nums[left] > nums[largest]`, set `largest = left`.
5. If `right < heap_size` and `nums[right] > nums[largest]`, set `largest = right`.
6. If `largest == curr`, the max-heap property is satisfied at this level; break and terminate.
7. Otherwise, swap `nums[curr]` and `nums[largest]`, update `curr = largest`, and repeat.

## Complexity Analysis

- **Time:** $O(\log n)$ where $n = \text{heap\_size}$. At each step, the algorithm descends one level down the binary tree, performing $O(1)$ comparisons. The maximum height of the tree is $\lfloor \log_2(\text{heap\_size}) \rfloor$.
- **Space:** $O(1)$ auxiliary space. The operation is performed iteratively in-place without recursion or extra memory allocations.

## Edge Cases

- No children (leaf node): Loop condition `2 * curr + 1 < heap_size` immediately evaluates to false, terminating with no swaps.
- Only one child (left child exists, right child does not): Handled cleanly by checking `right < heap_size` before comparing the right child.
- heap_size <= 1: Sift-down does nothing as there are no children.
- Duplicate elements: Strict inequality (`>`) ensures stability and prevents unnecessary swaps when parent equals a child.
- Negative numbers and zeros: Handled correctly as standard comparison applies.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
def sift_down(nums: list[int], heap_size: int, i: int) -> None:
    """Sift down the element at index i within the heap boundaries [0, heap_size - 1]."""
    curr = i
    while True:
        left = 2 * curr + 1
        right = 2 * curr + 2
        largest = curr

        if left < heap_size and nums[left] > nums[largest]:
            largest = left
        if right < heap_size and nums[right] > nums[largest]:
            largest = right

        if largest == curr:
            break

        nums[curr], nums[largest] = nums[largest], nums[curr]
        curr = largest
```
