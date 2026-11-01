def longest_awesome(s: str) -> int:
    """Find length of longest substring that can be rearranged into a palindrome."""
    seen = [-2] * 1024
    seen[0] = -1
    
    mask = 0
    max_len = 0
    
    for i, ch in enumerate(s):
        digit = ord(ch) - ord('0')
        mask ^= (1 << digit)
        
        # Case 1: All digits in substring have even count
        if seen[mask] != -2:
            max_len = max(max_len, i - seen[mask])
        
        # Case 2: Exactly one digit in substring has odd count
        for d in range(10):
            target_mask = mask ^ (1 << d)
            if seen[target_mask] != -2:
                max_len = max(max_len, i - seen[target_mask])
        
        # Record first time seeing this mask
        if seen[mask] == -2:
            seen[mask] = i
            
    return max_len
