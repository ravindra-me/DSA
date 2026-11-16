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
