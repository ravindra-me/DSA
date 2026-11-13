from collections import Counter

def remove_duplicate_letters(s: str) -> str:
    """Remove duplicate letters to return lexicographically smallest result while preserving order."""
    count = Counter(s)
    stack = []
    visited = set()
    
    for char in s:
        count[char] -= 1
        if char in visited:
            continue
            
        while stack and stack[-1] > char and count[stack[-1]] > 0:
            removed = stack.pop()
            visited.remove(removed)
            
        stack.append(char)
        visited.add(char)
        
    return "".join(stack)
