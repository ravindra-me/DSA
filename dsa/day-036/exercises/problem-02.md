# Problem 2: In-Place Max-Heapify Subtree

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Sift-Down / Heapify Routine | [Day 36: Heap Sort](../README.md) |

## Problem Statement

Given an array `nums`, an integer `heap_size` representing the active heap boundary (where elements from index `0` to `heap_size - 1` belong to the heap), and an index `i`, perform the standard `sift_down` operation on node `i` in-place so that the subtree rooted at `i` satisfies the max-heap property.

You may assume the subtrees rooted at both children of `i` already satisfy the max-heap property within `heap_size`.

## Input

- `nums: list[int]` - The array containing the heap.
- `heap_size: int` - The size of the active heap range ($0 \le \text{heap\_size} \le \text{len}(nums)$).
- `i: int` - The root index of the subtree to sift down ($0 \le i < \text{heap\_size}$).

## Output

None (modifies `nums` in-place).

## Constraints

- 1 <= len(nums) <= 10^5
- 0 <= heap_size <= len(nums)
- 0 <= i < heap_size if heap_size > 0
- -10^9 <= nums[j] <= 10^9

## Examples

**Example 1**

```text
Input:  nums = [1, 14, 10, 8, 7, 9, 3, 2, 4, 6], heap_size = 10, i = 0
Output: [14, 8, 10, 4, 7, 9, 3, 2, 1, 6]
```

1 sifts down past 14 and 8 until it reaches index 8.

**Example 2**

```text
Input:  nums = [5, 4, 3, 2, 1], heap_size = 5, i = 0
Output: [5, 4, 3, 2, 1]
```

The root 5 is already greater than both its children 4 and 3, so no swaps are needed.

## Function Signature

```python
def sift_down(nums: list[int], heap_size: int, i: int) -> None:
    """Sift down the element at index i within the heap boundaries [0, heap_size - 1]."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Compare nums[i] with its left and right children within heap_size. Swap with the larger child if necessary and repeat down the tree in O(log n) time and O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
