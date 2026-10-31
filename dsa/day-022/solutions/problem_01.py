def is_valid_palindrome(s: str) -> bool:
    """Return True if s is a palindrome considering only alphanumeric chars, case-insensitively."""
    left: int = 0
    right: int = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
