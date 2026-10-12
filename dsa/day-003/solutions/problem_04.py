def longest_palindrome(s: str) -> str:
    """Find the longest palindromic substring by expanding around centers."""
    if len(s) <= 1:
        return s

    start = 0
    max_len = 1
    n = len(s)

    def expand(left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        # Loop terminates when s[left] != s[right] or out of bounds
        return left + 1, right - 1

    for i in range(n):
        # Odd-length palindrome centered at i
        l1, r1 = expand(i, i)
        len1 = r1 - l1 + 1
        if len1 > max_len:
            start = l1
            max_len = len1

        # Even-length palindrome centered between i and i + 1
        l2, r2 = expand(i, i + 1)
        len2 = r2 - l2 + 1
        if len2 > max_len:
            start = l2
            max_len = len2

    return s[start:start + max_len]
