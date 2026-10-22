from collections import deque

def predict_party_victory(senate: str) -> str:
    """Predict which party wins the vote following optimal FIFO ban logic."""
    r_queue: deque[int] = deque()
    d_queue: deque[int] = deque()
    
    for idx, char in enumerate(senate):
        if char == "R":
            r_queue.append(idx)
        else:
            d_queue.append(idx)
            
    n = len(senate)
    while r_queue and d_queue:
        r_idx = r_queue.popleft()
        d_idx = d_queue.popleft()
        
        if r_idx < d_idx:
            r_queue.append(r_idx + n)
        else:
            d_queue.append(d_idx + n)
            
    return "Radiant" if r_queue else "Dire"
