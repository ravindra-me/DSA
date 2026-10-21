# Problem 2: Online Stock Span

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Easy/Medium | Previous greater element tracking across a streaming sequence | [Day 12: Monotonic Stack](../README.md) |

## Problem Statement

Design an algorithm that collects daily price quotes for a stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

Implement the `StockSpanner` class:
- `__init__()` Initializes the object of the class.
- `next(price: int) -> int` Returns the span of the stock's price given that today's price is `price`.

## Input

`price: int` passed sequentially to `next()`.

## Output

`int` representing the span for the current day.

## Constraints

- 1 <= price <= 10^5
- At most 10^5 calls will be made to next.

## Examples

**Example 1**

```text
Input:  spanner = StockSpanner()
[spanner.next(p) for p in [100, 80, 60, 70, 60, 75, 85]]
Output: [1, 1, 1, 2, 1, 4, 6]
```

When 75 arrives, it covers 75, 60, 70, 60 (span 4). When 85 arrives, it covers all except 100 (span 6).

**Example 2**

```text
Input:  spanner = StockSpanner()
[spanner.next(p) for p in [10, 20, 30, 40]]
Output: [1, 2, 3, 4]
```

Strictly increasing prices accumulate the entire history up to that point.

## Function Signature

```python
class StockSpanner:
    """Calculates stock span for consecutive streaming prices."""
    def __init__(self) -> None:
        pass

    def next(self, price: int) -> int:
        pass
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Maintain a monotonic decreasing stack containing pairs of `(price, span)`. When a new price is greater than or equal to the top, pop and add its span. Target amortized $O(1)$ time per call.

</details>

## Your Turn

- Write your solution in [`practice/problem_02.py`](../practice/problem_02.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-02.md`](../solutions/problem-02.md), but try first!
