def reverse_string(s: str) -> str:
    """Reverses a string using recursion."""
    if len(s) <= 1:
        return s
    
    return reverse_string(s[1:]) + s[0]
