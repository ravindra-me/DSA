from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group a list of strings into anagram clusters."""
    groups: defaultdict[tuple[int, ...], list[str]] = defaultdict(list)
    ord_a = ord("a")

    for word in words:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord_a] += 1
        groups[tuple(count)].append(word)

    return list(groups.values())
