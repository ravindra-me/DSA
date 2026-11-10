def remove_k_duplicates(s: str, k: int) -> str:
    """Remove all k-adjacent duplicates from string s repeatedly."""
    stack = []  # Element structure: [char, count]
    
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([char, 1])
            
    return "".join(char * count for char, count in stack)
