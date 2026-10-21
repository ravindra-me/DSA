# Solution 2: Online Stock Span

> Spoiler warning: try [the exercise](../exercises/problem-02.md) first.

**Difficulty:** Easy/Medium | **Concept:** Previous greater element tracking across a streaming sequence

## Approach

Maintain a monotonic decreasing stack of pairs `(price, span)`. When a new price arrives, initialize its span to 1 and repeatedly pop elements from the stack whose prices are less than or equal to the current price, adding their spans to the current span before pushing `(price, span)` onto the stack.

## Thought Process

A naive approach records every price seen so far in an array. For each new price, it walks backward until encountering a strictly greater price. In the worst case (strictly decreasing prices followed by large spikes or sorted in non-increasing order), this takes $O(N)$ per call, leading to $O(N^2)$ overall for $N$ calls.

Notice that if a past price $p_{prev} \le price_{current}$, any future query that spans across $price_{current}$ will also span across $p_{prev}$ without needing to inspect $p_{prev}$ directly. Thus, $price_{current}$ can 'subsume' the span of $p_{prev}$.

By storing pairs of `(price, span)` in a strictly decreasing stack, each element pushed is popped at most once across the lifetime of the object. This guarantees that $N$ consecutive operations take amortized $O(1)$ time each.

## Algorithm

1. Initialize an empty list `stack` to hold tuples of `(price, span)`.
2. When `next(price)` is called, initialize `span = 1`.
3. While `stack` is non-empty and `stack[-1][0] <= price`, pop `(prev_price, prev_span)` from `stack` and add `prev_span` to `span`.
4. Push `(price, span)` onto `stack`.
5. Return `span`.

## Complexity Analysis

- **Time:** Amortized $O(1)$ per `next()` call, totaling $O(N)$ for $N$ calls. Each price is pushed onto the stack once and popped at most once.
- **Space:** $O(N)$ overall space to store up to $N$ price-span pairs in the stack in the worst case (strictly decreasing prices).

## Edge Cases

- Strictly decreasing sequence: No elements are popped; each returns a span of 1.
- Strictly increasing sequence: Every prior element is popped and merged; spans increase as 1, 2, 3, ...
- Duplicate consecutive prices: The condition `<=` ensures identical prices are absorbed into the span.
- Maximum constraint: Handling up to 10^5 calls efficiently without recursion or deep calls.

## Implementation

Source: [`solutions/problem_02.py`](../solutions/problem_02.py) · Tests: [`tests/test_problem_02.py`](../tests/test_problem_02.py)

```python
class StockSpanner:
    """Calculates stock span for consecutive streaming prices."""

    def __init__(self) -> None:
        # Stack stores tuples of (price, span)
        self._stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        span = 1
        while self._stack and self._stack[-1][0] <= price:
            span += self._stack.pop()[1]
        self._stack.append((price, span))
        return span
```
