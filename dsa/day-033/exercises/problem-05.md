# Problem 5: Simulate External K-Way Merge Sort

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Chunk-based external sorting and multiway merging with bounded memory buffer | [Day 33: Merge Sort](../README.md) |

## Problem Statement

You are given a simulated unsorted external stream of numbers `stream` and a memory buffer limit `chunk_size`. Simulate the two-phase external merge sort algorithm:
1. **Run Generation Phase**: Read the stream in consecutive chunks of size up to `chunk_size`. Sort each chunk independently in memory in non-decreasing order. Each sorted chunk is a 'run'.
2. **K-Way Merge Phase**: Simultaneously merge all runs into a single non-decreasing sorted list using a min-heap, maintaining at most one element per active run in memory at any time.

Return the final fully sorted list.

## Input

`stream: list[int]`, the input data sequence; `chunk_size: int`, maximum number of elements allowed in memory during run creation.

## Output

`list[int]`, the fully sorted sequence in non-decreasing order.

## Constraints

- 0 <= len(stream) <= 10^5
- 1 <= chunk_size <= 10^4
- -10^9 <= stream[i] <= 10^9

## Examples

**Example 1**

```text
Input:  stream = [7, 1, 5, 2, 9, 3, 8, 4, 6], chunk_size = 3
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Runs created: [1, 5, 7], [2, 3, 9], [4, 6, 8]. Merging them via min-heap produces [1, 2, 3, 4, 5, 6, 7, 8, 9].

**Example 2**

```text
Input:  stream = [], chunk_size = 5
Output: []
```

Empty stream returns an empty list.

**Example 3**

```text
Input:  stream = [42], chunk_size = 10
Output: [42]
```

Single element produces a single run.

## Function Signature

```python
def external_k_way_sort(stream: list[int], chunk_size: int) -> list[int]:
    """Simulates external merge sort using chunked runs and a min-heap k-way merge."""
    pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Slice `stream` into blocks of length `chunk_size`, sort each block. Then initialize a min-heap with tuples `(run[0], run_idx, element_idx)`. Repeatedly pop the min element, append to result, and push the next element from that run until the heap is empty.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
