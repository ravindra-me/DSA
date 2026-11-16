# Solution 4: Card Deck Revealing Order

> Spoiler warning: try [the exercise](../exercises/problem-04.md) first.

**Difficulty:** Medium/Hard | **Concept:** Simulating reverse FIFO transformations using queue state transitions

## Approach

We can simulate the process by tracking the indices of the result array using a queue. By sorting `deck` in ascending order, we fill the output positions indicated by the queue following the exact rules: take the top index to place the current smallest available card, then move the next index to the back of the queue.

## Thought Process

The problem asks for an initial arrangement of cards such that revealing them following a specific rule results in a sorted order. Instead of working backwards from the sorted cards, we can simulate the physical process using card positions (indices `0` to `N-1`).

If we put index placeholders `0, 1, ..., N-1` in a double-ended queue, the simulation dictates:
1. Dequeue the front index `i`—this is where the smallest remaining card goes.
2. Dequeue the next front index `j` and enqueue it to the back (moving the next card to the bottom of the deck).

Since the revealed cards must be in strictly increasing order, we first sort `deck`. Then, as we step through the sorted cards from smallest to largest, we assign each card to the index popped from our queue.

## Algorithm

1. Sort the input `deck` in non-decreasing order.
2. Initialize a double-ended queue `index_queue` with integers from `0` to `len(deck) - 1`.
3. Create a result array `ans` of size `len(deck)`.
4. Iterate through each `card` in the sorted `deck`:
5. Pop the front index from `index_queue` and place `card` at `ans[index]`.
6. If `index_queue` is not empty, pop the front index and push it to the back of `index_queue`.
7. Return `ans`.

## Complexity Analysis

- **Time:** O(N log N) where N is the number of cards in `deck`. Sorting the deck takes O(N log N) time, and processing the queue takes O(N) time with O(1) deque operations.
- **Space:** O(N) auxiliary space to store the index queue and the result array.

## Edge Cases

- Single card (`len(deck) == 1`): The queue processes 1 element immediately without any moving to the back; returns `[deck[0]]`.
- Two cards (`len(deck) == 2`): First card is assigned to index 0, second card to index 1.
- Already sorted or reverse sorted decks: Handled correctly as the input is explicitly sorted first.

## Implementation

Source: [`solutions/problem_04.py`](../solutions/problem_04.py) · Tests: [`tests/test_problem_04.py`](../tests/test_problem_04.py)

```python
from collections import deque

def deck_revealed_increasing(deck: list[int]) -> list[int]:
    """Reconstruct the deck order that reveals cards in increasing numerical order."""
    n = len(deck)
    sorted_deck = sorted(deck)
    index_queue = deque(range(n))
    result = [0] * n
    
    for card in sorted_deck:
        result[index_queue.popleft()] = card
        if index_queue:
            index_queue.append(index_queue.popleft())
            
    return result
```
