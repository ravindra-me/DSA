from collections import deque


def is_deque_palindrome(s: str) -> bool:
    """Return True if s is a palindrome using a deque for matching."""
    char_deque: deque[str] = deque(
        ch.lower() for ch in s if ch.isalnum()
    )

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True
