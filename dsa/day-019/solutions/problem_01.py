def is_anagram(s: str, t: str) -> bool:
    """Return True if t is an anagram of s, otherwise False."""
    if len(s) != len(t):
        return False

    counts = [0] * 26
    offset = ord('a')
    for char_s, char_t in zip(s, t):
        counts[ord(char_s) - offset] += 1
        counts[ord(char_t) - offset] -= 1

    return all(count == 0 for count in counts)
