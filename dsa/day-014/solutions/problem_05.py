def shortest_palindrome(s: str) -> str:
    """Find the shortest palindrome by prepending characters to s."""
    if len(s) <= 1:
        return s

    # Combine s, a delimiter, and reversed s
    # The delimiter '#' ensures prefix matches cannot span across the two parts.
    rev_s = s[::-1]
    combined = s + "#" + rev_s
    n = len(combined)

    # Compute KMP prefix table (pi array)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and combined[i] != combined[j]:
            j = pi[j - 1]
        if combined[i] == combined[j]:
            j += 1
        pi[i] = j

    # pi[-1] is the length of the longest palindromic prefix of s
    longest_pal_prefix_len = pi[-1]
    non_pal_suffix = s[longest_pal_prefix_len:]
    return non_pal_suffix[::-1] + s
