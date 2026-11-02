def length_of_longest_substring(s: str) -> int:
    """Returns the length of the longest substring without repeating characters."""
    last_seen = {}
    max_len = 0
    left = 0
    
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len
