from collections import Counter

def character_replacement(s: str, k: int) -> int:
    """Calculates maximum length of repeating character substring after at most k replacements."""
    counts = Counter()
    left = 0
    max_freq = 0
    max_len = 0
    
    for right in range(len(s)):
        counts[s[right]] += 1
        max_freq = max(max_freq, counts[s[right]])
        
        # Current window size is right - left + 1.
        # Number of replacements needed is window size - max_freq.
        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len
