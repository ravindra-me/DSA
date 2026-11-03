# Problem 5: Stream Peak Detection

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Hard | Stateful streaming linear search over infinite dynamic window | [Day 25: Linear Search](../README.md) |

## Problem Statement

Implement a `StreamPeakFinder` class that receives integers one by one via a `process(val: int) -> int | None` method. The class must perform a linear stream scan to find local peaks. A local peak is defined as a value that is strictly greater than both its immediate predecessor and immediate successor in the stream. `process` should return the value of the peak as soon as the peak's successor is processed. If processing `val` completes a new peak, return the peak value. Otherwise, return `None`.

## Input

Sequential calls to `process(val: int)`.

## Output

Returns `int` (the peak value) when a peak is finalized by the current call, otherwise `None`.

## Constraints

- Calls to process <= 10^5
- -10^9 <= val <= 10^9

## Examples

**Example 1**

```text
Input:  Calls: process(3), process(7), process(2)
Output: Returns: None, None, 7
```

When 2 arrives, 7 is confirmed as greater than both 3 and 2. Peak 7 is returned.

**Example 2**

```text
Input:  Calls: process(1), process(2), process(3)
Output: Returns: None, None, None
```

No peak found yet since 2 < 3.

## Function Signature

```python
class StreamPeakFinder:
    def __init__(self):
        pass
    def process(self, val: int) -> int | None:
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a rolling 3-element buffer state during sequential stream processing. Target complexity: O(1) time per call, O(1) space.

</details>

## Your Turn

- Write your solution in [`practice/problem_05.py`](../practice/problem_05.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-05.md`](../solutions/problem-05.md), but try first!
