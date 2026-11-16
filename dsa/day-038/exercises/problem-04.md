# Problem 4: Card Deck Revealing Order

| Difficulty | Related concept | Day |
|------------|-----------------|-----|
| Medium/Hard | Simulating reverse FIFO transformations using queue state transitions | [Day 38: Queue](../README.md) |

## Problem Statement

You are given an integer array `deck` representing a deck of numbered cards. You want to arrange the cards in a specific order such that when they are revealed according to the following process, the cards are revealed in strictly increasing order:

1. Take the top card of the deck, reveal it, and take it out of the deck.
2. If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
3. If there are still unrevealed cards, go back to step 1. Otherwise, stop.

Return an ordering of the deck that will reveal the cards in increasing sorted order.

Note: The first entry in the returned array represents the top of the deck.

## Input

A list of integers `deck`.

## Output

A list of integers representing the original deck configuration.

## Constraints

- 1 <= len(deck) <= 10^4
- 1 <= deck[i] <= 10^6
- All elements of deck are distinct.

## Examples

**Example 1**

```text
Input:  deck = [17, 13, 11, 2, 3, 5, 7]
Output: [2, 13, 3, 11, 5, 17, 7]
```

Initially arranged [2, 13, 3, 11, 5, 17, 7]: reveal 2, put 13 to bottom -> deck is [3, 11, 5, 17, 7, 13]; reveal 3, put 11 to bottom -> ... revealed order is [2, 3, 5, 7, 11, 13, 17].

**Example 2**

```text
Input:  deck = [1]
Output: [1]
```

Single card is revealed immediately.

## Function Signature

```python
def deck_revealed_increasing(deck: list[int]) -> list[int]:
    """Reconstruct the deck order that reveals cards in increasing numerical order."""
```

## Expected Approach (hint)

<details>
<summary>Show hint</summary>

Sort the cards, then simulate the process on card index positions using a queue to determine which index gets revealed at each step. Target O(N log N) time.

</details>

## Your Turn

- Write your solution in [`practice/problem_04.py`](../practice/problem_04.py).
- Run the tests with `DSA_SOLUTIONS_DIR=practice` (see the [lesson README](../README.md#how-to-practice)).
- Stuck? The full walkthrough is in [`solutions/problem-04.md`](../solutions/problem-04.md), but try first!
