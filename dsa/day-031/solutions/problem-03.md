# Solution 3: Sort Nearly-Sorted Array (k-Sorted)

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** Insertion sort efficiency on inputs with bounded inversion distance

## Approach

Standard insertion sort works by taking each element and shifting it left into its sorted position within the already sorted prefix. In a $k$-sorted array, an element is guaranteed to be at most $k$ positions away from its final sorted position, meaning the inner loop of insertion sort executes at most $k$ times per element, yielding an optimal $O(n \cdot k)$ time and $O(1)$ space in-place sort.

## Thought Process

When faced with a nearly-sorted array where every element is within $k$ positions of its sorted spot, general-purpose $O(n \log n)$ sorting algorithms (or $O(n \log k)$ min-heap approaches) are commonly used. However, min-heaps require $O(k)$ auxiliary space to hold the sliding window of size $k + 1$.

Notice that the inner step of insertion sort terminates as soon as it encounters an element smaller than or equal to the key being inserted. Since the element starts within at most $k$ positions to the right of its target position (relative to the sorted prefix), it will never need to shift left more than $k$ times (and at most $2k$ comparisons in worst-case relative inversions, but bounded strictly by $O(k)$ shifts). Thus, the standard in-place insertion sort naturally achieves $O(n \cdot k)$ time complexity without requiring any modifications or auxiliary data structures.

## Algorithm

1. Check if the length of the array $n$ is less than 2; if so, return the array immediately.
2. Iterate with index $i$ from 1 to $n - 1$, setting `key = arr[i]`.
3. Initialize an inner index $j = i - 1$.
4. While $j \ge 0$ and $arr[j] > key$, shift $arr[j]$ to $arr[j + 1]$ and decrement $j$. Because the array is $k$-sorted, this loop iterates at most $O(k)$ times.
5. Place `key` into $arr[j + 1]$.
6. Return the mutated array $arr$.

## Complexity Analysis

- **Time:** $O(n \cdot k)$ because there are $n$ elements, and each element shifts left at most $O(k)$ positions due to the $k$-sorted guarantee.
- **Space:** $O(1)$ auxiliary space because elements are shifted in-place with only a few scalar variables.

## Edge Cases

- Empty array: the outer loop does not execute; empty list returned immediately.
- Single element array: the outer loop range is empty; single element list returned unchanged.
- k = 0 (already sorted array): the while-condition `arr[j] > key` fails immediately on the first check, running in $O(n)$ time.
- Duplicate elements: strict inequality `arr[j] > key` ensures stability and avoids unnecessary shifts.
- Negative numbers and extreme values: standard integer comparisons handle negative numbers, zeroes, and large values correctly.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def sort_k_sorted(arr: list[int], k: int) -> list[int]:
    """Sorts a k-sorted array in-place in O(n * k) time using insertion sort."""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```
